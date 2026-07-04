"""Built-in election-cycle race registries."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Mapping

from election_modeling.elections import ElectionModel
from election_modeling.races import Electorate

Office = Literal["senate", "governor"]


@dataclass(frozen=True)
class RaceSpec:
    """Metadata for a modeled race."""

    race_id: str
    cycle: int
    office: Office
    state: str


DEFAULT_PLACEHOLDER_ELECTORATE = Electorate(
    republican=1.0 / 3.0,
    democratic=1.0 / 3.0,
    independent=1.0 / 3.0,
)

TURNOUT_2024_PREDICTION_ELECTORATES_BY_STATE: dict[str, Electorate] = {
    "Arizona": Electorate(republican=0.34, democratic=0.27, independent=0.39),
    "Florida": Electorate(republican=0.42, democratic=0.28, independent=0.30),
    "Georgia": Electorate(republican=0.41, democratic=0.36, independent=0.23),
    "Iowa": Electorate(
        republican=36.0 / 101.0,
        democratic=26.0 / 101.0,
        independent=39.0 / 101.0,
    ),
    "Michigan": Electorate(republican=0.34, democratic=0.35, independent=0.31),
    "New Hampshire": Electorate(republican=0.29, democratic=0.28, independent=0.43),
    "North Carolina": Electorate(republican=0.37, democratic=0.32, independent=0.31),
    "Ohio": Electorate(republican=0.41, democratic=0.30, independent=0.29),
    "Pennsylvania": Electorate(republican=0.40, democratic=0.37, independent=0.23),
    "Texas": Electorate(republican=0.41, democratic=0.30, independent=0.29),
    "Wisconsin": Electorate(republican=0.37, democratic=0.33, independent=0.30),
}

SENATE_2026_STATES: tuple[str, ...] = (
    "Florida",
    "Texas",
    "Georgia",
    "Maine",
    "New Hampshire",
    "Iowa",
    "Alaska",
    "Michigan",
    "Ohio",
    "North Carolina",
)

GOVERNOR_2026_STATES: tuple[str, ...] = (
    "Florida",
    "Georgia",
    "Texas",
    "New Hampshire",
    "Iowa",
    "Pennsylvania",
    "Arizona",
    "Ohio",
    "Michigan",
    "Wisconsin",
)

STATE_ABBREVIATIONS: dict[str, str] = {
    "Alaska": "ak",
    "Arizona": "az",
    "Florida": "fl",
    "Georgia": "ga",
    "Iowa": "ia",
    "Maine": "me",
    "Michigan": "mi",
    "New Hampshire": "nh",
    "North Carolina": "nc",
    "Ohio": "oh",
    "Pennsylvania": "pa",
    "Texas": "tx",
    "Wisconsin": "wi",
}


def race_id_for(state: str, office: Office) -> str:
    try:
        state_code = STATE_ABBREVIATIONS[state]
    except KeyError as exc:
        raise KeyError(f"unknown state: {state}") from exc
    office_code = "sen" if office == "senate" else "gov"
    return f"{state_code}_{office_code}"


def _race_specs(states: tuple[str, ...], office: Office) -> tuple[RaceSpec, ...]:
    return tuple(
        RaceSpec(
            race_id=race_id_for(state, office),
            cycle=2026,
            office=office,
            state=state,
        )
        for state in states
    )


SENATE_2026_RACES = _race_specs(SENATE_2026_STATES, "senate")
GOVERNOR_2026_RACES = _race_specs(GOVERNOR_2026_STATES, "governor")
RACES_2026 = SENATE_2026_RACES + GOVERNOR_2026_RACES
RACES_2026_BY_ID = {race.race_id: race for race in RACES_2026}
TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID: dict[str, Electorate] = {
    race.race_id: electorate
    for race in RACES_2026
    if (
        electorate := TURNOUT_2024_PREDICTION_ELECTORATES_BY_STATE.get(race.state)
    )
    is not None
}


def create_2026_election_model(
    electorates: Mapping[str, Electorate] | None = None,
    *,
    default_electorate: Electorate = DEFAULT_PLACEHOLDER_ELECTORATE,
    **race_model_kwargs: object,
) -> ElectionModel:
    """Create an election model preloaded with the initial 2026 race list.

    ``electorates`` is keyed by race ID, for example ``"fl_sen"`` or
    ``"pa_gov"``. Supplied electorates override the built-in 2024 prediction
    turnout weights. Races without a supplied or built-in electorate use
    ``default_electorate``.
    """

    electorates = {
        **TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID,
        **(electorates or {}),
    }
    election = ElectionModel()
    for race in RACES_2026:
        election.add_race(
            race.race_id,
            electorate=electorates.get(race.race_id, default_electorate),
            **race_model_kwargs,
        )
    return election
