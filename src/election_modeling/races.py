"""Race-level forecasting from filtered party-ID support states."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from election_modeling.filters import KalmanState, RaceKalmanFilter
from election_modeling.polls import LinearPollObservation, PollObservation


@dataclass(frozen=True)
class Electorate:
    """Predicted electorate composition by party ID."""

    republican: float
    democratic: float
    independent: float

    def __post_init__(self) -> None:
        vector = self.party_vector()
        if np.any(vector < 0):
            raise ValueError("electorate shares must be non-negative.")
        total = float(np.sum(vector))
        if not np.isclose(total, 1.0):
            raise ValueError("electorate shares must sum to 1.")

    def party_vector(self) -> np.ndarray:
        return np.asarray(
            [self.republican, self.democratic, self.independent],
            dtype=float,
        )

    def as_vector(self) -> np.ndarray:
        return np.asarray(
            [self.republican, self.republican, self.democratic, self.democratic, self.independent, self.independent],
            dtype=float,
        )

    def margin_gradient(self) -> np.ndarray:
        return np.asarray(
            [
                self.republican,
                -self.republican,
                self.democratic,
                -self.democratic,
                self.independent,
                -self.independent,
            ],
            dtype=float,
        )


@dataclass(frozen=True)
class Forecast:
    """Race forecast from the current filtered state."""

    candidate_a_share: float
    candidate_b_share: float
    margin: float
    margin_standard_error: float
    margin_of_error: float
    z_score: float
    state: KalmanState

    @property
    def candidate_a_percent(self) -> float:
        return self.candidate_a_share * 100.0

    @property
    def candidate_b_percent(self) -> float:
        return self.candidate_b_share * 100.0

    @property
    def margin_percent(self) -> float:
        return self.margin * 100.0

    @property
    def margin_of_error_percent(self) -> float:
        return self.margin_of_error * 100.0


class RaceModel:
    """Combines a six-state Kalman filter with an electorate forecast."""

    def __init__(self, filter_: RaceKalmanFilter, electorate: Electorate) -> None:
        self.filter = filter_
        self.electorate = electorate

    @classmethod
    def default(
        cls,
        *,
        electorate: Electorate,
        initial_mean: Sequence[float] | None = None,
        initial_variance: float = 0.04,
        process_variance: float = 0.00005,
    ) -> "RaceModel":
        """Create a race model with broad priors and a random-walk transition."""

        if initial_mean is None:
            initial_mean = (0.86, 0.10, 0.08, 0.88, 0.46, 0.46)
        if initial_variance <= 0:
            raise ValueError("initial_variance must be positive.")
        if process_variance < 0:
            raise ValueError("process_variance must be non-negative.")

        state = KalmanState(
            mean=np.asarray(initial_mean, dtype=float),
            covariance=np.eye(6, dtype=float) * initial_variance,
        )
        filter_ = RaceKalmanFilter(
            state,
            process_covariance=np.eye(6, dtype=float) * process_variance,
        )
        return cls(filter_=filter_, electorate=electorate)

    def predict(self, *, steps: int = 1) -> KalmanState:
        return self.filter.predict(steps=steps)

    def update(self, observation: PollObservation) -> KalmanState:
        return self.filter.update(observation)

    def update_topline(
        self,
        *,
        candidate_a_share: float,
        candidate_b_share: float,
        sample_size: int,
        pollster: str | None = None,
        field_date: str | None = None,
        extra_variance: float = 0.0,
    ) -> KalmanState:
        """Update from an aggregate ballot test when crosstabs are unavailable."""

        if sample_size <= 0:
            raise ValueError("topline sample size must be positive.")
        if candidate_a_share < 0 or candidate_b_share < 0:
            raise ValueError("topline shares must be non-negative.")
        if candidate_a_share + candidate_b_share > 1:
            raise ValueError("topline shares must sum to at most 1.")
        if extra_variance < 0:
            raise ValueError("extra_variance must be non-negative.")

        values = np.asarray([candidate_a_share, candidate_b_share], dtype=float)
        covariance = np.asarray(
            [
                [
                    candidate_a_share * (1.0 - candidate_a_share) / sample_size,
                    -candidate_a_share * candidate_b_share / sample_size,
                ],
                [
                    -candidate_a_share * candidate_b_share / sample_size,
                    candidate_b_share * (1.0 - candidate_b_share) / sample_size,
                ],
            ],
            dtype=float,
        )
        covariance = covariance + np.eye(2, dtype=float) * extra_variance
        design_matrix = np.asarray(
            [
                [
                    self.electorate.republican,
                    0.0,
                    self.electorate.democratic,
                    0.0,
                    self.electorate.independent,
                    0.0,
                ],
                [
                    0.0,
                    self.electorate.republican,
                    0.0,
                    self.electorate.democratic,
                    0.0,
                    self.electorate.independent,
                ],
            ],
            dtype=float,
        )
        observation = LinearPollObservation(
            values=values,
            covariance=covariance,
            design_matrix=design_matrix,
            pollster=pollster,
            field_date=field_date,
        )
        return self.filter.update_linear(observation)

    def forecast(self, *, z_score: float = 1.96) -> Forecast:
        """Forecast the top-line race margin from the current filtered state."""

        if z_score <= 0:
            raise ValueError("z_score must be positive.")

        state = self.filter.state
        weights = self.electorate.as_vector()
        candidate_a_selector = np.asarray([1, 0, 1, 0, 1, 0], dtype=float)
        candidate_b_selector = np.asarray([0, 1, 0, 1, 0, 1], dtype=float)

        candidate_a = float(np.sum(weights * candidate_a_selector * state.mean))
        candidate_b = float(np.sum(weights * candidate_b_selector * state.mean))
        gradient = self.electorate.margin_gradient()
        margin = candidate_a - candidate_b
        margin_variance = float(gradient @ state.covariance @ gradient.T)
        margin_standard_error = float(np.sqrt(max(0.0, margin_variance)))

        return Forecast(
            candidate_a_share=candidate_a,
            candidate_b_share=candidate_b,
            margin=margin,
            margin_standard_error=margin_standard_error,
            margin_of_error=z_score * margin_standard_error,
            z_score=z_score,
            state=state,
        )
