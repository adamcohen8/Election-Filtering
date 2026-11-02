"""Race estimates with dated updates and explicit uncertainty components."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import date
from typing import Sequence

import numpy as np

from election_modeling.filters import KalmanState, RaceKalmanFilter
from election_modeling.polls import LinearPollObservation, PollObservation, _share_variance
from election_modeling.validation import nonnegative, sample_size as validate_sample_size


def parse_date(value: str) -> date:
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError("dates must use YYYY-MM-DD")
    return parsed


@dataclass(frozen=True)
class Electorate:
    """R/D/I central shares; each share defaults to 1 percentage-point SD.

    Equal marginal variances and a fixed sum imply pairwise correlation -1/2.
    This is a local Gaussian moment model, appropriate for the supplied central
    shares, which are all more than three SDs from the boundaries.
    """
    republican: float
    democratic: float
    independent: float
    share_standard_deviation: float = 0.01

    def __post_init__(self) -> None:
        vector = self.party_vector()
        if not np.all(np.isfinite(vector)) or np.any(vector < 0) or np.any(vector > 1):
            raise ValueError("electorate shares must be finite and in [0, 1]")
        if not np.isclose(vector.sum(), 1.0, rtol=0, atol=1e-10):
            raise ValueError("electorate shares must sum to 1")
        object.__setattr__(self, "share_standard_deviation",
                           nonnegative(self.share_standard_deviation, "electorate share SD"))

    def party_vector(self) -> np.ndarray:
        return np.asarray([self.republican, self.democratic, self.independent], dtype=float)

    def as_vector(self) -> np.ndarray:
        return np.repeat(self.party_vector(), 2)

    def margin_gradient(self) -> np.ndarray:
        return self.as_vector() * np.tile([1, -1], 3)

    def covariance(self) -> np.ndarray:
        return self.share_standard_deviation**2 * (1.5 * np.eye(3) - 0.5 * np.ones((3, 3)))


@dataclass(frozen=True)
class Forecast:
    candidate_a_share: float
    candidate_b_share: float
    margin: float
    margin_standard_error: float
    margin_of_error: float
    z_score: float
    state: KalmanState
    polling_variance: float
    movement_variance: float
    turnout_variance: float
    observation_count: int
    state_date: str | None
    forecast_date: str | None

    @property
    def candidate_a_percent(self) -> float:
        return self.candidate_a_share * 100

    @property
    def candidate_b_percent(self) -> float:
        return self.candidate_b_share * 100

    @property
    def margin_percent(self) -> float:
        return self.margin * 100

    @property
    def margin_of_error_percent(self) -> float:
        return self.margin_of_error * 100


class RaceModel:
    """Constrained support filter plus an independent turnout-composition model."""
    def __init__(self, filter_: RaceKalmanFilter, electorate: Electorate, *,
                 observation_count: int = 0, last_date: str | None = None) -> None:
        if isinstance(observation_count, bool) or not isinstance(observation_count, int) or observation_count < 0:
            raise ValueError("observation count must be a non-negative integer")
        if last_date is not None:
            parse_date(last_date)
        self.filter = filter_
        self.electorate = electorate
        self.observation_count = observation_count
        self.last_date = last_date

    @classmethod
    def default(cls, *, electorate: Electorate, initial_mean: Sequence[float] | None = None,
                initial_variance: float = 0.04, process_variance: float = 0.00005,
                shared_margin_sd: float = 0.02, pollster_margin_sd: float = 0.01,
                survey_margin_sd: float = 0.01) -> "RaceModel":
        initial_variance = nonnegative(initial_variance, "initial variance")
        process_variance = nonnegative(process_variance, "process variance")
        if initial_variance == 0:
            raise ValueError("initial variance must be positive")
        if initial_mean is None:
            initial_mean = (0.86, 0.10, 0.08, 0.88, 0.46, 0.46)
        state = KalmanState(np.asarray(initial_mean, dtype=float), np.eye(6) * initial_variance)
        return cls(RaceKalmanFilter(
            state, process_covariance=np.eye(6) * process_variance,
            shared_margin_sd=shared_margin_sd, pollster_margin_sd=pollster_margin_sd,
            survey_margin_sd=survey_margin_sd,
        ), electorate)

    def predict(self, *, steps: int = 1) -> KalmanState:
        # Explicit manual prediction moves the stored calendar date as well.
        from datetime import timedelta
        state = self.filter.predict(steps=steps)
        if self.last_date is not None:
            self.last_date = (parse_date(self.last_date) + timedelta(days=steps)).isoformat()
        return state

    def _apply(self, observation: PollObservation | LinearPollObservation) -> KalmanState:
        next_date = observation.field_date
        if next_date is not None:
            parse_date(next_date)
        elif self.last_date is not None:
            raise ValueError("dated models require dated observations")
        if next_date is not None and self.last_date is None and self.observation_count:
            raise ValueError("replay undated observations with dates before adding dated polls")
        working = deepcopy(self.filter)
        if self.last_date is not None and next_date is not None:
            days = (parse_date(next_date) - parse_date(self.last_date)).days
            if days < 0:
                raise ValueError("out-of-order poll: replay the full chronological feed")
            if days:
                working.predict(steps=days)
        if isinstance(observation, PollObservation):
            working.update(observation)
        else:
            working.update_linear(observation)
        self.filter = working
        self.last_date = next_date
        self.observation_count += 1
        return self.filter.state

    def update(self, observation: PollObservation) -> KalmanState:
        return self._apply(observation)

    def update_topline(self, *, candidate_a_share: float, candidate_b_share: float,
                       sample_size: int, pollster: str | None = None,
                       field_date: str | None = None, extra_variance: float = 0.0,
                       design_effect: float = 1.5, sample_id: str | None = None) -> KalmanState:
        n = validate_sample_size(sample_size)
        design_effect = nonnegative(design_effect, "design effect")
        extra_variance = nonnegative(extra_variance, "extra variance")
        if design_effect == 0:
            raise ValueError("design effect must be positive")
        a, b = float(candidate_a_share), float(candidate_b_share)
        if not np.all(np.isfinite([a, b])) or min(a, b) < 0 or a + b > 1:
            raise ValueError("topline shares must be finite, non-negative, and sum to at most 1")
        n_eff = n / design_effect
        covariance = np.array([[_share_variance(a, n_eff), -a*b/n_eff],
                               [-a*b/n_eff, _share_variance(b, n_eff)]])
        covariance += np.eye(2) * extra_variance
        h = np.zeros((2, 6))
        h[0, ::2] = self.electorate.party_vector()
        h[1, 1::2] = self.electorate.party_vector()
        return self._apply(LinearPollObservation(
            values=np.array([a, b]), covariance=covariance, design_matrix=h,
            pollster=pollster, field_date=field_date, sample_id=sample_id,
        ))

    def forecast(self, *, z_score: float = 1.96, target_date: str | None = None) -> Forecast:
        z_score = nonnegative(z_score, "z score")
        if z_score == 0:
            raise ValueError("z score must be positive")
        projected = self.filter
        if target_date is not None:
            parse_date(target_date)
            if self.last_date is None and self.observation_count:
                raise ValueError("an election-day forecast requires dated observations")
            if self.last_date is not None:
                days = (parse_date(target_date) - parse_date(self.last_date)).days
                if days < 0:
                    raise ValueError("forecast date precedes the model state")
                if days:
                    projected = deepcopy(self.filter)
                    projected.predict(steps=days)
        state = projected.state
        w = self.electorate.party_vector()
        support = state.mean.reshape(3, 2)
        candidate_a, candidate_b = w @ support
        difference = np.zeros((3, 6))
        for party in range(3):
            difference[party, 2*party:2*party+2] = [1, -1]
        d = difference @ state.mean
        sigma_d = difference @ state.covariance @ difference.T
        sigma_w = self.electorate.covariance()
        # Exact second moment of a bilinear form for independent w and d.
        # Includes the interaction term omitted by a first-order delta method.
        turnout_variance = float(d @ sigma_w @ d + np.trace(sigma_w @ sigma_d))
        state_variance = float(w @ sigma_d @ w)
        current_variance = float(self.electorate.margin_gradient() @ self.filter.state.covariance @ self.electorate.margin_gradient())
        polling_variance = min(current_variance, state_variance)
        movement_variance = state_variance - polling_variance
        variance = state_variance + turnout_variance
        if not np.isfinite(variance) or min(state_variance, turnout_variance) < -1e-12:
            raise ValueError("invalid forecast variance")
        standard_error = float(np.sqrt(max(variance, 0)))  # roundoff only; matrices validated upstream
        return Forecast(
            candidate_a_share=float(candidate_a), candidate_b_share=float(candidate_b),
            margin=float(candidate_a-candidate_b), margin_standard_error=standard_error,
            margin_of_error=z_score*standard_error, z_score=z_score, state=state,
            polling_variance=max(0.0, polling_variance), movement_variance=max(0.0, movement_variance),
            turnout_variance=max(0.0, turnout_variance), observation_count=self.observation_count,
            state_date=self.last_date, forecast_date=target_date or self.last_date,
        )
