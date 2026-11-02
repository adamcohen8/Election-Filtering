"""Replay the separately reviewed Nebraska Senate acquisition, preserving prior inputs."""
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path
import tempfile

import numpy as np

from ingest_senate_research import ROOT, compile_research, digest, replay, write_json
from research_revisions import original_rows, same_race_inputs
from election_modeling.cycles import RACES_2026_BY_ID, create_2026_election_model
from election_modeling.persistence import load_election_model, save_election_model
from election_modeling.public import public_forecast_payload, public_race_history_payload

BASE = ROOT / "research/nebraska_senate_polls_20261101"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    config = json.loads((BASE / "review-decisions.json").read_text())
    selected, held = compile_research(BASE, config, race_specs=(RACES_2026_BY_ID["ne_sen"],))
    for row in selected:
        assert (row["candidate_a"], row["candidate_b"]) == ("Pete Ricketts", "Dan Osborn")
        assert (row["candidate_a_party"], row["candidate_b_party"]) == ("republican", "independent")
        row["acquisition_id"] = BASE.name
    feed_path = ROOT / "data/ingestion/2026_normalized_polls.json"
    existing = json.loads(feed_path.read_text())["polls"]
    retained = [r for r in existing if r.get("acquisition_id") != BASE.name]
    baseline = json.loads((BASE / "baseline/polls-before.json").read_text())["polls"]
    retained_by_id = {r["poll_id"]: r for r in original_rows(retained)}
    if any(retained_by_id.get(r["poll_id"]) != r for r in baseline):
        raise ValueError("Nebraska acquisition changed a pre-existing feed row")
    rows = sorted(retained + selected, key=lambda r: (r["field_date"], r["poll_id"]))
    election, ledger = replay(rows)
    previous = load_election_model(BASE / "baseline/model-before.json")
    configured = create_2026_election_model()
    for race_id, model in previous.races.items():
        if race_id == "ne_sen" or not same_race_inputs(rows, baseline, race_id):
            continue
        current = election.races[race_id]
        np.testing.assert_array_equal(current.filter.joint_mean, model.filter.joint_mean)
        np.testing.assert_allclose(current.filter.joint_covariance, model.filter.joint_covariance, atol=1e-15, rtol=0)
        # Turnout assumptions may be intentionally revised after this acquisition.
        assert current.electorate == configured.races[race_id].electorate
        assert current.observation_count == model.observation_count
    electorate = election.races["ne_sen"].electorate
    assert (electorate.republican, electorate.democratic, electorate.independent) == (.57, .24, .19)
    artifacts = set()
    for row in selected:
        assert row["evidence_artifacts"]
        for artifact in row["evidence_artifacts"]:
            assert hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest() == artifact["sha256"]
            artifacts.add(artifact["path"])
    forecasts = public_forecast_payload(election)
    ne = next(r for r in forecasts["races"] if r["race_id"] == "ne_sen")
    assert ne["candidate_b_party"] == "Independent"
    with tempfile.TemporaryDirectory(prefix="nebraska-replay-") as directory:
        staged = Path(directory) / "polls.json"
        write_json(staged, {"polls": rows})
        history = public_race_history_payload(feed_path=staged)
    count = len(selected)
    manifest = {
        "acquisition_id": BASE.name, "accepted_count": count, "held": held,
        "counts_by_race": {"ne_sen": count}, "window": config["window"],
        "in_window_count": sum(not r.get("backfill_original_cutoff") for r in selected),
        "backfill_count": sum(bool(r.get("backfill_original_cutoff")) for r in selected),
        "shortfall_to_ten": max(0, 10-count), "party_basis_counts": dict(Counter(r["crosstab_basis"] for r in selected)),
        "precision_methods": dict(Counter(r["model_base_method"] for r in selected)),
        "accepted_poll_ids": [r["poll_id"] for r in selected],
        "electorate": {"republican": .57, "democratic": .24, "independent": .19,
                       "provisional": False, "basis": "User-selected R57/D24/I19, updated November1 2026"},
        "source_artifacts_hash_checked": len(artifacts), "retained_baseline_rows": len(baseline),
        "prior_race_states_preserved": len(previous.races),
        "review_decisions_sha256": digest(config), "acquisition_rows_sha256": digest(selected),
        "feed_sha256": digest(rows), "limitations": config["limitations"],
    }
    if not args.check:
        write_json(feed_path, {"polls": rows})
        save_election_model(election, ROOT / "data/models/2026_election_model.json")
        ledger.path = ROOT / "data/ingestion/2026_seen_polls.json"
        ledger.save()
        write_json(ROOT / "docs/data/forecasts.json", forecasts)
        write_json(ROOT / "docs/data/race-history.json", history)
        write_json(BASE / "ingestion-manifest.json", manifest)
    print(json.dumps({"check_only": args.check, **manifest}, indent=2))


if __name__ == "__main__":
    main()
