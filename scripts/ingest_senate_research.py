"""Validate reviewed primary-source research and replay the local poll feed.

No network access. Research originals and review decisions remain separate from
the normalized feed. Run after every Senate race has a completed REPORT.md.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from election_modeling.cycles import SENATE_2026_RACES, create_2026_election_model
from election_modeling.ingestion import (
    IngestionLedger, NormalizedPoll, PollIngestionPipeline, StaticPollSource,
    canonical_poll, measurement_key,
)
from election_modeling.persistence import save_election_model
from election_modeling.public import public_forecast_payload, public_race_history_payload

PARTIES = ("republican", "democratic", "independent")
DEFAULT_RESEARCH = ROOT / "research" / "senate_polls_20261101"
# This acquisition predates the separately researched Nebraska addition.
INITIAL_SENATE_RACE_IDS = {
    "fl_sen", "tx_sen", "ga_sen", "me_sen", "nh_sen", "ia_sen",
    "ak_sen", "mi_sen", "oh_sen", "nc_sen", "ks_sen", "mn_sen",
}


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def normalize_reviewed_row(raw: dict, review: dict, *, source_path: str,
                           start: str, end: str, backfill_allowed: bool = False,
                           expected_office: str = "senate") -> dict:
    """Produce a model row without disguising estimates as respondent counts."""
    row = {**raw, **review.get("overrides", {})}
    publication = row.get("publication_date")
    if publication is None:
        bounds = review.get("publication_date_bounds")
        if not bounds or len(bounds) != 2:
            raise ValueError("publication date not established inside the window")
        lower, upper = (date.fromisoformat(value).isoformat() for value in bounds)
        in_window = start <= lower <= upper <= end
        older_backfill = (lower <= upper < start and backfill_allowed
                          and review.get("backfill_authorized") is True)
        if not (in_window or older_backfill):
            raise ValueError("publication date not established inside the window")
        if older_backfill:
            row["backfill_original_cutoff"] = start
        row["publication_date_bounds"] = bounds
    elif not start <= date.fromisoformat(publication).isoformat() <= end:
        if publication < start and backfill_allowed and review.get("backfill_authorized") is True:
            row["backfill_original_cutoff"] = start
        else:
            raise ValueError("publication date outside requested window")
    field_end = date.fromisoformat(row["field_date"]).isoformat()
    if row.get("field_start") and date.fromisoformat(row["field_start"]) > date.fromisoformat(field_end):
        raise ValueError("fieldwork begins after it ends")
    if field_end > (publication or row["publication_date_bounds"][1]):
        raise ValueError("publication precedes end of fieldwork")
    basis = row.get("crosstab_basis")
    ordinary_basis = basis in {"party_id", "party_registration"}
    authorized_proxy = review.get("allow_proxy") is True and basis in {"modeled_party_id", "party_basis_unspecified", "modeled_subgroup_estimate"}
    if row.get("office") != expected_office or not (ordinary_basis or authorized_proxy):
        raise ValueError(f"only actual party-ID/registration {expected_office.title()} crosstabs are eligible")
    if not row.get("source_url") or not row.get("source_location") or not row.get("evidence_excerpt"):
        raise ValueError("primary source, table location and evidence are required")

    method = row.get("subgroup_n_method")
    original_bases = {party: row.get(f"{party}_n") for party in PARTIES}
    precision = review.get("precision", {})
    mode = precision.get("method", method)
    if mode == "assumed_covariance":
        # Unknown respondent counts stay unknown. This is a directly specified
        # Gaussian measurement error, not a synthetic or implied sample size.
        sd = precision.get("cell_sd")
        correlation = precision.get("within_group_correlation", -0.5)
        if (isinstance(sd, bool) or not isinstance(sd, (int, float)) or not math.isfinite(sd)
                or not 0 < sd <= 1 or not -1 < correlation < 1 or not precision.get("evidence")):
            raise ValueError("assumed covariance needs an explicit positive cell SD and evidence")
        covariance = [[0.0] * 6 for _ in range(6)]
        for i in range(6):
            covariance[i][i] = sd * sd
            covariance[i][i ^ 1] = correlation * sd * sd
        row["crosstab_covariance"] = covariance
        bases = original_bases
        default_deff = 1.0
    elif mode == "suppression_lower_bound":
        minimum = precision.get("minimum_n")
        if isinstance(minimum, bool) or not isinstance(minimum, int) or minimum < 1 or not precision.get("evidence"):
            raise ValueError("a sourced subgroup suppression threshold is required")
        bases = {party: minimum for party in PARTIES}
        default_deff = 3.0
    elif mode == "reported_effective":
        bases = row.get("effective_subgroup_n")
        if not bases or not precision.get("evidence"):
            raise ValueError("reported effective bases and evidence are required")
        default_deff = 1.0
    elif mode == "derived_total_x_share":
        total, composition = row.get("reported_total_n"), row.get("reported_party_composition")
        if not isinstance(total, (int, float)) or total <= 0 or not composition:
            raise ValueError("matching population total and composition are required")
        bases = {party: math.floor(total * composition[party] + 1e-10) for party in PARTIES}
        default_deff = 3.0
    elif mode in {"reported_unweighted", "reported_weighted", "reported_count_weighting_unspecified", "reported_n_weighting_unspecified", "reported_weighting_unspecified"}:
        bases = original_bases
        default_deff = 1.5 if mode == "reported_unweighted" else 2.0
    else:
        raise ValueError(f"unsupported or missing subgroup denominator: {mode}")

    row["source_support_values"] = {f"{p}_{c}": raw.get(f"{p}_{c}") for p in PARTIES for c in ("a", "b")}
    row["source_candidate_names"] = {"candidate_a": raw.get("candidate_a"), "candidate_b": raw.get("candidate_b")}
    approximations = {}
    for cell, interval in review.get("interval_midpoints", {}).items():
        if mode != "assumed_covariance" or cell not in row["source_support_values"] or raw.get(cell) is not None:
            raise ValueError("interval approximation needs a censored source cell and explicit covariance")
        source = raw.get(cell + "_censored", {})
        lower, upper = interval["lower"], interval["upper"]
        if source.get("lower_exclusive") != lower or source.get("upper_exclusive") != upper or not 0 <= lower < upper <= 1:
            raise ValueError("approximation must match the published interval")
        midpoint = (lower + upper) / 2
        row[cell] = midpoint
        index = [f"{p}_{c}" for p in PARTIES for c in ("a", "b")].index(cell)
        extra = ((upper - lower) / 2) ** 2
        row["crosstab_covariance"][index][index] += extra
        approximations[cell] = {"source_interval": [lower, upper], "model_midpoint": midpoint,
                                "additional_variance": extra}
    if approximations:
        row["support_approximations"] = approximations

    for party in PARTIES:
        n = bases[party]
        if n is None and mode == "assumed_covariance":
            row[f"{party}_n"] = None
        elif isinstance(n, bool) or not isinstance(n, (int, float)) or not math.isfinite(n) or n < 1:
            raise ValueError(f"invalid {party} base")
        else:
            row[f"{party}_n"] = math.floor(n)
        a, b = row.get(f"{party}_a"), row.get(f"{party}_b")
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in (a, b)):
            raise ValueError(f"missing or censored {party} support")
        if a < 0 or b < 0 or a + b > 1:
            raise ValueError(f"invalid {party} support pair")
    row["source_subgroup_bases"] = original_bases
    row["source_crosstab_basis"] = raw.get("crosstab_basis")
    row["source_subgroup_n_method"] = method
    row["subgroup_n_method"] = mode
    row["model_base_method"] = mode
    row["model_base_rounding"] = "floor" if mode != "assumed_covariance" else None
    row["precision_review"] = precision
    row["design_effect"] = precision.get("design_effect", default_deff)
    if not math.isfinite(row["design_effect"]) or row["design_effect"] < 1:
        raise ValueError("design effect must be finite and at least one")
    row["research_poll_id"] = row["poll_id"]
    row["poll_id"] = f'{row["race_id"]}--{row["poll_id"]}'
    row["sample_id"] = f'{row["race_id"]}--{row.get("sample_id") or row["research_poll_id"]}'
    row["research_source_path"] = source_path
    row["research_record_sha256"] = digest(raw)
    candidates = [ROOT / row["evidence_path"]] if row.get("evidence_path") else []
    archived_pdf = DEFAULT_RESEARCH / "verification/sources" / f'{row["race_id"]}--{row["research_poll_id"]}.pdf'
    if archived_pdf.exists():
        candidates.append(archived_pdf)
    row["evidence_artifacts"] = [
        {"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        for path in dict.fromkeys(candidates) if path.is_file()
    ]
    row["review_reason"] = review["reason"]
    row["proxy_inclusion_authorized"] = bool(authorized_proxy)
    row["ingestion_status"] = "accepted"
    return row


def validate_backfill_selection(accepted: list[dict], policy: dict) -> None:
    """Keep the prior acquisition intact and cap only authorized older additions."""
    baseline = policy["baseline_source_hashes"]
    by_id = {row["poll_id"]: row for row in accepted}
    if not baseline.keys() <= by_id.keys():
        raise ValueError("backfill must preserve every baseline poll")
    for poll_id, source_hash in baseline.items():
        if by_id[poll_id]["research_record_sha256"] != source_hash:
            raise ValueError("backfill changed a baseline research record")
    target = policy["target_count"]
    counts = Counter(row["race_id"] for row in accepted)
    for row in accepted:
        if row["poll_id"] not in baseline:
            race = row["race_id"]
            if race not in policy["target_races"] or not row.get("backfill_original_cutoff"):
                raise ValueError("new poll is not an authorized older backfill")
            if policy["baseline_counts"][race] >= target or counts[race] > target:
                raise ValueError("backfill exceeds the race's target count")


def compile_research(research_root: Path, decisions: dict, *, race_specs=None,
                     expected_office: str = "senate") -> tuple[list[dict], list[dict]]:
    race_specs = (tuple(r for r in SENATE_2026_RACES if r.race_id in INITIAL_SENATE_RACE_IDS)
                  if race_specs is None else race_specs)
    start, end = decisions["window"]["start"], decisions["window"]["end"]
    date.fromisoformat(start)
    date.fromisoformat(end)
    reviews = decisions["decisions"]
    accepted, held, keys = [], [], set()
    sources = []
    for race in race_specs:
        directory = research_root / race.race_id
        if not (directory / "REPORT.md").is_file():
            raise ValueError(f"research incomplete: {race.race_id}")
        path = directory / "polls.json"
        payload = json.loads(path.read_text())
        if payload["race_id"] != race.race_id:
            raise ValueError(f"wrong race in {path}")
        sources.append((path, payload["polls"]))
    known_races = {race.race_id: race for race in race_specs}
    for relative in decisions.get("supplement_files", []):
        path = (research_root / relative).resolve()
        if not path.is_relative_to(research_root.resolve()) or not (path.parent / "REPORT.md").is_file():
            raise ValueError(f"invalid or incomplete supplement: {relative}")
        sources.append((path, json.loads(path.read_text())["polls"]))
    for path, rows in sources:
        for raw in rows:
            race = known_races.get(raw["race_id"])
            key = f'{raw["race_id"]}/{raw["poll_id"]}'
            if key in keys or race is None or raw["state"] != race.state:
                raise ValueError(f"duplicate or mismatched research record: {key}")
            keys.add(key)
            review = reviews.get(key)
            if not review or not review.get("reason"):
                raise ValueError(f"explicit review missing: {key}")
            if review.get("record_sha256") != digest(raw):
                raise ValueError(f"research changed after review: {key}")
            if review["action"] == "hold":
                held.append({"key": key, "reason": review["reason"], "source_url": raw.get("source_url")})
                continue
            if review["action"] != "accept":
                raise ValueError(f"invalid review action: {key}")
            try:
                policy = decisions.get("backfill_policy", {})
                accepted.append(normalize_reviewed_row(raw, review, source_path=str(path.relative_to(ROOT)), start=start, end=end,
                    backfill_allowed=raw["race_id"] in policy.get("target_races", {}), expected_office=expected_office))
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"{key}: {exc}") from exc
    if set(reviews) != keys:
        raise ValueError(f"stale review keys: {set(reviews) - keys}")
    accepted.sort(key=lambda row: (row["field_date"], row["poll_id"]))
    # One population/question/party-basis version per survey and race.
    samples = [(row["race_id"], row["sample_id"]) for row in accepted]
    if len(set(samples)) != len(samples):
        raise ValueError("multiple versions of the same survey selected")
    if decisions.get("backfill_policy"):
        validate_backfill_selection(accepted, decisions["backfill_policy"])
    return accepted, held


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")
    temp.replace(path)


def replay(rows: list[dict]):
    polls = []
    for row in rows:
        try:
            polls.append(canonical_poll(NormalizedPoll.from_mapping(row), row["race_id"]))
        except (ValueError, TypeError, KeyError) as exc:
            raise ValueError(f'{row.get("poll_id")}: {exc}') from exc
    if len({p.poll_id for p in polls}) != len(polls):
        raise ValueError("duplicate IDs in merged feed")
    if len({measurement_key(p, p.race_id) for p in polls}) != len(polls):
        raise ValueError("duplicate measurements in merged feed")
    election = create_2026_election_model()
    ledger = IngestionLedger()
    result = PollIngestionPipeline(sources=(StaticPollSource(polls),), ledger=ledger).run(election)
    if result.errors or result.unknown_race_ids or result.unclassified_poll_ids or len(result.applied) != len(polls):
        raise ValueError(f"replay failed: {result}")
    return election, ledger


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate and replay without publishing files")
    args = parser.parse_args()
    research_root = DEFAULT_RESEARCH
    decisions = json.loads((research_root / "review-decisions.json").read_text())
    selected, held = compile_research(research_root, decisions)
    feed_path = ROOT / "data/ingestion/2026_normalized_polls.json"
    existing = json.loads(feed_path.read_text())["polls"] if feed_path.exists() else []
    # Replace only this acquisition's rows. Preserve any unrelated input data.
    retained = [row for row in existing if row.get("acquisition_id") != research_root.name]
    for row in selected:
        row["acquisition_id"] = research_root.name
    rows = sorted(retained + selected, key=lambda row: (row["field_date"], row["poll_id"]))
    election, ledger = replay(rows)
    forecasts = public_forecast_payload(election)
    with tempfile.TemporaryDirectory(prefix="senate-replay-") as directory:
        staged_feed = Path(directory) / "polls.json"
        write_json(staged_feed, {"polls": rows})
        history = public_race_history_payload(feed_path=staged_feed)
    counts = Counter(row["race_id"] for row in selected)
    manifest = {
        "window": decisions["window"], "cutoff_basis": "publication_date",
        "observation_date_basis": "field_end", "acquisition_id": research_root.name,
        "accepted_count": len(selected), "held_record_count": len(held),
        "counts_by_race": {race.race_id: counts[race.race_id] for race in SENATE_2026_RACES},
        "accepted_poll_ids": [row["poll_id"] for row in selected], "held": held,
        "counts_by_pollster": dict(sorted(Counter(row["pollster"] for row in selected).items())),
        "counts_by_party_basis": dict(sorted(Counter(row["crosstab_basis"] for row in selected).items())),
        "counts_by_precision_method": dict(sorted(Counter(row["model_base_method"] for row in selected).items())),
        "inclusion_policy": decisions.get("inclusion_policy"),
        "backfill_policy": decisions.get("backfill_policy"),
        "precision_policy": decisions["precision_policy"],
        "limitations": decisions["limitations"],
        "feed_sha256": digest(rows), "review_decisions_sha256": digest(decisions),
    }
    if not args.check:
        # No live model/ledger mutation occurs until the complete replay succeeds.
        write_json(feed_path, {"polls": rows})
        save_election_model(election, ROOT / "data/models/2026_election_model.json")
        ledger.path = ROOT / "data/ingestion/2026_seen_polls.json"
        ledger.save()
        write_json(ROOT / "docs/data/forecasts.json", forecasts)
        write_json(ROOT / "docs/data/race-history.json", history)
        write_json(research_root / "ingestion-manifest.json", manifest)
    print(json.dumps({"check_only": args.check, "accepted": len(selected), "held": len(held), "counts_by_race": manifest["counts_by_race"]}, indent=2))


if __name__ == "__main__":
    main()
