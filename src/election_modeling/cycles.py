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

SENATE_2026_STATES: tuple[str, ...] = (
    "Florida",
    "Texas",
    "Georgia",
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


def create_2026_election_model(
    electorates: Mapping[str, Electorate] | None = None,
    *,
    default_electorate: Electorate = DEFAULT_PLACEHOLDER_ELECTORATE,
    **race_model_kwargs: object,
) -> ElectionModel:
    """Create an election model preloaded with the initial 2026 race list.

    ``electorates`` is keyed by race ID, for example ``"fl_sen"`` or
    ``"pa_gov"``. Races without a supplied electorate use
    ``default_electorate``; the package default is an intentionally neutral
    placeholder so the model can be built before real electorate forecasts land.
    """

    electorates = electorates or {}
    election = ElectionModel()
    for race in RACES_2026:
        election.add_race(
            race.race_id,
            electorate=electorates.get(race.race_id, default_electorate),
            **race_model_kwargs,
        )
    return election
