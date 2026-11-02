"""Constrained Gaussian filtering with persistent directional polling errors."""
from __future__ import annotations

from dataclasses import dataclass
from math import erfc, exp, pi, sqrt
from typing import Sequence

import numpy as np

from election_modeling.polls import LinearPollObservation, PollObservation
from election_modeling.validation import covariance_matrix, nonnegative


@dataclass(frozen=True)
class KalmanState:
    mean: np.ndarray
    covariance: np.ndarray

    def __post_init__(self) -> None:
        mean = np.array(self.mean, dtype=float, copy=True)
        if mean.shape != (6,) or not np.all(np.isfinite(mean)):
            raise ValueError("mean must contain exactly 6 finite values")
        covariance = covariance_matrix(self.covariance, 6)
        mean.setflags(write=False)
        covariance.setflags(write=False)
        object.__setattr__(self, "mean", mean)
        object.__setattr__(self, "covariance", covariance)


def _mills_ratio(alpha: float) -> float:
    # Stable inverse Mills ratio phi(alpha)/Phi(alpha), including deep tails.
    if alpha < -8:
        t = -alpha
        return t + 1 / t - 2 / t**3 + 10 / t**5 - 74 / t**7
    return exp(-alpha * alpha / 2) / sqrt(2 * pi) / (0.5 * erfc(-alpha / sqrt(2)))


def _constrain(mean: np.ndarray, covariance: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Moment-match violated simplex half-spaces; update all cross-covariances.

    Each step uses the exact moments of a Gaussian truncated by a*x <= b.
    Replacing the result by a Gaussian between constraints is an assumed-density
    approximation, not an exact multivariate truncated-normal posterior.
    """
    mean, covariance = mean.copy(), covariance.copy()
    constraints = []
    for first in (0, 2, 4):
        for offset in (0, 1):
            a = np.zeros(mean.size)
            a[first + offset] = -1
            constraints.append((a, 0.0))
        a = np.zeros(mean.size)
        a[first:first + 2] = 1
        constraints.append((a, 1.0))
    for _ in range(256):
        a, bound = max(constraints, key=lambda item: item[0] @ mean - item[1])
        violation = float(a @ mean - bound)
        if violation <= 1e-13:
            # Remove floating-point-sized violations only.
            mean[:6] = np.maximum(mean[:6], 0)
            for first in (0, 2, 4):
                total = mean[first:first + 2].sum()
                if total > 1:
                    mean[first:first + 2] /= total
            return mean, (covariance + covariance.T) / 2
        pa = covariance @ a
        variance = float(a @ pa)
        if variance <= 1e-18:
            raise ValueError("infeasible deterministic support state")
        sigma = sqrt(variance)
        alpha = -violation / sigma
        ratio = _mills_ratio(alpha)
        mean -= pa * (ratio / sigma)
        reduction = min(1.0, max(0.0, ratio * (ratio + alpha)))
        covariance -= np.outer(pa, pa) / variance * reduction
        covariance = (covariance + covariance.T) / 2
    raise ValueError("support constraints did not converge")


class RaceKalmanFilter:
    """Six support states plus shared, pollster and survey margin-error states.

    Bias standard deviations are in *margin* units. The defaults are explicit
    provisional assumptions, not estimates calibrated on historical elections.
    """
    def __init__(
        self,
        initial_state: KalmanState,
        *,
        transition: Sequence[Sequence[float]] | None = None,
        process_covariance: Sequence[Sequence[float]] | None = None,
        clip_support: bool = True,
        shared_margin_sd: float = 0.02,
        pollster_margin_sd: float = 0.01,
        survey_margin_sd: float = 0.01,
    ) -> None:
        self.transition = np.array(np.eye(6) if transition is None else transition, dtype=float)
        if self.transition.shape != (6, 6) or not np.all(np.isfinite(self.transition)):
            raise ValueError("transition must be a finite 6x6 matrix")
        self.process_covariance = covariance_matrix(
            np.eye(6) * 0.00005 if process_covariance is None else process_covariance, 6, "process covariance"
        )
        self.clip_support = bool(clip_support)
        self.shared_margin_sd = nonnegative(shared_margin_sd, "shared margin SD")
        self.pollster_margin_sd = nonnegative(pollster_margin_sd, "pollster margin SD")
        self.survey_margin_sd = nonnegative(survey_margin_sd, "survey margin SD")
        self.bias_keys: list[str] = []
        self.joint_mean = initial_state.mean.copy()
        self.joint_covariance = initial_state.covariance.copy()
        self._commit(self.joint_mean, self.joint_covariance)

    @property
    def state(self) -> KalmanState:
        return KalmanState(self.joint_mean[:6], self.joint_covariance[:6, :6])

    def _commit(self, mean: np.ndarray, covariance: np.ndarray) -> None:
        covariance = covariance_matrix(covariance, mean.size)
        if self.clip_support:
            mean, covariance = _constrain(mean, covariance)
        self.joint_mean = mean
        self.joint_covariance = covariance_matrix(covariance, mean.size)

    def predict(self, *, steps: int = 1) -> KalmanState:
        if isinstance(steps, bool) or not isinstance(steps, (int, np.integer)) or steps < 1:
            raise ValueError("steps must be a positive integer")
        transition = np.eye(self.joint_mean.size)
        transition[:6, :6] = self.transition
        mean, covariance = self.joint_mean.copy(), self.joint_covariance.copy()
        for _ in range(steps):
            mean = transition @ mean
            covariance = transition @ covariance @ transition.T
            covariance[:6, :6] += self.process_covariance
        self._commit(mean, covariance)
        return self.state

    def update(self, observation: PollObservation) -> KalmanState:
        indexes = np.flatnonzero(observation.observed_mask)
        if not indexes.size:
            raise ValueError("observation must include at least one finite value")
        return self._update_linear(
            values=observation.adjusted_values[indexes],
            measurement_covariance=observation.covariance[np.ix_(indexes, indexes)],
            design_matrix=np.eye(6)[indexes],
            pollster=observation.pollster,
            field_date=observation.field_date,
            sample_id=observation.sample_id,
        )

    def update_linear(self, observation: LinearPollObservation) -> KalmanState:
        return self._update_linear(
            values=observation.values,
            measurement_covariance=observation.covariance,
            design_matrix=observation.design_matrix,
            pollster=observation.pollster,
            field_date=observation.field_date,
            sample_id=observation.sample_id,
        )

    def _update_linear(self, *, values, measurement_covariance, design_matrix,
                       pollster=None, field_date=None, sample_id=None) -> KalmanState:
        mean, covariance = self.joint_mean.copy(), self.joint_covariance.copy()
        keys = self.bias_keys.copy()
        pollster_key = " ".join((pollster or "unknown").casefold().split())
        effects = [
            ("shared", self.shared_margin_sd),
            (f"pollster:{pollster_key}", self.pollster_margin_sd),
            (f"survey:{pollster_key}:{sample_id or field_date or 'undated'}", self.survey_margin_sd),
        ]
        active = []
        for key, sd in effects:
            if sd == 0:
                continue
            if key not in keys:
                keys.append(key)
                mean = np.append(mean, 0.0)
                enlarged = np.zeros((mean.size, mean.size))
                enlarged[:-1, :-1] = covariance
                enlarged[-1, -1] = sd**2
                covariance = enlarged
            active.append(6 + keys.index(key))
        h = np.zeros((values.size, mean.size))
        h[:, :6] = design_matrix
        direction = design_matrix @ np.tile([0.5, -0.5], 3)
        for index in active:
            h[:, index] = direction
        innovation = values - h @ mean
        s = h @ covariance @ h.T + measurement_covariance
        gain = covariance @ h.T @ np.linalg.pinv(s, hermitian=True)
        mean += gain @ innovation
        joseph = np.eye(mean.size) - gain @ h
        covariance = joseph @ covariance @ joseph.T + gain @ measurement_covariance @ gain.T
        self._commit(mean, covariance)
        self.bias_keys = keys
        return self.state
