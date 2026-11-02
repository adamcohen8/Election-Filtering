"""Versioned snapshots preserving chronology, configuration and nuisance states."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping

import numpy as np

from election_modeling.cycles import create_2026_election_model, ensure_2026_races
from election_modeling.elections import ElectionModel
from election_modeling.filters import KalmanState, RaceKalmanFilter
from election_modeling.races import Electorate, RaceModel
from election_modeling.validation import covariance_matrix

SCHEMA_VERSION = 2


def save_election_model(election: ElectionModel, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(_election_to_dict(election), indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def load_election_model(path: str | Path) -> ElectionModel:
    payload = json.loads(Path(path).read_text())
    if payload.get('schema_version') != SCHEMA_VERSION:
        raise ValueError('Legacy snapshot: replay the chronological poll feed under methodology v2; old snapshots omit dates and persistent errors')
    election = ElectionModel()
    for race_id, record in payload['races'].items():
        electorate = Electorate(**record['electorate'])
        f = record['filter']
        mean = np.asarray(f['joint_mean'], dtype=float)
        keys = f['bias_keys']
        if not isinstance(keys, list) or not all(isinstance(key, str) for key in keys) or len(set(keys)) != len(keys):
            raise ValueError('invalid bias-state keys')
        if mean.shape != (6 + len(keys),) or not np.all(np.isfinite(mean)):
            raise ValueError('invalid joint state')
        covariance = covariance_matrix(f['joint_covariance'], mean.size)
        filter_ = RaceKalmanFilter(
            KalmanState(mean[:6], covariance[:6, :6]), transition=f['transition'],
            process_covariance=f['process_covariance'], clip_support=f['clip_support'],
            shared_margin_sd=f['shared_margin_sd'], pollster_margin_sd=f['pollster_margin_sd'],
            survey_margin_sd=f['survey_margin_sd'],
        )
        filter_._commit(mean, covariance)
        filter_.bias_keys = keys.copy()
        election.races[race_id] = RaceModel(filter_, electorate,
            observation_count=record['observation_count'], last_date=record['last_date'])
    return election


def load_or_create_2026_election_model(path: str | Path, *,
                                     electorates: Mapping[str, Electorate] | None = None) -> ElectionModel:
    if Path(path).exists():
        return ensure_2026_races(load_election_model(path), electorates=electorates)
    return create_2026_election_model(electorates=electorates)


def _election_to_dict(election: ElectionModel) -> dict[str, object]:
    races = {}
    for race_id, model in election.races.items():
        f = model.filter
        races[race_id] = {
            'electorate': {
                'republican': model.electorate.republican,
                'democratic': model.electorate.democratic,
                'independent': model.electorate.independent,
                'share_standard_deviation': model.electorate.share_standard_deviation,
            },
            'observation_count': model.observation_count, 'last_date': model.last_date,
            'filter': {
                'joint_mean': f.joint_mean.tolist(), 'joint_covariance': f.joint_covariance.tolist(),
                'bias_keys': f.bias_keys, 'transition': f.transition.tolist(),
                'process_covariance': f.process_covariance.tolist(), 'clip_support': f.clip_support,
                'shared_margin_sd': f.shared_margin_sd, 'pollster_margin_sd': f.pollster_margin_sd,
                'survey_margin_sd': f.survey_margin_sd,
            },
        }
    return {'schema_version': SCHEMA_VERSION, 'races': races}
