"""Public forecast export helpers for static pages."""

from __future__ import annotations

import json
from math import fsum
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from election_modeling.cycles import RACES_2026_BY_ID, create_2026_election_model
from election_modeling.elections import ElectionModel
from election_modeling.ingestion import (NormalizedPoll, RaceClassifier, StructuredJSONSource,
                                        apply_poll, canonical_poll, measurement_key, _is_blocked_pollster)
from election_modeling.nominees import NOMINEES_2026_BY_RACE, RaceNominees
from election_modeling.persistence import load_election_model
from election_modeling.races import Forecast, RaceModel
from election_modeling.states import PARTY_IDS


@dataclass(frozen=True)
class PublicExportOptions:
    """Controls how model forecasts are converted into public map states."""

    tossup_margin_threshold: float = 0.005
    tilt_margin_threshold: float = 0.02
    lean_margin_threshold: float = 0.05
    likely_margin_threshold: float = 0.08
    z_score: float = 1.96
    forecast_date: str = "2026-11-03"


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
        data_available = _has_public_forecast_data(model, nominees)
        forecast = model.forecast(z_score=options.z_score,
                                  target_date=options.forecast_date if data_available else None)
        opponent = nominees.candidate_b if nominees else None
        leader = _leader_for_margin(forecast.margin, opponent.party if opponent else "democratic") if data_available else "unknown"
        status = (
            _status_for_margin(margin=forecast.margin, leader=leader, options=options)
            if data_available
            else "unrated"
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
                "candidate_b_party": opponent.party.title() if opponent else "Democratic",
                "candidate_b_name": opponent.name
                if opponent
                else None,
                "candidate_b_nominee_status": opponent.status
                if opponent
                else None,
                "data_available": data_available,
                "data_note": None if data_available else "Prior only: no dated polling observations",
                "estimate_type": "election_day" if data_available else "prior_only",
                "observation_count": model.observation_count,
                "state_date": model.last_date,
                "forecast_date": options.forecast_date,
                "margin_uncertainty_sd_points": {
                    "polling": 100 * forecast.polling_variance**0.5,
                    "movement": 100 * forecast.movement_variance**0.5,
                    "turnout": 100 * forecast.turnout_variance**0.5,
                } if data_available else None,
                "turnout_share_sd_points": 100 * model.electorate.share_standard_deviation,
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
            "rolling_average_window": 7,
            "rolling_average_points": [],
            "rolling_average": None,
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

    seen_ids: set[str] = set()
    seen_measurements: set[str] = set()
    for poll, race_id in sorted(poll_pairs, key=lambda item: (item[0].field_date, item[0].poll_id)):
        if _is_blocked_pollster(poll.pollster):
            continue
        poll = canonical_poll(poll, race_id)
        key = measurement_key(poll, race_id)
        if poll.poll_id in seen_ids or key in seen_measurements:
            continue
        model = election.races[race_id]
        history = histories[race_id]
        poll_point = _public_poll_point(poll, model=model)
        if poll_point is not None:
            history["poll_points"].append(poll_point)

        _apply_poll_to_model(poll, model)
        seen_ids.add(poll.poll_id)
        seen_measurements.add(key)
        _append_daily_model_point(
            history,
            _public_history_point(
                date=poll.field_date,
                forecast=model.forecast(z_score=options.z_score),
            ),
        )

    for history in histories.values():
        points = _rolling_average_points(history["poll_points"])
        history["rolling_average_points"] = points
        history["rolling_average"] = points[-1] if points else None

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cycle": 2026,
        "races": [histories[race_id] for race_id in sorted(histories)],
    }


def _rolling_average_points(poll_points: list[dict[str, object]]) -> list[dict[str, object]]:
    """Equal-weight trailing seven polls, after canonicalization and deduplication.

    Count surveys rather than days; retain the last window of each day for the
    chart. Early windows use all available polls. The poll markers already use
    the race's electorate weights for crosstabs (or the reported topline).
    """
    points = []
    for index, poll in enumerate(poll_points):
        window = poll_points[max(0, index - 6):index + 1]
        candidate_a = fsum(p["candidate_a_share"] for p in window) / len(window)
        candidate_b = fsum(p["candidate_b_share"] for p in window) / len(window)
        margin = candidate_a - candidate_b
        point = {
            "date": poll["date"],
            "window_start_date": window[0]["date"],
            "poll_count": len(window),
            "poll_ids": [p["poll_id"] for p in window],
            "candidate_a_share": round(candidate_a, 4),
            "candidate_b_share": round(candidate_b, 4),
            "margin": round(margin, 4),
            "margin_percent": round(margin * 100, 2),
        }
        if points and points[-1]["date"] == point["date"]:
            points[-1] = point
        else:
            points.append(point)
    return points


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


def _has_public_forecast_data(model: RaceModel, nominees: RaceNominees | None) -> bool:
    return bool(model.observation_count > 0 and model.last_date is not None
                and nominees and nominees.republican and nominees.candidate_b)


def _apply_poll_to_model(poll: NormalizedPoll, model: RaceModel) -> None:
    apply_poll(poll, model)


def _public_history_point(*, date: str, forecast: Forecast) -> dict[str, object]:
    return {
        "date": date,
        "candidate_a_share": round(forecast.candidate_a_share, 4),
        "candidate_b_share": round(forecast.candidate_b_share, 4),
        "margin": round(forecast.margin, 4),
        "margin_percent": round(forecast.margin_percent, 2),
    }


def _append_daily_model_point(history: dict[str, object], point: dict[str, object]) -> None:
    """Keep the public model line to one end-of-day point per date."""

    model_points = history["model_points"]
    if not isinstance(model_points, list):
        raise TypeError("history model_points must be a list")
    if model_points and model_points[-1].get("date") == point["date"]:
        model_points[-1] = point
        return
    model_points.append(point)


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
        "party_basis": poll.crosstab_basis,
        "precision_method": poll.precision_method,
        "partial_party_id": partial_party_id,
        "source_url": poll.source_url,
    }


def _weighted_crosstab_result(
    *,
    poll: NormalizedPoll,
    model: RaceModel,
) -> tuple[float, float, int | None, bool] | None:
    if poll.crosstab is None:
        return None

    candidate_a_share = 0.0
    candidate_b_share = 0.0
    total_weight = 0.0
    total_sample = 0
    complete_sample_sizes = True
    for party_id in PARTY_IDS:
        if party_id not in poll.crosstab.values:
            continue
        weight = getattr(model.electorate, party_id)
        candidate_a, candidate_b = poll.crosstab.values[party_id]
        candidate_a_share += weight * candidate_a
        candidate_b_share += weight * candidate_b
        total_weight += weight
        if party_id in poll.crosstab.subgroup_sample_sizes:
            total_sample += poll.crosstab.subgroup_sample_sizes[party_id]
        else:
            complete_sample_sizes = False

    if total_weight <= 0:
        return None

    return (
        candidate_a_share / total_weight,
        candidate_b_share / total_weight,
        total_sample if complete_sample_sizes else None,
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
    if nominees.independent:
        sources["independent"] = nominees.independent.source_url
    return sources


def _state_code_for_race(race_id: str) -> str | None:
    if race_id == "us_house_generic":
        return "US"
    return race_id[:2].upper()


def _leader_for_margin(margin: float, opponent_party: str = "democratic") -> str:
    if margin > 0:
        return "republican"
    if margin < 0:
        return opponent_party
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
    if lead < options.tilt_margin_threshold:
        return f"tilt-{leader}"
    if lead < options.lean_margin_threshold:
        return f"lean-{leader}"
    if lead < options.likely_margin_threshold:
        return f"likely-{leader}"
    return f"safe-{leader}"
