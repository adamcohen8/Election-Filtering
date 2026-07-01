"""Polling observations and poll-level adjustments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

from election_modeling.states import PARTY_IDS, PARTY_STATE_SLICES, PartyID


def _as_vector(values: Sequence[float], *, name: str) -> np.ndarray:
    vector = np.asarray(values, dtype=float)
    if vector.shape != (6,):
        raise ValueError(f"{name} must contain exactly 6 values.")
    return vector


def _as_square_matrix(values: Sequence[Sequence[float]], *, name: str) -> np.ndarray:
    matrix = np.asarray(values, dtype=float)
    if matrix.shape != (6, 6):
        raise ValueError(f"{name} must be a 6x6 matrix.")
    return matrix


@dataclass(frozen=True)
class PollAdjustment:
    """Additive correction for a poll's observed six-state support vector.

    Use positive values when the raw poll should be moved upward for that state
    and negative values when it should be moved downward.
    """

    values: np.ndarray

    @classmethod
    def from_values(cls, values: Sequence[float]) -> "PollAdjustment":
        return cls(values=_as_vector(values, name="adjustment values"))


@dataclass(frozen=True)
class LinearPollObservation:
    """A noisy poll observation with a custom linear measurement matrix."""

    values: np.ndarray
    covariance: np.ndarray
    design_matrix: np.ndarray
    pollster: str | None = None
    field_date: str | None = None

    def __post_init__(self) -> None:
        values = np.asarray(self.values, dtype=float)
        covariance = np.asarray(self.covariance, dtype=float)
        design_matrix = np.asarray(self.design_matrix, dtype=float)
        if values.ndim != 1:
            raise ValueError("linear observation values must be a vector.")
        if covariance.shape != (values.size, values.size):
            raise ValueError("linear observation covariance shape does not match values.")
        if design_matrix.shape != (values.size, 6):
            raise ValueError("linear observation design matrix must have 6 columns.")
        if not np.all(np.isfinite(values)):
            raise ValueError("linear observation values must contain finite values.")
        if not np.all(np.isfinite(covariance)):
            raise ValueError("linear observation covariance must contain finite values.")
        if not np.all(np.isfinite(design_matrix)):
            raise ValueError("linear observation design matrix must contain finite values.")
        if np.any(np.diag(covariance) <= 0):
            raise ValueError("linear observation covariance diagonal must be positive.")
        object.__setattr__(self, "values", values)
        object.__setattr__(self, "covariance", covariance)
        object.__setattr__(self, "design_matrix", design_matrix)


@dataclass(frozen=True)
class PollObservation:
    """A noisy poll observation of the six latent support states.

    Missing state cells can be represented with ``np.nan`` in ``values``. The
    Kalman update will use only the observed cells.
    """

    values: np.ndarray
    covariance: np.ndarray
    adjustment: PollAdjustment | None = None
    pollster: str | None = None
    field_date: str | None = None

    def __post_init__(self) -> None:
        values = _as_vector(self.values, name="poll values")
        covariance = _as_square_matrix(self.covariance, name="poll covariance")
        if not np.all(np.isfinite(covariance)):
            raise ValueError("poll covariance must contain finite values.")
        if np.any(np.diag(covariance) <= 0):
            raise ValueError("poll covariance diagonal must be positive.")
        object.__setattr__(self, "values", values)
        object.__setattr__(self, "covariance", covariance)

    @property
    def adjusted_values(self) -> np.ndarray:
        if self.adjustment is None:
            return self.values.copy()
        return self.values + self.adjustment.values

    @property
    def observed_mask(self) -> np.ndarray:
        return np.isfinite(self.adjusted_values)

    @classmethod
    def from_party_id_shares(
        cls,
        *,
        values: Mapping[PartyID, tuple[float, float]],
        subgroup_sample_sizes: Mapping[PartyID, int],
        adjustment: PollAdjustment | None = None,
        pollster: str | None = None,
        field_date: str | None = None,
        extra_variance: float = 0.0,
    ) -> "PollObservation":
        """Build an observation from party-ID candidate shares.

        ``values`` maps each party-ID group to ``(candidate_a, candidate_b)``.
        If a party-ID group is omitted, its two states are treated as missing.
        Within each party-ID group, covariance is estimated with a multinomial
        approximation, preserving negative covariance between the two candidates.
        """

        vector = np.full(6, np.nan, dtype=float)
        covariance = np.eye(6, dtype=float)

        for party_id in PARTY_IDS:
            first, second = PARTY_STATE_SLICES[party_id]
            if party_id not in values:
                covariance[first, first] = 1.0
                covariance[second, second] = 1.0
                continue

            candidate_a, candidate_b = values[party_id]
            n = subgroup_sample_sizes[party_id]
            if n <= 0:
                raise ValueError(f"sample size for {party_id} must be positive.")
            if candidate_a < 0 or candidate_b < 0 or candidate_a + candidate_b > 1:
                raise ValueError(
                    f"shares for {party_id} must be non-negative and sum to at most 1."
                )

            vector[first] = candidate_a
            vector[second] = candidate_b
            covariance[first, first] = candidate_a * (1.0 - candidate_a) / n
            covariance[second, second] = candidate_b * (1.0 - candidate_b) / n
            covariance[first, second] = -candidate_a * candidate_b / n
            covariance[second, first] = covariance[first, second]

        if extra_variance < 0:
            raise ValueError("extra_variance must be non-negative.")
        covariance = covariance + np.eye(6) * extra_variance

        return cls(
            values=vector,
            covariance=covariance,
            adjustment=adjustment,
            pollster=pollster,
            field_date=field_date,
        )
