"""Kalman filtering for six-state election support models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from election_modeling.polls import PollObservation


def _symmetrize(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.T) / 2.0


@dataclass(frozen=True)
class KalmanState:
    mean: np.ndarray
    covariance: np.ndarray

    def __post_init__(self) -> None:
        mean = np.asarray(self.mean, dtype=float)
        covariance = np.asarray(self.covariance, dtype=float)
        if mean.shape != (6,):
            raise ValueError("mean must contain exactly 6 values.")
        if covariance.shape != (6, 6):
            raise ValueError("covariance must be a 6x6 matrix.")
        object.__setattr__(self, "mean", mean)
        object.__setattr__(self, "covariance", _symmetrize(covariance))


class RaceKalmanFilter:
    """Linear Kalman filter over six party-ID support states."""

    def __init__(
        self,
        initial_state: KalmanState,
        *,
        transition: Sequence[Sequence[float]] | None = None,
        process_covariance: Sequence[Sequence[float]] | None = None,
        clip_support: bool = True,
    ) -> None:
        self.state = initial_state
        self.transition = (
            np.eye(6, dtype=float)
            if transition is None
            else np.asarray(transition, dtype=float)
        )
        self.process_covariance = (
            np.eye(6, dtype=float) * 0.00005
            if process_covariance is None
            else np.asarray(process_covariance, dtype=float)
        )
        if self.transition.shape != (6, 6):
            raise ValueError("transition must be a 6x6 matrix.")
        if self.process_covariance.shape != (6, 6):
            raise ValueError("process_covariance must be a 6x6 matrix.")
        self.clip_support = clip_support

    def predict(self, *, steps: int = 1) -> KalmanState:
        """Advance the latent race state before ingesting new polling."""

        if steps < 1:
            raise ValueError("steps must be at least 1.")

        mean = self.state.mean
        covariance = self.state.covariance
        for _ in range(steps):
            mean = self.transition @ mean
            covariance = (
                self.transition @ covariance @ self.transition.T
                + self.process_covariance
            )

        self.state = KalmanState(self._bounded(mean), covariance)
        return self.state

    def update(self, observation: PollObservation) -> KalmanState:
        """Update the state estimate with a poll observation."""

        z_full = observation.adjusted_values
        mask = observation.observed_mask
        if not np.any(mask):
            raise ValueError("observation must include at least one finite value.")

        observed_indexes = np.flatnonzero(mask)
        h = np.eye(6, dtype=float)[observed_indexes]
        z = z_full[observed_indexes]
        r = observation.covariance[np.ix_(observed_indexes, observed_indexes)]

        predicted_mean = self.state.mean
        predicted_covariance = self.state.covariance
        innovation = z - h @ predicted_mean
        innovation_covariance = h @ predicted_covariance @ h.T + r
        kalman_gain = (
            predicted_covariance
            @ h.T
            @ np.linalg.pinv(innovation_covariance)
        )

        mean = predicted_mean + kalman_gain @ innovation
        identity = np.eye(6, dtype=float)
        joseph = identity - kalman_gain @ h
        covariance = joseph @ predicted_covariance @ joseph.T + kalman_gain @ r @ kalman_gain.T

        self.state = KalmanState(self._bounded(mean), covariance)
        return self.state

    def _bounded(self, mean: np.ndarray) -> np.ndarray:
        if not self.clip_support:
            return mean
        return np.clip(mean, 0.0, 1.0)
