"""Public forecast export helpers for static pages."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from election_modeling.cycles import RACES_2026_BY_ID, create_2026_election_model
from election_modeling.elections import ElectionModel
from election_modeling.nominees import NOMINEES_2026_BY_RACE, RaceNominees
from election_modeling.persistence import load_election_model


@dataclass(frozen=True)
class PublicExportOptions:
    """Controls how model forecasts are converted into public map states."""

    tossup_uses_moe: bool = True
    tossup_margin_threshold: float = 0.03
    z_score: float = 1.96


def public_forecast_payload(
    election: ElectionModel,
    *,
    options: PublicExportOptions | None = None,
) -> dict[str, object]:
    """Convert an election model into a compact static-site JSON payload."""

    options = options or PublicExportOptions()
    races = []
    for race_id, model in sorted(election.races.items()):
        race = RACES_2026_BY_ID.get(race_id)
        if race is None:
            continue
        nominees = NOMINEES_2026_BY_RACE.get(race_id)
        forecast = model.forecast(z_score=options.z_score)
        leader = _leader_for_margin(forecast.margin)
        tossup = _is_tossup(
            margin=forecast.margin,
            margin_of_error=forecast.margin_of_error,
            options=options,
        )
        status = "tossup" if tossup else leader
        races.append(
            {
                "race_id": race_id,
                "cycle": race.cycle,
                "office": race.office,
                "state": race.state,
                "state_code": race_id[:2].upper(),
                "candidate_a_party": "Republican",
                "candidate_a_name": nominees.republican.name
                if nominees and nominees.republican
                else None,
                "candidate_a_nominee_status": nominees.republican.status
                if nominees and nominees.republican
                else None,
                "candidate_b_party": "Democratic",
                "candidate_b_name": nominees.democratic.name
                if nominees and nominees.democratic
                else None,
                "candidate_b_nominee_status": nominees.democratic.status
                if nominees and nominees.democratic
                else None,
                "candidate_a_share": round(forecast.candidate_a_share, 4),
                "candidate_b_share": round(forecast.candidate_b_share, 4),
                "margin": round(forecast.margin, 4),
                "margin_percent": round(forecast.margin_percent, 2),
                "margin_of_error": round(forecast.margin_of_error, 4),
                "margin_of_error_percent": round(
                    forecast.margin_of_error_percent,
                    2,
                ),
                "leader": leader,
                "status": status,
                "nominee_last_verified": nominees.last_verified if nominees else None,
                "nominee_note": nominees.notes if nominees else None,
                "nominee_sources": _nominee_sources(nominees),
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cycle": 2026,
        "offices": ("senate", "governor"),
        "races": races,
    }


def export_public_forecasts(
    *,
    snapshot_path: str | Path = "data/models/2026_election_model.json",
    output_path: str | Path = "docs/data/forecasts.json",
    options: PublicExportOptions | None = None,
) -> dict[str, object]:
    """Load the current model snapshot and write public map JSON."""

    snapshot = Path(snapshot_path)
    election = load_election_model(snapshot) if snapshot.exists() else create_2026_election_model()
    payload = public_forecast_payload(election, options=options)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n")
    return payload


def _nominee_sources(nominees: RaceNominees | None) -> dict[str, str]:
    if nominees is None:
        return {}

    sources = {}
    if nominees.republican:
        sources["republican"] = nominees.republican.source_url
    if nominees.democratic:
        sources["democratic"] = nominees.democratic.source_url
    return sources


def _leader_for_margin(margin: float) -> str:
    if margin > 0:
        return "republican"
    if margin < 0:
        return "democratic"
    return "tie"


def _is_tossup(
    *,
    margin: float,
    margin_of_error: float,
    options: PublicExportOptions,
) -> bool:
    if options.tossup_uses_moe:
        return abs(margin) <= margin_of_error
    return abs(margin) <= options.tossup_margin_threshold
