# Election Modeling

A small Python library for modeling two-candidate election races from noisy poll
cross-tabs.

The core model treats each race as six latent support states:

- Republican party-ID voters supporting candidate A
- Republican party-ID voters supporting candidate B
- Democratic party-ID voters supporting candidate A
- Democratic party-ID voters supporting candidate B
- Independent voters supporting candidate A
- Independent voters supporting candidate B

Polls are noisy observations of those latent states. The library uses a Kalman
filter to update the race estimate, then combines the filtered support estimates
with a predicted electorate to produce a margin and uncertainty interval.

## Quick Start

```python
from election_modeling import (
    Electorate,
    PollObservation,
    create_2026_election_model,
)

election = create_2026_election_model(
    {
        "fl_sen": Electorate(republican=0.36, democratic=0.34, independent=0.30),
        "nc_gov": Electorate(republican=0.37, democratic=0.33, independent=0.30),
    }
)

poll = PollObservation.from_party_id_shares(
    values={
        "republican": (0.88, 0.08),
        "democratic": (0.06, 0.91),
        "independent": (0.47, 0.44),
    },
    subgroup_sample_sizes={
        "republican": 320,
        "democratic": 310,
        "independent": 260,
    },
)

election.update("fl_sen", poll)
forecast = election.forecast("fl_sen")

print(forecast.margin)
print(forecast.margin_of_error)
```

Positive margins mean candidate A leads candidate B.

## Poll Ingestion Automation

The IO layer separates source-specific scraping from model updates. A source
adapter returns normalized party-ID cross-tabs, then the ingestion pipeline:

1. classifies each poll into a race ID
2. skips duplicate poll IDs
3. converts party-ID rows into `PollObservation` objects
4. updates each race's Kalman filter

```python
from election_modeling import (
    NormalizedPoll,
    PartyIDCrosstab,
    StaticPollSource,
    create_2026_election_model,
    run_2026_ingestion,
)

election = create_2026_election_model()
source = StaticPollSource(
    [
        NormalizedPoll(
            poll_id="example-fl-sen-2026-01",
            pollster="Example Polling",
            field_date="2026-03-15",
            race_id="fl_sen",
            crosstab=PartyIDCrosstab(
                values={
                    "republican": (0.88, 0.08),
                    "democratic": (0.07, 0.90),
                    "independent": (0.48, 0.44),
                },
                subgroup_sample_sizes={
                    "republican": 350,
                    "democratic": 330,
                    "independent": 280,
                },
            ),
        )
    ]
)

result = run_2026_ingestion(election, [source])
print(result.applied)
```

For web feeds that already expose normalized rows, use `StructuredCSVSource` or
`StructuredJSONSource`. Pollster/PDF-specific scrapers can be added as new
`PollSource` adapters without changing the Kalman filter code.

For a recurring job, use `run_2026_poll_io(...)`. It loads the last saved model
snapshot, ingests new polls, updates the filters, saves the model state, and
tracks already-seen poll IDs.

```python
from election_modeling import run_2026_poll_io

run = run_2026_poll_io(
    csv_sources=["https://example.com/normalized-party-id-polls.csv"],
    snapshot_path="data/models/2026_election_model.json",
    ledger_path="data/ingestion/2026_seen_polls.json",
)

print(run.result.applied)
```

## GitHub Pages

The public map lives in `docs/` so GitHub Pages can serve it from the repository
without a build step. It reads `docs/data/forecasts.json`, which is generated
from the current model snapshot.

```bash
python scripts/export_public.py
```

The page includes Senate and Governor tabs, a geographic 50-state interactive
map, modeled race coloring, and a race detail panel.
