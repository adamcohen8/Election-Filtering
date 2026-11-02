"""Built-in election-cycle race registries."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Mapping

from election_modeling.elections import ElectionModel
from election_modeling.races import Electorate

Office = Literal["senate", "governor", "generic_ballot"]


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
    "Alaska": Electorate(republican=0.40, democratic=0.24, independent=0.36),
    "Arizona": Electorate(republican=0.36, democratic=0.29, independent=0.35),
    "Florida": Electorate(republican=0.40, democratic=0.27, independent=0.33),
    "Georgia": Electorate(republican=0.40, democratic=0.36, independent=0.24),
    "Iowa": Electorate(republican=0.38, democratic=0.27, independent=0.35),
    "Kansas": Electorate(republican=0.48, democratic=0.27, independent=0.25),
    "Maine": Electorate(republican=0.31, democratic=0.28, independent=0.41),
    "Michigan": Electorate(republican=0.35, democratic=0.33, independent=0.32),
    "Minnesota": Electorate(republican=0.34, democratic=0.37, independent=0.29),
    # User-selected Nebraska turnout shares.
    "Nebraska": Electorate(republican=0.57, democratic=0.24, independent=0.19),
    "Nevada": Electorate(republican=0.38, democratic=0.34, independent=0.28),
    "New Hampshire": Electorate(republican=0.32, democratic=0.30, independent=0.38),
    "North Carolina": Electorate(republican=0.38, democratic=0.36, independent=0.26),
    "Ohio": Electorate(republican=0.42, democratic=0.30, independent=0.28),
    "Pennsylvania": Electorate(republican=0.38, democratic=0.38, independent=0.24),
    "Texas": Electorate(republican=0.41, democratic=0.28, independent=0.31),
    "United States": Electorate(republican=0.37, democratic=0.33, independent=0.30),
    "Wisconsin": Electorate(republican=0.37, democratic=0.34, independent=0.29),
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
    "Kansas",
    "Minnesota",
    "Nebraska",
)

# Alaska governor is excluded by user request: its GOP has multiple finalists.
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
    "Kansas",
    "Maine",
    "Nevada",
    "Minnesota",
)

GENERIC_BALLOT_2026_RACES: tuple[RaceSpec, ...] = (
    RaceSpec(
        race_id="us_house_generic",
        cycle=2026,
        office="generic_ballot",
        state="United States",
    ),
)

STATE_ABBREVIATIONS: dict[str, str] = {
    "Alaska": "ak",
    "Arizona": "az",
    "Florida": "fl",
    "Georgia": "ga",
    "Iowa": "ia",
    "Kansas": "ks",
    "Maine": "me",
    "Michigan": "mi",
    "Minnesota": "mn",
    "Nebraska": "ne",
    "Nevada": "nv",
    "New Hampshire": "nh",
    "North Carolina": "nc",
    "Ohio": "oh",
    "Pennsylvania": "pa",
    "Texas": "tx",
    "United States": "us",
    "Wisconsin": "wi",
}

OFFICE_CODES: dict[Office, str] = {
    "senate": "sen",
    "governor": "gov",
    "generic_ballot": "house_generic",
}


def race_id_for(state: str, office: Office) -> str:
    try:
        state_code = STATE_ABBREVIATIONS[state]
    except KeyError as exc:
        raise KeyError(f"unknown state: {state}") from exc
    office_code = OFFICE_CODES[office]
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
RACES_2026 = SENATE_2026_RACES + GOVERNOR_2026_RACES + GENERIC_BALLOT_2026_RACES
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
    ensure_2026_races(
        election,
        electorates=electorates,
        default_electorate=default_electorate,
        **race_model_kwargs,
    )
    return election


def ensure_2026_races(
    election: ElectionModel,
    electorates: Mapping[str, Electorate] | None = None,
    *,
    default_electorate: Electorate = DEFAULT_PLACEHOLDER_ELECTORATE,
    **race_model_kwargs: object,
) -> ElectionModel:
    """Add any currently registered 2026 races missing from an election model."""

    electorates = {
        **TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID,
        **(electorates or {}),
    }
    for race in RACES_2026:
        if race.race_id in election.races:
            continue
        election.add_race(
            race.race_id,
            electorate=electorates.get(race.race_id, default_electorate),
            **race_model_kwargs,
        )
    return election
