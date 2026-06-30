"""Election modeling primitives."""

from election_modeling.cycles import (
    DEFAULT_PLACEHOLDER_ELECTORATE,
    GOVERNOR_2026_RACES,
    RACES_2026,
    RACES_2026_BY_ID,
    SENATE_2026_RACES,
    RaceSpec,
    create_2026_election_model,
    race_id_for,
)
from election_modeling.elections import ElectionModel
from election_modeling.filters import KalmanState, RaceKalmanFilter
from election_modeling.automation import AutomationRun, run_2026_poll_io
from election_modeling.ingestion import (
    AppliedPoll,
    IngestionLedger,
    IngestionResult,
    NormalizedPoll,
    PartyIDCrosstab,
    PollIngestionPipeline,
    PollSource,
    RaceClassifier,
    StaticPollSource,
    StructuredCSVSource,
    StructuredJSONSource,
    run_2026_ingestion,
)
from election_modeling.persistence import (
    load_election_model,
    load_or_create_2026_election_model,
    save_election_model,
)
from election_modeling.polls import PollAdjustment, PollObservation
from election_modeling.races import Electorate, Forecast, RaceModel
from election_modeling.states import PARTY_IDS, STATE_INDEX, STATE_NAMES, PartyID

__all__ = [
    "Electorate",
    "ElectionModel",
    "Forecast",
    "DEFAULT_PLACEHOLDER_ELECTORATE",
    "GOVERNOR_2026_RACES",
    "AppliedPoll",
    "AutomationRun",
    "IngestionLedger",
    "IngestionResult",
    "KalmanState",
    "NormalizedPoll",
    "PARTY_IDS",
    "PartyIDCrosstab",
    "PartyID",
    "PollIngestionPipeline",
    "PollSource",
    "PollAdjustment",
    "PollObservation",
    "RACES_2026",
    "RACES_2026_BY_ID",
    "RaceClassifier",
    "RaceKalmanFilter",
    "RaceModel",
    "RaceSpec",
    "SENATE_2026_RACES",
    "STATE_INDEX",
    "STATE_NAMES",
    "StaticPollSource",
    "StructuredCSVSource",
    "StructuredJSONSource",
    "create_2026_election_model",
    "load_election_model",
    "load_or_create_2026_election_model",
    "race_id_for",
    "run_2026_ingestion",
    "run_2026_poll_io",
    "save_election_model",
]
