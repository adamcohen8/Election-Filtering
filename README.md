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

## Local Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q --ignore=tests/test_maine_calibration.py
node --test tests/test_public_ui.cjs
python scripts/ingest_senate_research.py --check
python research/senate_polls_20261101/verification/validate.py
```

The Maine calibration tests require historical datasets intentionally absent
from this checkout. The remaining tests run with the declared NumPy and pytest
dependencies. The UI checks use Node's built-in test runner.

## Seven-poll rolling average

Every race's history export includes a seven-poll rolling average beside the
Kalman history. Each poll has equal weight, regardless of sample size or age.
The window uses the latest seven accepted, deduplicated polls ordered by
field-end date and then poll ID. With fewer than seven, it uses all available
polls. Polls on the same day each count toward the window; the chart shows the
final window for that day.

Crosstab polls use the same electorate-adjusted candidate shares as the poll
markers; topline polls use their reported shares. The averages use those
exported shares, rounded to four decimal places. The race page shows the latest
average, poll count, date range, and dashed candidate lines. Races without polls
show “Awaiting polls.” This descriptive average has no uncertainty interval or
Election Day projection. In `docs/data/race-history.json`, each race exposes
`rolling_average_window`, `rolling_average_points`, and the latest
`rolling_average` (null with no polls).

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

## Filtering methodology

The filter uses dated constrained-Gaussian updates, persistent polling-error
terms, and uncertainty in the R/D/I electorate weights. The requested turnout
allowance is three percentage points at three sigma (one-point marginal SD).
See [methodology version 2](METHODOLOGY.md) for equations, configurable
assumptions, snapshot replay requirements, and verification limits.

## 2026 race coverage

Candidate audit checked November 1, 2026. The registry includes 13 U.S. Senate
races (including the Florida and Ohio special elections), 14 governor races,
and the national generic congressional ballot. It covers the 17 states with
built-in electorate weights. Alaska governor is excluded at the user's request
because the general election has multiple Republican finalists.

Each matchup below lists the Republican first and the opponent second. Nebraska's
opponent is independent Dan Osborn. The
state links provide the candidate verification sources; the source URLs and
verification dates are also recorded in `src/election_modeling/nominees.py`.
The model forecasts each listed pair. Other candidates remain outside the
two-candidate model; their support is not redistributed to the modeled pair.

| State | U.S. Senate: Republican / Democrat | Governor: Republican / Democrat |
| --- | --- | --- |
| [Alaska](https://apnews.com/article/412ea91b906a29c038b5d2cc6e7b93d1) | Dan Sullivan / Mary Peltola | Excluded by request |
| [Arizona](https://apnews.com/article/42fd6bfa4d9010786e8af5ec9892be95) | No 2026 election | Andy Biggs / Katie Hobbs |
| [Florida](https://apnews.com/article/4e7c37012dae6fdb2427de8d1b222a4c) | Ashley Moody / Angie Nixon (special) | Byron Donalds / David Jolly |
| [Georgia](https://apnews.com/article/e8b4d650269102ad4723a5a162a24cf4) | Mike Collins / Jon Ossoff | Rick Jackson / Keisha Lance Bottoms |
| [Iowa](https://apnews.com/article/2e005b6badba2d106c43ce5bc25d07fc) | Ashley Hinson / Josh Turek | Zach Lahn / Rob Sand |
| [Kansas](https://apnews.com/article/eef95708ad9460def594935ac301c4f5) | Roger Marshall / Adam Hamilton | Ty Masterson / Cindy Holscher |
| [Maine](https://apnews.com/article/0738e23c17299037479d9807d7f7bb62) | Susan Collins / Troy Jackson | Bobby Charles / Hannah Pingree |
| [Michigan](https://apnews.com/article/ef0c10050672e639203efdc64d2b59f5) | Mike Rogers / Abdul El-Sayed | John James / Jocelyn Benson |
| [Minnesota](https://apnews.com/article/0ad3241b58ecc7fa2ca1693bbd2f4013) | Michele Tafoya / Peggy Flanagan (DFL) | Lisa Demuth / Amy Klobuchar (DFL) |
| [Nebraska](https://apnews.com/article/78b5008f5c41597306574eccabec630f) | Pete Ricketts / Dan Osborn (Independent) | Not added |
| [Nevada](https://www.multistate.us/elections/governor-race/nevada-2026) | No 2026 election | Joe Lombardo / Aaron Ford |
| [New Hampshire](https://apnews.com/article/b7e739aba1fe5f0525e55b973000cc1a) | John E. Sununu / Chris Pappas | Kelly Ayotte / Cinde Warmington |
| [North Carolina](https://apnews.com/article/5a8ec7df25bf8ee18df535bf8eeb2b0d) | Michael Whatley / Roy Cooper | No 2026 election |
| [Ohio](https://apnews.com/article/edfb7e19f15c21bf6d1a1a785042c977) | Jon Husted / Sherrod Brown (special) | Vivek Ramaswamy / Amy Acton |
| [Pennsylvania](https://apnews.com/article/2b3e8b883d526a59c979a09581cb09f5) | No 2026 election | Stacy Garrity / Josh Shapiro |
| [Texas](https://apnews.com/article/04e87ff214dc580d4dc6751644fdc467) | Ken Paxton / James Talarico | Greg Abbott / Gina Hinojosa |
| [Wisconsin](https://apnews.com/article/b6fc54862bb0364082fd60a6b02b59fd) | No 2026 election | Tom Tiffany / David Crowley |

The calendar was cross-checked against the
[U.S. Senate election-class listing](https://www.dailypress.senate.gov/on-the-floor/senate-facts/)
and [National Governors Association election calendar](https://www.nga.org/governors/elections/).
Troy Jackson is the confirmed Maine Democratic Senate nominee following the
July replacement convention; his previous presumptive status has been updated.

## GitHub Pages

The November 2 refresh adds 31 race observations from 20 new surveys:
16 Senate, 13 governor and two national generic-ballot inputs. One existing
Florida RedBox governor observation is revised in place. The combined feed now
contains 316 observations across 28 models; Nebraska has five and the national
generic ballot has 25. Current turnout weights are preserved. Source records,
pending tables and validation are in
[`research/poll_refresh_20261102/REPORT.md`](research/poll_refresh_20261102/REPORT.md).
Rebuild or verify the current refresh with
`python scripts/ingest_poll_refresh.py` and its `--check` option.

The original November 1 national generic House acquisition included 23 reviewed
October-window waves from 14 pollster programs, using R37/D33/I30. No older backfill was needed.
It brought the combined feed to 285 observations across 28 models. Voter populations,
party proxies, missing-base precision and unrecovered tables are documented in
`research/generic_ballot_polls_20261101/REPORT.md`. Rebuild or verify with
`python scripts/ingest_generic_ballot_research.py` and its `--check` option.

The November 1 Senate acquisition includes 129 reviewed distinct survey waves.
The original 96 published October 1 through November 1 remain unchanged. At the
user's request, 33 older qualifying waves were added for the nine races below
10 polls. Eleven Senate races now have at least 10 polls; Kansas has 9 because
one more complete R/D/I ballot table could not be verified. Alaska and Georgia
include older 2025 hypothetical matchups of the same current candidates.

All seven user-supplied NYT/Siena state tables and the Washington Post/Schar
Maine and Kansas tables are included. Source-specific party definitions,
weighted/estimated counts, provisional dates and missing-count uncertainty remain
labeled. Minnesota uses R34/D37/I29 and had ten accepted waves at that acquisition. Newer
unrecovered tables and the remaining Kansas gap are documented in the research
audit. The Senate acquisition is preserved separately from governor polling.

Nebraska Senate was a separate addition with four complete party-table waves:
On Point October 30, SurveyUSA September 14, Tavern May 11 and Lake Research
January 22 (December 2025 fieldwork). Its
R57/D24/I19 electorate is user-selected. On Point's
registration groups and modeled allocation of undecideds are explicitly labeled;
the other three waves are older backfills. Six more eligible tables were not
located. Dan Osborn is labeled Independent, with no Democratic caucus affiliation
assigned. The previous 258 input rows and 27 race states are preserved. This
brought the feed to 262 observations across 28 models before the generic ballot addition. See
`research/nebraska_senate_polls_20261101/REPORT.md` for evidence and limitations.

The November 1 governor acquisition added 129 reviewed waves across all 14 governor races,
including the six user-supplied NYT/Siena governor tables and the user-supplied AJC Georgia table. Ten races meet the
ten-poll target: Texas has 14, Florida 11, and Arizona, Iowa, Maine, Michigan,
Minnesota, New Hampshire, Ohio and Georgia have 10 each. Kansas has 7,
Nevada and Wisconsin 6 each, and Pennsylvania 5. Complete party tables for
additional sources could not be recovered; the source gaps are recorded in
`research/governor_polls_20261101/REPORT.md`. One ASU Arizona record is held
because its first-publication bounds cross the October 1 cutoff. Older waves
fill only races below ten, and alternate ballot/population versions do not
count as separate polls. Minnesota governor uses the user's R34/D37/I29 shares.

The normalized input is `data/ingestion/2026_normalized_polls.json`; the replayed
model is `data/models/2026_election_model.json`. Source inventories, original
tables, per-record review decisions, precision assumptions and exclusions are in
`research/senate_polls_20261101/`. Weighted bases, rounded-composition estimates
and published subgroup-size lower bounds are labeled separately from reported
unweighted interview counts. For twenty-four waves, explicit assumed measurement
covariance replaces an unavailable subgroup-count calculation; unknown counts
remain null. Same-wave population and ballot alternatives are
not counted twice. The original repository's excluded datasets were not imported
into the models.

Validate or rebuild this reviewed acquisition locally, without network access:

```bash
python scripts/ingest_senate_research.py --check
python scripts/ingest_senate_research.py
python scripts/ingest_governor_research.py --check
python scripts/ingest_governor_research.py
python research/governor_polls_20261101/verification/validate.py
python scripts/ingest_nebraska_research.py --check
python scripts/ingest_nebraska_research.py
```

The importer verifies record hashes, publication eligibility, candidates, all
three party groups, measurement uncertainty and duplicate survey versions before replaying
chronologically. It preserves unrelated feed rows and rebuilds the snapshot,
ledger, static forecasts and history together after successful validation.

The public map lives in `docs/` so GitHub Pages can serve it from the repository
without a build step. It reads `docs/data/forecasts.json`, which is generated
from the current model snapshot.

```bash
python scripts/export_public.py
```

The page includes Senate and Governor tabs, a geographic 50-state interactive
map, modeled race coloring, and a race detail panel.
