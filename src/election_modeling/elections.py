"""Containers for modeling many races in an election cycle."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from election_modeling.polls import PollObservation
from election_modeling.races import Electorate, Forecast, RaceModel


@dataclass
class ElectionModel:
    """A keyed collection of race models for Senate, governor, or other races."""

    races: dict[str, RaceModel] = field(default_factory=dict)

    @classmethod
    def from_electorates(
        cls,
        electorates: Mapping[str, Electorate],
        **race_model_kwargs: object,
    ) -> "ElectionModel":
        election = cls()
        for race_id, electorate in electorates.items():
            election.add_race(
                race_id,
                electorate=electorate,
                **race_model_kwargs,
            )
        return election

    def add_race(
        self,
        race_id: str,
        *,
        electorate: Electorate,
        **race_model_kwargs: object,
    ) -> RaceModel:
        if race_id in self.races:
            raise ValueError(f"race already exists: {race_id}")
        model = RaceModel.default(electorate=electorate, **race_model_kwargs)
        self.races[race_id] = model
        return model

    def update(self, race_id: str, observation: PollObservation) -> RaceModel:
        model = self._race(race_id)
        model.update(observation)
        return model

    def forecast(self, race_id: str, *, z_score: float = 1.96) -> Forecast:
        return self._race(race_id).forecast(z_score=z_score)

    def forecast_all(self, *, z_score: float = 1.96) -> dict[str, Forecast]:
        return {
            race_id: model.forecast(z_score=z_score)
            for race_id, model in self.races.items()
        }

    def _race(self, race_id: str) -> RaceModel:
        try:
            return self.races[race_id]
        except KeyError as exc:
            raise KeyError(f"unknown race: {race_id}") from exc
