"""Review and replay governor polling while preserving the existing Senate feed."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import tempfile

from ingest_senate_research import ROOT, compile_research, digest, replay, write_json
from research_revisions import apply_current_revisions
from election_modeling.cycles import GOVERNOR_2026_RACES
from election_modeling.nominees import NOMINEES_2026_BY_RACE
from election_modeling.persistence import save_election_model
from election_modeling.public import public_forecast_payload, public_race_history_payload

RESEARCH = ROOT / "research/governor_polls_20261101"


def compile_governors(base: Path, decisions: dict):
    selected, held = compile_research(base, decisions, race_specs=GOVERNOR_2026_RACES,
                                     expected_office="governor")
    for row in selected:
        nominees = NOMINEES_2026_BY_RACE[row["race_id"]]
        if (row["candidate_a"] != nominees.republican.name
                or row["candidate_b"] != nominees.democratic.name
                or row.get("candidate_a_party") != "republican"
                or row.get("candidate_b_party") != "democratic"):
            raise ValueError(f"wrong governor candidate matchup: {row['poll_id']}")
    return selected, held


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    decisions = json.loads((RESEARCH / "review-decisions.json").read_text())
    selected, held = compile_governors(RESEARCH, decisions)
    feed_path = ROOT / "data/ingestion/2026_normalized_polls.json"
    existing = json.loads(feed_path.read_text())["polls"]
    retained = [r for r in existing if r.get("acquisition_id") != RESEARCH.name]
    baseline = json.loads((RESEARCH / "baseline/normalized-polls-before.json").read_text())["polls"]
    by_id = {r["poll_id"]: r for r in retained}
    if any(by_id.get(r["poll_id"]) != r for r in baseline):
        raise ValueError("governor acquisition must preserve the original feed rows")
    for row in selected:
        row["acquisition_id"] = RESEARCH.name
    source_selected = selected
    selected = apply_current_revisions(selected, existing)
    rows = sorted(retained + selected, key=lambda r: (r["field_date"], r["poll_id"]))
    election, ledger = replay(rows)
    forecasts = public_forecast_payload(election)
    with tempfile.TemporaryDirectory(prefix="governor-replay-") as directory:
        staged = Path(directory) / "polls.json"
        write_json(staged, {"polls": rows})
        history = public_race_history_payload(feed_path=staged)
    counts = Counter(r["race_id"] for r in selected)
    manifest = {
        "acquisition_id": RESEARCH.name, "office": "governor", "window": decisions["window"],
        "cutoff_basis": "publication_date", "observation_date_basis": "field_end",
        "accepted_count": len(selected), "held_record_count": len(held),
        "counts_by_race": {r.race_id: counts[r.race_id] for r in GOVERNOR_2026_RACES},
        "accepted_poll_ids": [r["poll_id"] for r in selected], "held": held,
        "counts_by_party_basis": dict(Counter(r["crosstab_basis"] for r in selected)),
        "counts_by_precision_method": dict(Counter(r["model_base_method"] for r in selected)),
        "counts_by_pollster": dict(Counter(r["pollster"] for r in selected)),
        "feed_sha256": digest(rows), "acquisition_rows_sha256": digest(source_selected),
        "review_decisions_sha256": digest(decisions), "retained_baseline_rows": len(baseline),
        "inclusion_policy": decisions.get("inclusion_policy"),
        "backfill_policy": decisions.get("backfill_policy"),
        "precision_policy": decisions["precision_policy"], "limitations": decisions["limitations"],
    }
    if not args.check:
        write_json(feed_path, {"polls": rows})
        save_election_model(election, ROOT / "data/models/2026_election_model.json")
        ledger.path = ROOT / "data/ingestion/2026_seen_polls.json"
        ledger.save()
        write_json(ROOT / "docs/data/forecasts.json", forecasts)
        write_json(ROOT / "docs/data/race-history.json", history)
        write_json(RESEARCH / "ingestion-manifest.json", manifest)
    print(json.dumps({"check_only": args.check, "accepted": len(selected), "held": len(held),
                      "counts_by_race": manifest["counts_by_race"]}, indent=2))


if __name__ == "__main__":
    main()
