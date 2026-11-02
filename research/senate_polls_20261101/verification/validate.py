"""Offline integrity check of reviewed inputs, replay, snapshot and exports."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from ingest_senate_research import compile_research, digest, replay
from election_modeling.persistence import load_election_model


def main():
    base = Path(__file__).resolve().parents[1]
    decisions = json.loads((base / "review-decisions.json").read_text())
    accepted, held = compile_research(base, decisions)
    feed = json.loads((ROOT / "data/ingestion/2026_normalized_polls.json").read_text())["polls"]
    acquisition_feed = [r for r in feed if r.get("acquisition_id") == base.name]
    election, ledger = replay(feed)
    saved = load_election_model(ROOT / "data/models/2026_election_model.json")
    manifest = json.loads((base / "ingestion-manifest.json").read_text())
    forecasts = json.loads((ROOT / "docs/data/forecasts.json").read_text())
    # Later acquisitions may share the feed; the archived Senate manifest pins
    # its original rows, while the complete replay below verifies today's model.
    assert manifest["feed_sha256"] == digest(acquisition_feed)
    assert manifest["review_decisions_sha256"] == digest(decisions)
    assert len(acquisition_feed) == len(accepted)
    assert len(feed) == sum(m.observation_count for m in saved.races.values())
    assert len({r["sample_id"] for r in feed}) == len(feed)
    artifacts = set()
    for row in acquisition_feed:
        for artifact in row["evidence_artifacts"]:
            path = ROOT / artifact["path"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == artifact["sha256"]
            artifacts.add(artifact["path"])
    maximum_covariance_difference = 0.0
    for race_id, model in election.races.items():
        restored = saved.races[race_id]
        np.testing.assert_array_equal(model.filter.joint_mean, restored.filter.joint_mean)
        # Snapshot PSD validation may repair machine-roundoff eigenvalues.
        np.testing.assert_allclose(model.filter.joint_covariance, restored.filter.joint_covariance,
                                   atol=1e-15, rtol=0)
        maximum_covariance_difference = max(maximum_covariance_difference,
            float(np.max(np.abs(model.filter.joint_covariance - restored.filter.joint_covariance))))
        assert model.electorate.share_standard_deviation == .01
    for row in forecasts["races"]:
        if row["data_available"]:
            assert row["forecast_date"] == "2026-11-03"
            assert row["candidate_a_share"] >= 0 and row["candidate_b_share"] >= 0
            assert row["candidate_a_share"] + row["candidate_b_share"] <= 1.0001
        assert row["observation_count"] == saved.races[row["race_id"]].observation_count
    mn = saved.races["mn_sen"]
    assert (mn.electorate.republican, mn.electorate.democratic, mn.electorate.independent) == (.34, .37, .29)
    actual_ledger = json.loads((ROOT / "data/ingestion/2026_seen_polls.json").read_text())
    assert set(actual_ledger["seen_poll_ids"]) == ledger.seen_poll_ids
    assert set(actual_ledger["measurement_keys"]) == ledger.measurement_keys
    for row in acquisition_feed:
        if row["model_base_method"] == "assumed_covariance":
            assert row.get("crosstab_covariance") is not None
            for party in ("republican", "democratic", "independent"):
                if row["source_subgroup_bases"][party] is None:
                    assert row[party + "_n"] is None
        if row["crosstab_basis"] in {"modeled_party_id", "modeled_subgroup_estimate", "party_basis_unspecified"}:
            assert row["proxy_inclusion_authorized"] is True
    exact_publications = [r["publication_date"] for r in acquisition_feed if r.get("publication_date")]
    publication_bounds = [r.get("publication_date_bounds", [r.get("publication_date")] * 2) for r in acquisition_feed]
    backfill_counts = dict(Counter(r["race_id"] for r in acquisition_feed if r.get("backfill_original_cutoff")))
    below_target = {}
    baseline_unchanged = None
    if decisions.get("backfill_policy"):
        policy = decisions["backfill_policy"]
        counts = Counter(r["race_id"] for r in acquisition_feed)
        below_target = {race: policy["target_count"] - counts[race]
                        for race in policy["target_races"] if counts[race] < policy["target_count"]}
        assert below_target == policy["unfilled"]
        before = json.loads((base / "backfill_revision/before-review-decisions.json").read_text())
        original, _ = compile_research(base, before)
        current_by_id = {r["poll_id"]: {k: v for k, v in r.items() if k != "acquisition_id"} for r in feed}
        assert all(current_by_id[r["poll_id"]] == r for r in original)
        baseline_unchanged = True
    report = {
        "checked_on": "2026-11-01", "reviewed_records": len(accepted) + len(held),
        "accepted_waves": len(acquisition_feed), "held_records": len(held), "distinct_samples": len(acquisition_feed),
        "models": len(saved.races),
        "senate_models_with_data": sum(k.endswith("_sen") and m.observation_count > 0 for k, m in saved.races.items()),
        "party_basis_counts": dict(Counter(r["crosstab_basis"] for r in acquisition_feed)),
        "model_base_method_counts": dict(Counter(r["model_base_method"] for r in acquisition_feed)),
        "field_date_range": [min(r["field_date"] for r in acquisition_feed), max(r["field_date"] for r in acquisition_feed)],
        "publication_date_range": [min(exact_publications), max(exact_publications)],
        "publication_date_range_including_bounds": [min(v[0] for v in publication_bounds), max(v[1] for v in publication_bounds)],
        "publication_dates_bounded_not_exact": sum(r.get("publication_date") is None for r in acquisition_feed),
        "backfill_counts": backfill_counts, "remaining_shortfall": below_target,
        "baseline_rows_unchanged": baseline_unchanged,
        "explicit_covariance_count": sum(r["model_base_method"] == "assumed_covariance" for r in acquisition_feed),
        "feed_sha256": digest(acquisition_feed), "full_feed_sha256": digest(feed), "replay_matches_snapshot_atol": 1e-15,
        "maximum_restored_covariance_difference": maximum_covariance_difference,
        "source_artifacts_hash_checked": len(artifacts), "ledger_matches_replay": True,
        "turnout_sd_1pp_all_races": True, "minnesota_weights": [.34, .37, .29],
        "governor_and_generic_models_prior_only": all(m.observation_count == 0 for k, m in saved.races.items() if k.endswith("_gov") or k == "us_house_generic"),
        "test_limitations": ["Historical Maine calibration requires the original datasets, intentionally not cloned. No forecast calibration or accuracy validation claimed."],
    }
    (base / "verification/validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
