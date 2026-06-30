"""Polling IO automation for web and structured feed ingestion."""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Mapping, Protocol
from urllib.request import Request, urlopen

from election_modeling.cycles import RACES_2026_BY_ID, Office, race_id_for
from election_modeling.elections import ElectionModel
from election_modeling.polls import PollAdjustment, PollObservation
from election_modeling.races import RaceModel
from election_modeling.states import PARTY_IDS, PartyID


@dataclass(frozen=True)
class PartyIDCrosstab:
    """Party-ID cross-tab support for a two-candidate poll."""

    values: Mapping[PartyID, tuple[float, float]]
    subgroup_sample_sizes: Mapping[PartyID, int]

    def to_observation(
        self,
        *,
        adjustment: PollAdjustment | None = None,
        pollster: str | None = None,
        field_date: str | None = None,
        extra_variance: float = 0.0,
    ) -> PollObservation:
        return PollObservation.from_party_id_shares(
            values=self.values,
            subgroup_sample_sizes=self.subgroup_sample_sizes,
            adjustment=adjustment,
            pollster=pollster,
            field_date=field_date,
            extra_variance=extra_variance,
        )


@dataclass(frozen=True)
class NormalizedPoll:
    """A poll record after source-specific scraping and normalization."""

    poll_id: str
    pollster: str
    field_date: str
    crosstab: PartyIDCrosstab
    race_id: str | None = None
    state: str | None = None
    office: Office | None = None
    candidate_a: str | None = None
    candidate_b: str | None = None
    source_url: str | None = None
    text: str = ""

    @classmethod
    def from_mapping(cls, row: Mapping[str, object]) -> "NormalizedPoll":
        normalized = {_normalize_key(key): value for key, value in row.items()}
        race_id = _empty_to_none(_string_value(normalized.get("race_id")))
        state = _empty_to_none(_string_value(normalized.get("state")))
        office = _parse_office(_empty_to_none(_string_value(normalized.get("office"))))
        pollster = _required_string(normalized, "pollster")
        field_date = _required_string(normalized, "field_date")
        candidate_a = _empty_to_none(_string_value(normalized.get("candidate_a")))
        candidate_b = _empty_to_none(_string_value(normalized.get("candidate_b")))
        source_url = _empty_to_none(_string_value(normalized.get("source_url")))
        text = _string_value(normalized.get("text")) or " ".join(
            value for value in (pollster, field_date, state or "", office or "") if value
        )

        values: dict[PartyID, tuple[float, float]] = {}
        sample_sizes: dict[PartyID, int] = {}
        for party_id in PARTY_IDS:
            a_value = _find_value(
                normalized,
                f"{party_id}_candidate_a",
                f"{party_id}_a",
                f"{party_id}_dem",
                f"{party_id}_candidate_1",
            )
            b_value = _find_value(
                normalized,
                f"{party_id}_candidate_b",
                f"{party_id}_b",
                f"{party_id}_rep",
                f"{party_id}_candidate_2",
            )
            n_value = _find_value(
                normalized,
                f"{party_id}_sample_size",
                f"{party_id}_n",
                f"{party_id}_sample",
            )
            if a_value is None and b_value is None and n_value is None:
                continue
            if a_value is None or b_value is None or n_value is None:
                raise ValueError(f"incomplete {party_id} crosstab fields")
            values[party_id] = (_parse_share(a_value), _parse_share(b_value))
            sample_sizes[party_id] = _parse_int(n_value)

        if not values:
            raise ValueError("poll row does not include any party-ID crosstabs")

        poll_id = _empty_to_none(_string_value(normalized.get("poll_id")))
        if poll_id is None:
            poll_id = _stable_poll_id(
                pollster=pollster,
                field_date=field_date,
                race_id=race_id,
                state=state,
                office=office,
                values=values,
                source_url=source_url,
            )

        return cls(
            poll_id=poll_id,
            pollster=pollster,
            field_date=field_date,
            crosstab=PartyIDCrosstab(values=values, subgroup_sample_sizes=sample_sizes),
            race_id=race_id,
            state=state,
            office=office,
            candidate_a=candidate_a,
            candidate_b=candidate_b,
            source_url=source_url,
            text=text,
        )


class PollSource(Protocol):
    """Source adapter that returns normalized polls from the web or local files."""

    name: str

    def fetch(self) -> Iterable[NormalizedPoll]:
        ...


@dataclass(frozen=True)
class StaticPollSource:
    """Small source adapter for tests, demos, and manually curated poll drops."""

    polls: Iterable[NormalizedPoll]
    name: str = "static"

    def fetch(self) -> Iterable[NormalizedPoll]:
        return list(self.polls)


@dataclass(frozen=True)
class StructuredCSVSource:
    """Fetch a CSV of normalized poll rows from a URL or local path."""

    location: str
    name: str = "structured_csv"

    def fetch(self) -> Iterable[NormalizedPoll]:
        text = _read_text_location(self.location)
        return [
            NormalizedPoll.from_mapping(row)
            for row in csv.DictReader(text.splitlines())
        ]


@dataclass(frozen=True)
class StructuredJSONSource:
    """Fetch JSON normalized poll rows from a URL or local path."""

    location: str
    name: str = "structured_json"

    def fetch(self) -> Iterable[NormalizedPoll]:
        text = _read_text_location(self.location)
        payload = json.loads(text)
        rows = payload["polls"] if isinstance(payload, dict) else payload
        return [NormalizedPoll.from_mapping(row) for row in rows]


@dataclass(frozen=True)
class RaceClassifier:
    """Classify normalized poll records into known race IDs."""

    known_races: Mapping[str, object] = field(default_factory=lambda: RACES_2026_BY_ID)

    def classify(self, poll: NormalizedPoll) -> str | None:
        if poll.race_id in self.known_races:
            return poll.race_id
        if poll.state and poll.office:
            race_id = race_id_for(poll.state, poll.office)
            if race_id in self.known_races:
                return race_id

        text = poll.text.lower()
        for race_id, race in self.known_races.items():
            state = getattr(race, "state").lower()
            office = getattr(race, "office")
            office_terms = ("senate", "senator") if office == "senate" else ("governor", "gubernatorial")
            if state in text and any(term in text for term in office_terms):
                return race_id
        return None


@dataclass
class IngestionLedger:
    """Tracks poll IDs already applied to avoid double-updating filters."""

    seen_poll_ids: set[str] = field(default_factory=set)
    path: Path | None = None

    @classmethod
    def load(cls, path: str | Path) -> "IngestionLedger":
        ledger_path = Path(path)
        if not ledger_path.exists():
            return cls(path=ledger_path)
        payload = json.loads(ledger_path.read_text())
        return cls(seen_poll_ids=set(payload.get("seen_poll_ids", [])), path=ledger_path)

    def has_seen(self, poll_id: str) -> bool:
        return poll_id in self.seen_poll_ids

    def mark_seen(self, poll_id: str) -> None:
        self.seen_poll_ids.add(poll_id)

    def save(self) -> None:
        if self.path is None:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"seen_poll_ids": sorted(self.seen_poll_ids)}
        self.path.write_text(json.dumps(payload, indent=2) + "\n")


@dataclass(frozen=True)
class AppliedPoll:
    poll_id: str
    race_id: str
    pollster: str
    field_date: str


@dataclass(frozen=True)
class IngestionResult:
    applied: tuple[AppliedPoll, ...]
    duplicate_poll_ids: tuple[str, ...]
    unclassified_poll_ids: tuple[str, ...]
    unknown_race_ids: tuple[str, ...]
    errors: tuple[str, ...]


@dataclass
class PollIngestionPipeline:
    """Fetch, classify, normalize, and apply new polls to race models."""

    sources: tuple[PollSource, ...]
    classifier: RaceClassifier = field(default_factory=RaceClassifier)
    ledger: IngestionLedger = field(default_factory=IngestionLedger)
    adjustment_by_poll_id: Mapping[str, PollAdjustment] = field(default_factory=dict)
    extra_variance: float = 0.0

    def run(self, election: ElectionModel) -> IngestionResult:
        applied: list[AppliedPoll] = []
        duplicates: list[str] = []
        unclassified: list[str] = []
        unknown_race_ids: list[str] = []
        errors: list[str] = []

        for source in self.sources:
            try:
                polls = source.fetch()
            except Exception as exc:
                errors.append(f"{source.name}: fetch failed: {exc}")
                continue

            for poll in polls:
                if self.ledger.has_seen(poll.poll_id):
                    duplicates.append(poll.poll_id)
                    continue
                race_id = self.classifier.classify(poll)
                if race_id is None:
                    unclassified.append(poll.poll_id)
                    continue
                if race_id not in election.races:
                    unknown_race_ids.append(race_id)
                    continue

                try:
                    observation = poll.crosstab.to_observation(
                        adjustment=self.adjustment_by_poll_id.get(poll.poll_id),
                        pollster=poll.pollster,
                        field_date=poll.field_date,
                        extra_variance=self.extra_variance,
                    )
                    election.update(race_id, observation)
                except Exception as exc:
                    errors.append(f"{poll.poll_id}: apply failed: {exc}")
                    continue

                self.ledger.mark_seen(poll.poll_id)
                applied.append(
                    AppliedPoll(
                        poll_id=poll.poll_id,
                        race_id=race_id,
                        pollster=poll.pollster,
                        field_date=poll.field_date,
                    )
                )

        self.ledger.save()
        return IngestionResult(
            applied=tuple(applied),
            duplicate_poll_ids=tuple(duplicates),
            unclassified_poll_ids=tuple(unclassified),
            unknown_race_ids=tuple(unknown_race_ids),
            errors=tuple(errors),
        )


def run_2026_ingestion(
    election: ElectionModel,
    sources: Iterable[PollSource],
    *,
    ledger_path: str | Path = "data/ingestion/2026_seen_polls.json",
    extra_variance: float = 0.0,
) -> IngestionResult:
    """Run the default 2026 poll ingestion automation."""

    pipeline = PollIngestionPipeline(
        sources=tuple(sources),
        classifier=RaceClassifier(RACES_2026_BY_ID),
        ledger=IngestionLedger.load(ledger_path),
        extra_variance=extra_variance,
    )
    return pipeline.run(election)


def _read_text_location(location: str) -> str:
    if location.startswith(("http://", "https://")):
        request = Request(location, headers={"User-Agent": "election-modeling/0.1"})
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")
    return Path(location).read_text()


def _normalize_key(key: object) -> str:
    return str(key).strip().lower().replace(" ", "_").replace("-", "_")


def _required_string(row: Mapping[str, object], key: str) -> str:
    value = _empty_to_none(_string_value(row.get(key)))
    if value is None:
        raise ValueError(f"missing required field: {key}")
    return value


def _string_value(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _empty_to_none(value: str) -> str | None:
    return value if value else None


def _parse_office(value: str | None) -> Office | None:
    if value is None:
        return None
    normalized = value.strip().lower()
    if normalized in {"sen", "senate", "senator"}:
        return "senate"
    if normalized in {"gov", "governor", "gubernatorial"}:
        return "governor"
    raise ValueError(f"unknown office: {value}")


def _find_value(row: Mapping[str, object], *keys: str) -> object | None:
    for key in keys:
        if key in row and _string_value(row[key]) != "":
            return row[key]
    return None


def _parse_share(value: object) -> float:
    text = _string_value(value).replace("%", "").replace(",", "")
    number = float(text)
    if number > 1.0:
        number = number / 100.0
    if not 0.0 <= number <= 1.0:
        raise ValueError(f"share outside [0, 1]: {value}")
    return number


def _parse_int(value: object) -> int:
    text = _string_value(value).replace(",", "")
    number = int(float(text))
    if number <= 0:
        raise ValueError(f"sample size must be positive: {value}")
    return number


def _stable_poll_id(
    *,
    pollster: str,
    field_date: str,
    race_id: str | None,
    state: str | None,
    office: Office | None,
    values: Mapping[PartyID, tuple[float, float]],
    source_url: str | None,
) -> str:
    payload = {
        "pollster": pollster,
        "field_date": field_date,
        "race_id": race_id,
        "state": state,
        "office": office,
        "values": {key: values[key] for key in sorted(values)},
        "source_url": source_url,
    }
    digest = hashlib.sha1(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
    return digest[:16]
