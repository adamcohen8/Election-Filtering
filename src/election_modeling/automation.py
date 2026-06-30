"""Convenience runner for recurring 2026 poll IO automation."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from election_modeling.elections import ElectionModel
from election_modeling.ingestion import (
    IngestionResult,
    PollSource,
    StructuredCSVSource,
    StructuredJSONSource,
    run_2026_ingestion,
)
from election_modeling.persistence import (
    load_or_create_2026_election_model,
    save_election_model,
)
from election_modeling.races import Electorate


@dataclass(frozen=True)
class AutomationRun:
    election: ElectionModel
    result: IngestionResult
    snapshot_path: Path
    ledger_path: Path


def run_2026_poll_io(
    *,
    csv_sources: Iterable[str] = (),
    json_sources: Iterable[str] = (),
    custom_sources: Iterable[PollSource] = (),
    snapshot_path: str | Path = "data/models/2026_election_model.json",
    ledger_path: str | Path = "data/ingestion/2026_seen_polls.json",
    electorates: Mapping[str, Electorate] | None = None,
    extra_variance: float = 0.0,
) -> AutomationRun:
    """Load model state, ingest new polls, update filters, and save state."""

    snapshot = Path(snapshot_path)
    ledger = Path(ledger_path)
    election = load_or_create_2026_election_model(snapshot, electorates=electorates)
    sources: list[PollSource] = [
        *(StructuredCSVSource(location) for location in csv_sources),
        *(StructuredJSONSource(location) for location in json_sources),
        *custom_sources,
    ]
    result = run_2026_ingestion(
        election,
        sources,
        ledger_path=ledger,
        extra_variance=extra_variance,
    )
    save_election_model(election, snapshot)
    return AutomationRun(
        election=election,
        result=result,
        snapshot_path=snapshot,
        ledger_path=ledger,
    )
