"""Offline governor source, acquisition, replay and preservation audit."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "scripts"), str(ROOT / "src")]
from ingest_governor_research import compile_governors
from ingest_senate_research import digest, replay
from research_revisions import original_rows, same_race_inputs
from election_modeling.persistence import load_election_model
from election_modeling.public import public_forecast_payload, public_race_history_payload
from election_modeling.cycles import RACES_2026


def main():
    base = Path(__file__).resolve().parents[1]
    config = json.loads((base / "review-decisions.json").read_text())
    selected, held = compile_governors(base, config)
    for row in selected:
        row["acquisition_id"] = base.name
    feed_path = ROOT / "data/ingestion/2026_normalized_polls.json"
    feed = json.loads(feed_path.read_text())["polls"]
    current = [r for r in original_rows(feed) if r.get("acquisition_id") == base.name]
    assert current == selected
    manifest = json.loads((base / "ingestion-manifest.json").read_text())
    # Later acquisitions may extend the feed; this manifest pins governor rows.
    assert manifest["acquisition_rows_sha256"] == digest(selected)
    assert manifest["review_decisions_sha256"] == digest(config)
    before = json.loads((base / "baseline/normalized-polls-before.json").read_text())["polls"]
    retained = [r for r in feed if r.get("acquisition_id") != base.name]
    retained_by_id = {r["poll_id"]: r for r in retained}
    assert all(retained_by_id.get(r["poll_id"]) == r for r in before)
    election, ledger = replay(feed)
    saved = load_election_model(ROOT / "data/models/2026_election_model.json")
    previous_model = load_election_model(base / "baseline/model-before.json")
    assert set(election.races) == set(saved.races)
    assert len(saved.races) == len(RACES_2026) and "ak_gov" not in saved.races
    for race, model in election.races.items():
        actual = saved.races[race]
        np.testing.assert_array_equal(model.filter.joint_mean, actual.filter.joint_mean)
        np.testing.assert_allclose(model.filter.joint_covariance, actual.filter.joint_covariance,
                                   atol=1e-15, rtol=0)
        assert model.observation_count == actual.observation_count
        assert actual.electorate.share_standard_deviation == .01
        if race.endswith("_sen") and race in previous_model.races and same_race_inputs(feed, before, race):
            prior = previous_model.races[race]
            np.testing.assert_array_equal(prior.filter.joint_mean, actual.filter.joint_mean)
            np.testing.assert_allclose(prior.filter.joint_covariance, actual.filter.joint_covariance,
                                       atol=1e-15, rtol=0)
            assert prior.observation_count == actual.observation_count
    mn = saved.races["mn_gov"].electorate
    assert (mn.republican, mn.democratic, mn.independent) == (.34, .37, .29)
    assert len(feed) == sum(m.observation_count for m in saved.races.values())
    actual_ledger = json.loads((ROOT / "data/ingestion/2026_seen_polls.json").read_text())
    assert set(actual_ledger["seen_poll_ids"]) == ledger.seen_poll_ids
    assert set(actual_ledger["measurement_keys"]) == ledger.measurement_keys
    # Export wall-clock generation timestamps differ on an independent replay.
    for expected, path in [
        (public_forecast_payload(election), ROOT / "docs/data/forecasts.json"),
        (public_race_history_payload(feed_path=feed_path), ROOT / "docs/data/race-history.json"),
    ]:
        actual = json.loads(path.read_text())
        expected = json.loads(json.dumps(expected))
        expected.pop("generated_at")
        actual.pop("generated_at")
        assert expected == actual
    artifacts = set()
    for row in selected:
        assert row["evidence_artifacts"], row["poll_id"]
        for artifact in row["evidence_artifacts"]:
            path = ROOT / artifact["path"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == artifact["sha256"]
            artifacts.add(artifact["path"])
        if row["model_base_method"] == "assumed_covariance":
            assert row.get("crosstab_covariance") is not None
            for party, source_n in row["source_subgroup_bases"].items():
                if source_n is None:
                    assert row[party + "_n"] is None
    nyt = [r for r in selected if "user_supplied_nyt" in r["research_source_path"]]
    assert len(nyt) == 6
    assert {r["state"] for r in nyt} == {"Florida", "Minnesota", "Kansas", "Iowa", "Ohio", "Texas"}
    censored = {r["race_id"]: r["support_approximations"] for r in selected if r.get("support_approximations")}
    assert censored["mn_gov"]["democratic_a"]["model_midpoint"] == .0025
    assert censored["me_gov"]["democratic_a"]["model_midpoint"] == .005
    counts = Counter(r["race_id"] for r in selected)
    shortfall = {k: 10-v for k,v in counts.items() if v < 10}
    assert shortfall == config["backfill_policy"]["unfilled"]
    assert dict(counts) == manifest["counts_by_race"]
    report = {
        "checked_on": "2026-11-01", "governor_waves": len(selected),
        "senate_rows_preserved": len(before), "total_feed_rows": len(feed),
        "governor_models_with_data": len(counts), "models": len(saved.races),
        "counts_by_race": dict(sorted(counts.items())), "shortfall_to_ten": shortfall,
        "in_window_count": sum(not r.get("backfill_original_cutoff") for r in selected),
        "older_backfill_count": sum(bool(r.get("backfill_original_cutoff")) for r in selected),
        "held_records": held, "user_supplied_nyt_tables": len(nyt),
        "censored_cell_approximations": censored,
        "precision_methods": dict(Counter(r["model_base_method"] for r in selected)),
        "source_artifacts_hash_checked": len(artifacts),
        "unchanged_input_senate_models_preserved": True, "senate_covariance_tolerance": 1e-15,
        "snapshot_ledger_forecasts_history_match_replay": True,
        "turnout_sd_1pp_all_races": True, "feed_sha256": digest(feed),
        "limitations": config["limitations"],
    }
    (base / "verification/validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
