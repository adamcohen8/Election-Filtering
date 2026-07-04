"""Public forecast export helpers for static pages."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from election_modeling.cycles import RACES_2026_BY_ID, create_2026_election_model
from election_modeling.elections import ElectionModel
from election_modeling.ingestion import NormalizedPoll, RaceClassifier, StructuredJSONSource
from election_modeling.nominees import NOMINEES_2026_BY_RACE, RaceNominees
from election_modeling.persistence import load_election_model
from election_modeling.races import Forecast, RaceModel
from election_modeling.states import PARTY_IDS


@dataclass(frozen=True)
class PublicExportOptions:
    """Controls how model forecasts are converted into public map states."""

    tossup_margin_threshold: float = 0.02
    lean_margin_threshold: float = 0.05
    likely_margin_threshold: float = 0.08
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
        data_available = _has_public_forecast_data(race.office, nominees)
        leader = _leader_for_margin(forecast.margin) if data_available else "tie"
        status = (
            _status_for_margin(margin=forecast.margin, leader=leader, options=options)
            if data_available
            else "tossup"
        )
        races.append(
            {
                "race_id": race_id,
                "cycle": race.cycle,
                "office": race.office,
                "state": race.state,
                "state_code": _state_code_for_race(race_id),
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
                "data_available": data_available,
                "data_note": None if data_available else "No data available",
                "candidate_a_share": round(forecast.candidate_a_share, 4)
                if data_available
                else None,
                "candidate_b_share": round(forecast.candidate_b_share, 4)
                if data_available
                else None,
                "margin": round(forecast.margin, 4) if data_available else None,
                "margin_percent": round(forecast.margin_percent, 2) if data_available else None,
                "margin_of_error": round(forecast.margin_of_error, 4)
                if data_available
                else None,
                "margin_of_error_percent": round(
                    forecast.margin_of_error_percent,
                    2,
                )
                if data_available
                else None,
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
        "offices": ("senate", "governor", "generic_ballot"),
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


def public_race_history_payload(
    *,
    feed_path: str | Path = "data/ingestion/2026_normalized_polls.json",
    options: PublicExportOptions | None = None,
) -> dict[str, object]:
    """Replay normalized polls into per-race history for static race pages."""

    options = options or PublicExportOptions()
    feed = Path(feed_path)
    election = create_2026_election_model()
    classifier = RaceClassifier(RACES_2026_BY_ID)
    histories: dict[str, dict[str, object]] = {
        race_id: {
            "race_id": race_id,
            "model_points": [],
            "poll_points": [],
        }
        for race_id in RACES_2026_BY_ID
    }

    if not feed.exists():
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "cycle": 2026,
            "races": list(histories.values()),
        }

    poll_pairs = []
    for poll in StructuredJSONSource(str(feed)).fetch():
        race_id = classifier.classify(poll)
        if race_id is None or race_id not in election.races:
            continue
        poll_pairs.append((poll, race_id))

    initialized_races: set[str] = set()
    for poll, race_id in sorted(poll_pairs, key=lambda item: (item[0].field_date, item[0].poll_id)):
        model = election.races[race_id]
        history = histories[race_id]
        if race_id not in initialized_races:
            history["model_points"].append(
                _public_history_point(
                    date=poll.field_date,
                    forecast=model.forecast(z_score=options.z_score),
                )
            )
            initialized_races.add(race_id)

        poll_point = _public_poll_point(poll, model=model)
        if poll_point is not None:
            history["poll_points"].append(poll_point)

        _apply_poll_to_model(poll, model)
        history["model_points"].append(
            _public_history_point(
                date=poll.field_date,
                forecast=model.forecast(z_score=options.z_score),
            )
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cycle": 2026,
        "races": [histories[race_id] for race_id in sorted(histories)],
    }


def export_public_race_history(
    *,
    feed_path: str | Path = "data/ingestion/2026_normalized_polls.json",
    output_path: str | Path = "docs/data/race-history.json",
    options: PublicExportOptions | None = None,
) -> dict[str, object]:
    """Write public per-race model and poll history JSON."""

    payload = public_race_history_payload(feed_path=feed_path, options=options)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n")
    return payload


def _has_public_forecast_data(office: str, nominees: RaceNominees | None) -> bool:
    if office == "generic_ballot":
        return True
    return bool(nominees and nominees.republican and nominees.democratic)


def _apply_poll_to_model(poll: NormalizedPoll, model: RaceModel) -> None:
    if poll.crosstab is not None:
        model.update(
            poll.crosstab.to_observation(
                pollster=poll.pollster,
                field_date=poll.field_date,
            )
        )
        return
    if poll.topline is not None:
        model.update_topline(
            candidate_a_share=poll.topline.candidate_a_share,
            candidate_b_share=poll.topline.candidate_b_share,
            sample_size=poll.topline.sample_size,
            pollster=poll.pollster,
            field_date=poll.field_date,
        )


def _public_history_point(*, date: str, forecast: Forecast) -> dict[str, object]:
    return {
        "date": date,
        "candidate_a_share": round(forecast.candidate_a_share, 4),
        "candidate_b_share": round(forecast.candidate_b_share, 4),
        "margin": round(forecast.margin, 4),
        "margin_percent": round(forecast.margin_percent, 2),
    }


def _public_poll_point(poll: NormalizedPoll, *, model: RaceModel) -> dict[str, object] | None:
    if poll.topline is not None:
        candidate_a_share = poll.topline.candidate_a_share
        candidate_b_share = poll.topline.candidate_b_share
        sample_size = poll.topline.sample_size
        measurement = "topline"
        partial_party_id = False
    elif poll.crosstab is not None:
        weighted = _weighted_crosstab_result(poll=poll, model=model)
        if weighted is None:
            return None
        candidate_a_share, candidate_b_share, sample_size, partial_party_id = weighted
        measurement = "party_id_crosstab"
    else:
        return None

    margin = candidate_a_share - candidate_b_share
    return {
        "poll_id": poll.poll_id,
        "pollster": poll.pollster,
        "date": poll.field_date,
        "candidate_a_share": round(candidate_a_share, 4),
        "candidate_b_share": round(candidate_b_share, 4),
        "margin": round(margin, 4),
        "margin_percent": round(margin * 100.0, 2),
        "leader": _leader_for_margin(margin),
        "sample_size": sample_size,
        "measurement": measurement,
        "partial_party_id": partial_party_id,
        "source_url": poll.source_url,
    }


def _weighted_crosstab_result(
    *,
    poll: NormalizedPoll,
    model: RaceModel,
) -> tuple[float, float, int, bool] | None:
    if poll.crosstab is None:
        return None

    candidate_a_share = 0.0
    candidate_b_share = 0.0
    total_weight = 0.0
    total_sample = 0
    for party_id in PARTY_IDS:
        if party_id not in poll.crosstab.values:
            continue
        weight = getattr(model.electorate, party_id)
        candidate_a, candidate_b = poll.crosstab.values[party_id]
        candidate_a_share += weight * candidate_a
        candidate_b_share += weight * candidate_b
        total_weight += weight
        total_sample += poll.crosstab.subgroup_sample_sizes.get(party_id, 0)

    if total_weight <= 0:
        return None

    return (
        candidate_a_share / total_weight,
        candidate_b_share / total_weight,
        total_sample,
        total_weight < 0.999,
    )


def _nominee_sources(nominees: RaceNominees | None) -> dict[str, str]:
    if nominees is None:
        return {}

    sources = {}
    if nominees.republican:
        sources["republican"] = nominees.republican.source_url
    if nominees.democratic:
        sources["democratic"] = nominees.democratic.source_url
    return sources


def _state_code_for_race(race_id: str) -> str | None:
    if race_id == "us_house_generic":
        return "US"
    return race_id[:2].upper()


def _leader_for_margin(margin: float) -> str:
    if margin > 0:
        return "republican"
    if margin < 0:
        return "democratic"
    return "tie"


def _status_for_margin(
    *,
    margin: float,
    leader: str,
    options: PublicExportOptions,
) -> str:
    lead = abs(margin)
    if leader == "tie" or lead < options.tossup_margin_threshold:
        return "tossup"
    if lead < options.lean_margin_threshold:
        return f"lean-{leader}"
    if lead < options.likely_margin_threshold:
        return f"likely-{leader}"
    return f"safe-{leader}"
