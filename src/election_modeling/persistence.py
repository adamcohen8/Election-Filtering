"""Persist and restore election model state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping

import numpy as np

from election_modeling.cycles import create_2026_election_model
from election_modeling.elections import ElectionModel
from election_modeling.filters import KalmanState, RaceKalmanFilter
from election_modeling.races import Electorate, RaceModel


def save_election_model(election: ElectionModel, path: str | Path) -> None:
    snapshot_path = Path(path)
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(_election_to_dict(election), indent=2) + "\n")


def load_election_model(path: str | Path) -> ElectionModel:
    payload = json.loads(Path(path).read_text())
    election = ElectionModel()
    for race_id, race_payload in payload["races"].items():
        electorate_payload = race_payload["electorate"]
        electorate = Electorate(
            republican=electorate_payload["republican"],
            democratic=electorate_payload["democratic"],
            independent=electorate_payload["independent"],
        )
        state_payload = race_payload["state"]
        state = KalmanState(
            mean=np.asarray(state_payload["mean"], dtype=float),
            covariance=np.asarray(state_payload["covariance"], dtype=float),
        )
        election.races[race_id] = RaceModel(
            filter_=RaceKalmanFilter(state),
            electorate=electorate,
        )
    return election


def load_or_create_2026_election_model(
    path: str | Path,
    *,
    electorates: Mapping[str, Electorate] | None = None,
) -> ElectionModel:
    snapshot_path = Path(path)
    if snapshot_path.exists():
        return load_election_model(snapshot_path)
    return create_2026_election_model(electorates=electorates)


def _election_to_dict(election: ElectionModel) -> dict[str, object]:
    return {
        "races": {
            race_id: {
                "electorate": {
                    "republican": model.electorate.republican,
                    "democratic": model.electorate.democratic,
                    "independent": model.electorate.independent,
                },
                "state": {
                    "mean": model.filter.state.mean.tolist(),
                    "covariance": model.filter.state.covariance.tolist(),
                },
            }
            for race_id, model in election.races.items()
        }
    }
