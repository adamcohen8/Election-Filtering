# November 2 polling refresh

**Current user policy (November3): all18 AtlasIntel observations are excluded. The active feed is329 observations.** The acquisition history below describes the source reviews before that exclusion; archives and original review records are retained. See [the exclusion report](../atlas_exclusion_20261103/REPORT.md) for current validation and results.

After the acquisition, the user changed Maine's electorate weights to R31/D28/I41 for Senate and governor. The current model and public exports use those weights. The ingestion manifest records this change relative to the unchanged acquisition baseline.

Added **62 race-level observations from 39 distinct state/national survey waves**, including the scheduled November2 9PM EST increment and November3 scrub, and replaced one revised Florida governor observation. The feed grew from 285 to 347 observations across 28 models. Most new releases are dated November1–2; the recovered Michigan Rasmussen governor release is dated October30; the newly available Iowa Rasmussen Senate page has honest October31–November2 publication bounds because its displayed dateline is stale. All current turnout weights and the 1pp turnout-share marginal SD are preserved.

The scheduled increment added 13 observations from eight surveys after the earlier316-row state. Its detailed source decisions, candidate shares, margins, rolling averages and independent preservation audit are in [the evening report](../poll_check_20261102_2100EST/REPORT.md). All316 earlier normalized rows and all32 earlier raw records/reviews remain exactly preserved.

| Program | New race observations |
|---|---:|
| Research Co. |14|
| InsiderAdvantage |6|
| University of New Hampshire Survey Center |4|
| AtlasIntel |18|
| GrayHouse |2|
| East Carolina University |1|
| YouGov national pre-election study |1|
| Survey 160 |8|
| Rasmussen Reports |6|
| Reuters/Ipsos |1|
| Focaldata/Financial Times |1|

There are 32 new Senate inputs, 26 governor inputs and 4 national generic-ballot inputs. One survey measuring both Senate and governor produces two race observations, not two independent surveys. See [ingestion-manifest.json](ingestion-manifest.json) for exact race counts and [polls.json](polls.json) for cells, dates and table locations. Nebraska increases from 4 to 5; national generic ballot from 23 to 27. Kansas now has11 Senate /9 governor observations after the Atlas addition. The [November3 scrub](../poll_scrub_20261103/REPORT.md) adds18 observations, preserves all329 prior rows, and records the complete current validation and held-source inventory.

## Source review

All additions have all six conditional candidate-support cells within R/D/I groups. Party ID is preferred; Nebraska GrayHouse uses voter-file registration. InsiderAdvantage's unspecified `Party` label is explicitly marked as the previously authorized proxy class. R/D/I support is never reconstructed from sample composition, ideology or recalled presidential vote. Source undecideds/third-party support is not redistributed. All-likely-voter Research Co. tables are selected instead of the adjacent decided-only tables. UNH uses only its ballot including leaners. Alaska InsiderAdvantage uses only first-round support, with Dan S. Sullivan distinguished from the similarly named other Republican; its same-survey RCV alternative/reposts are not added separately.

InsiderAdvantage table images were retrieved from the pollster's own X profile. Signed-in access supplied by the user resolved the separately posted Ohio image. Primary posts: [Georgia](https://x.com/InsiderPolling/status/2117369154638676386), [Alaska](https://x.com/InsiderPolling/status/2117293566951395511), [Minnesota](https://x.com/InsiderPolling/status/2117018158611812417), [Ohio](https://x.com/InsiderPolling/status/2116992824411636158). Georgia's article prints 49.03 for Bottoms while its table prints 49.3; the explicit, internally consistent party table is used and the discrepancy is disclosed in the row. Atlas primary PDFs identify likely voters despite aggregator adult labels. YouGov's national House vote party-ID columns are used, not the adjacent tautological columns defined by House vote itself.

Unknown applicable subgroup Ns remain null, with the established explicit 5pp cell SD and within-pair correlation−.5. Source-reported weighted/uncertain bases are distinguished from raw unweighted Ns. UNH prints design effect `2.4%`/`2.3%`; provisional conservative dimensionless DEFF 2.4/2.3 is used, not a variance-reducing factor. GrayHouse Nebraska's rounded weighted chart bases are noted but are not treated as exact interviews. These are measurement assumptions, not forecast-error calibration.

## Same-wave revision

The current Florida RedBox PDF SHA256 is `6c4d234b6efb22c6bfce2f263f6f64b45e3575049110dbc4f673bfce37b16450`; archived original SHA256 is `ff02d17c7ab60b9a1835d7ac0638da85bdef59186f7d5a98cb7291d329751d77`. Page 18 changes independent Jolly support 55%→56%. Replace `fl_gov--redbox-20261031` while keeping its survey ID, original acquisition identity, pinned predecessor and original artifact. All six Senate support cells are unchanged, so its already-loaded observation stays intact. This is zero additional survey waves. Current Florida release label November 2 differs from the previously recorded November 1 label.

## Coverage and pending sources

The user also reports new Emerson Texas and Ohio polls. The evening review found a November2 Poll Vault briefing lead, but exact survey dates, tested offices and full R/D/I tables remain unverified. The primary Emerson blog still showed October30 releases. This lead remains pending full results, with no new observations added. The evening [held inventory](../poll_check_20261102_2100EST/held-inventory.json) also records unresolved Atlas Ohio, co/efficient Iowa and incomplete/restricted sources.

The user explicitly excluded the new November 1 NYT/Siena Texas Senate screenshot after supplying it. That wave was never ingested and remains excluded; older NYT/Siena waves and Texas governor are unaffected.

[held-sources.json](held-sources.json) records unresolved NYT/Siena access, YouGov state reports without party support columns, incomplete NPA memos, Trafalgar composition-only party pages, Morning Consult 403, and an unverified Concord Ohio report. The new GrayHouse PDFs were recovered through the primary article download buttons; they are now included. Recently indexed older Lake Research/RedBox surveys are not mistaken for newly published waves. The prior NYT/AJC access-policy restrictions were respected; no alternate-copy workaround was used. This search does not establish exhaustive public or private coverage.

[discovery-inventory.json](discovery-inventory.json) retains the current race-index leads. [download-inventory.json](download-inventory.json) and [manual-download-inventory.json](manual-download-inventory.json) pin artifacts and access outcomes. Primary sources and rendered table checks are in `sources/`. No original excluded historical datasets were imported.

## Offline rebuild and verification

```sh
PYTHONPATH=src python scripts/ingest_poll_refresh.py
PYTHONPATH=src python scripts/ingest_poll_refresh.py --check
```

Compilation verifies review hashes, source hashes, matchup, publication eligibility, sample uniqueness, pinned replacements and all six cells before replaying. The full feed is replayed chronologically; the snapshot, ledger, forecasts and history are checked together. Original285 rows are preserved except the explicitly pinned RedBox revision. Every unaffected model must exactly preserve its mean and preserve covariance within1e-15; all turnout assumptions match the current cycle configuration. The manifest separately records the subsequent user-selected Maine weight change relative to the unchanged original acquisition baseline. Older acquisition rebuilds retain the revision, and their audits distinguish new inputs from unintended changes.

Validation results are recorded in `validation.json`. Historical Maine calibration remains unavailable because its excluded original datasets are absent; this refresh makes no empirical calibration claim. The earlier316-row state was published to GitHub. The scheduled evening increment was subsequently published in commit a2c4c6d. The November3 scrub was followed by the user-requested AtlasIntel exclusion; see that report for the current model state.
