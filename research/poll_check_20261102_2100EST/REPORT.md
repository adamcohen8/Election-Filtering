# Scheduled polling update — November 2, 2026, 9PM EST

Added **13 observations from eight newly verified survey waves**: six Senate, five governor, and two national generic-ballot inputs. The feed grows **316 → 329** across the same28 models. All previous316 normalized rows, current user-selected electorate weights (including Maine R31/D28/I41), model assumptions and margin-based ratings are preserved. Alaska governor and the user-excluded November1 NYT/Siena Texas Senate wave remain excluded. Nebraska still uses independent Dan Osborn.

The scheduled run prepared this update locally. Subsequent GitHub publication and deployment are a separate user-authorized step. The one-time scheduled check has completed and its automation was deleted successfully; unresolved source tables remain held.

## Accepted original sources

- [Survey 160 four-state study](https://www.survey160.com/methodological-research-blog/survey-160-pre-election-surveys-in-four-states), released November2, fielded October27–November1: Kansas, Ohio, Maine and Minnesota, each Senate and governor (eight observations/four surveys). Use full registered-voter first-choice Party ID tables and exact unweighted subgroup bases. The adjacent LV headline and leaned ballots are different selections, not extra waves. State-wide reported design effects1.78/3.63/2.30/2.04 are provisionally applied to subgroups.
- [Reuters/Ipsos](https://www.ipsos.com/en-us/reutersipsos-early-november-survey), November2 release, October29–November2 fieldwork: one national LV generic ballot including candidate leaners. Use applicable bases R413/D421/I378; retain conservative DEFF1.5 instead of reducing it to the source-wide1.03.
- [Focaldata/Financial Times](https://www.focaldata.com/blog/democrats-lead-by-7-points-in-final-focaldata-ft-midterms-poll), November2 release, October30–November1 fieldwork: one all-adult first-choice national ballot. Pool strong/not-strong R and D identifiers; retain partisan leaners with independents, matching prior Focaldata handling. Exact weighted support counts/bases determine support, raw Ns916/771/646 determine measurement bases, with existing provisional DEFF2.0. Unknown-party respondents remain outside the groups.
- [Rasmussen Ohio Senate public table](https://www.rasmussenreports.com/public_content/politics/public_surveys/crosstabs_2_ohio_senate_october_27_31_2026), November2 release, October27–31 fieldwork: one Senate observation. Separate Independent from Another party.
- [Rasmussen Iowa Senate](https://www.rasmussenreports.com/public_content/politics/elections/election_2026/election_2026_iowa_senate) and [Iowa governor](https://www.rasmussenreports.com/public_content/politics/elections/election_2026/election_2026_iowa_governor), October27–31 fieldwork, n901: two office observations from one survey. Public narrative supplies all six support cells. The Senate page has a stale October2 dateline before fieldwork; first publication is honestly bounded October31–November2 instead of inventing an exact date. The governor release is dated November2. All three Rasmussen observations retain unspecified party-classification proxies and null subgroup Ns, using the established explicit5pp cell SD and−.5 within-pair correlation. No premium content was bypassed.

The publication eligibility start for the combined November2 acquisition is widened from November1 to October31 solely to accommodate the honest Iowa Senate publication bounds. The original32 raw records and decisions remain identical. No additional historical backfill was performed.

## Updated results

Kalman estimates below project to November3. Rolling averages are equal-weight means of the latest seven accepted polls, using available polls when fewer exist. Candidate shares are electorate-adjusted, with residual undecided/other support retained; no hypothetical party-based undecided allocations are applied. Margins use unrounded underlying shares and can differ slightly from subtraction of rounded displayed shares.

| Race | Republican | Opponent | Kalman R share | Kalman opponent share | Kalman margin | Previous margin | 7-poll R share | 7-poll opponent share | 7-poll margin |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Iowa Governor | Zach Lahn | Rob Sand | 44.32% | 50.11% | D+5.78 | D+6.70 | 43.26% | 50.86% | D+7.61 |
| Iowa Senate | Ashley Hinson | Josh Turek | 46.64% | 47.06% | D+0.42 | D+1.27 | 46.74% | 45.95% | R+0.79 |
| Kansas Governor | Ty Masterson | Cindy Holscher | 50.99% | 44.88% | R+6.10 | R+4.07 | 49.61% | 45.22% | R+4.39 |
| Kansas Senate | Roger Marshall | Adam Hamilton | 46.25% | 46.01% | R+0.24 | D+0.54 | 46.24% | 47.17% | D+0.93 |
| Maine Governor | Bobby Charles | Hannah Pingree | 42.48% | 48.87% | D+6.40 | D+4.25 | 40.19% | 48.14% | D+7.95 |
| Maine Senate | Susan Collins | Troy Jackson | 47.94% | 49.32% | D+1.38 | R+0.24 | 48.10% | 47.69% | R+0.41 |
| Minnesota Governor | Lisa Demuth | Amy Klobuchar | 43.06% | 50.73% | D+7.67 | D+8.70 | 41.90% | 49.75% | D+7.85 |
| Minnesota Senate | Michele Tafoya | Peggy Flanagan | 45.82% | 48.66% | D+2.84 | D+2.49 | 44.72% | 48.00% | D+3.28 |
| Ohio Governor | Vivek Ramaswamy | Amy Acton | 46.82% | 47.79% | D+0.97 | D+0.52 | 46.69% | 46.85% | D+0.16 |
| Ohio Senate | Jon Husted | Sherrod Brown | 47.58% | 46.72% | R+0.85 | R+1.39 | 46.95% | 45.57% | R+1.37 |
| United States generic ballot | Generic Republican | Generic Democrat | 44.75% | 49.10% | D+4.35 | D+5.76 | 44.20% | 49.24% | D+5.04 |

Full before/after values, statuses, counts and rolling-window poll IDs: [results.json](results.json). New source records and per-record hashes: [new-records.json](new-records.json), [new-review-decisions.json](new-review-decisions.json). The main acquisition raw files are updated together so `scripts/ingest_poll_refresh.py` remains the owner of deterministic replay.

## Source gaps and sanitation

[held-inventory.json](held-inventory.json) preserves earlier exclusions and records the new Emerson/Poll Vault briefing lead, Atlas Ohio, co/efficient Iowa, incomplete Rasmussen generic ballot, restricted Rasmussen Michigan governor, and other unresolved original tables. Composition-only tables and toplines do not satisfy the six-cell requirement. Prior NYT/AJC access restrictions were respected, with no alternate-copy attempts. The explicitly excluded new Texas Senate NYT wave remains excluded. Research Co., Emerson, Quantus and other recent wave leads were compared with already accepted observations rather than counted again. This is not proof of exhaustive public/private coverage.

[download-inventory.json](download-inventory.json) logs sandbox network failures followed by authorized ordinary public-source downloads, source links, byte counts and original/sanitized SHA256 values. All12 archived primary/source-discovery artifacts pass hash checks and credential-pattern scanning; the scan also examines uncompressed XLSX XML. **No copied credential patterns were found, so no new sanitation was required (zero redactions).** Previously sanitized materials remain preserved.

## Validation

- 103 applicable Python tests and six UI tests passed; intentionally absent historical Maine calibration datasets remain excluded.
- All five acquisition `--check` commands and both historical Senate/governor provenance audits passed.
- Snapshot, seen-poll/fingerprint ledger, public forecasts and public history agree with complete chronological replay.
- All316 previous input rows and original32 November2 raw records/reviews are exactly preserved. All17 races with no new observations preserve their conditional means exactly and covariance within1e-15. All28 current electorate weights and static model settings are unchanged.
- An independent audit recomputed every latest rolling average from its constituent public poll points; no duplicate poll IDs or same-race survey waves exist.
- [validation.json](validation.json) and [source-artifact-hashes.json](source-artifact-hashes.json) provide the machine-readable checks. No empirical forecasting-calibration claim is made.

Reproduce offline:

```sh
.venv/bin/python research/poll_check_20261102_2100EST/prepare_records.py
PYTHONPATH=src .venv/bin/python scripts/ingest_poll_refresh.py --check
PYTHONPATH=src .venv/bin/python research/poll_check_20261102_2100EST/validate.py
```
