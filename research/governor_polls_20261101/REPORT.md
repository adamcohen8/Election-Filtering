# Governor polling acquisition — November 1, 2026

Added **129 reviewed governor survey waves** across all **14 modeled governor races**. They comprise 82 releases in the October 1–November 1 publication window and 47 authorized older backfills. The merged feed has 258 race-specific observations: these 129 governor observations plus the original 129 Senate observations. A paired Senate/governor survey is one wave for each of its separate race questions, not two independent surveys of the electorate.

Ten governor races meet the ten-poll target. Four remain below ten because complete additional candidate-by-party tables were not recovered. Research inventories document the search; they do not establish that every public poll was found.

| State | Accepted waves | Oct 1–Nov 1 releases | Older backfills | Shortfall to ten |
|---|---:|---:|---:|---:|
| [Arizona](az_gov/REPORT.md) | 10 | 7 | 3 | 0 |
| [Florida](fl_gov/REPORT.md) | 11 | 11 | 0 | 0 |
| [Georgia](ga_gov/REPORT.md) | 10 | 3 | 7 | 0 |
| [Iowa](ia_gov/REPORT.md) | 10 | 6 | 4 | 0 |
| [Kansas](ks_gov/REPORT.md) | 7 | 6 | 1 | 3 |
| [Maine](me_gov/REPORT.md) | 10 | 8 | 2 | 0 |
| [Michigan](mi_gov/REPORT.md) | 10 | 5 | 5 | 0 |
| [Minnesota](mn_gov/REPORT.md) | 10 | 4 | 6 | 0 |
| [Nevada](nv_gov/REPORT.md) | 6 | 3 | 3 | 4 |
| [New Hampshire](nh_gov/REPORT.md) | 10 | 3 | 7 | 0 |
| [Ohio](oh_gov/REPORT.md) | 10 | 8 | 2 | 0 |
| [Pennsylvania](pa_gov/REPORT.md) | 5 | 2 | 3 | 5 |
| [Texas](tx_gov/REPORT.md) | 14 | 14 | 0 | 0 |
| [Wisconsin](wi_gov/REPORT.md) | 6 | 2 | 4 | 4 |

## User-supplied NYT/Siena tables

All six governor screenshots enter their own governor models, using the rightmost PARTY ID columns and Republican candidate first. Adjacent Senate-vote columns are not substituted. Dates come from provisional parent-wave metadata; unshown governor subgroup sizes remain null. Iowa/Ohio/Texas/Kansas are treated as the early October wave, Florida/Minnesota as October 28. Florida field-end uncertainty remains labeled. The governor question in these screenshots does not explicitly establish ballot leaner allocation.

| State | Republicans: R candidate / D candidate | Democrats: R candidate / D candidate | Independents: R candidate / D candidate |
|---|---|---|---|
| Florida: Donalds / Jolly | 91 / 6 | 4 / 93 | 35 / 52 |
| Iowa: Lahn / Sand | 84 / 9 | 2 / 98 | 31 / 59 |
| Ohio: Ramaswamy / Acton | 89 / 9 | 3 / 91 | 41 / 50 |
| Texas: Abbott / Hinojosa | 88 / 8 | 3 / 94 | 39 / 55 |
| Kansas: Masterson / Holscher | 84 / 10 | 5 / 92 | 36 / 53 |
| Minnesota: Demuth / Klobuchar | 94 / 4 | <0.5 / 97 | 35 / 57 |

Percentages above are source values. Minnesota’s censored Republican-support cell among Democrats is represented by a labeled 0.25% midpoint with additional interval variance, not zero. Maine Marist October 27 similarly reports Charles <1% among Democrats; that separate source uses a labeled 0.5% midpoint. Original intervals remain inspectable in the raw and normalized records.

## Rules and precision

Publication date controls the initial window, including September fieldwork first released in October. For sub-ten races, older verified waves are selected newest publication first toward ten. All recovered complete in-window waves are retained even when a race exceeds ten. One population/ballot version per survey and race enters. Exact current candidate pairs are required; topline-only, ideology-only, incomplete R/D/I tables, different candidate pairs and fabricated Wedgewood polls do not enter. Alaska governor stays excluded by the user’s decision.

Straight party identification is preferred when available. Registration, modeled party, unspecified party and broad independent/other proxies are labeled under the user’s previously authorized inclusion rules. Party leaner treatment is preserved; it is not uniform across publishers. This is a material comparability limitation. Third candidates and undecideds remain outside the two candidates’ shares, without renormalization.

The measurement precision policies remain provisional: DEFF1.5 for unweighted bases, DEFF2 for weighted/unspecified bases, DEFF3 for total-times-rounded-share estimates, with larger source-informed effects where required. Fifty-seven waves use explicit assumed covariance (5pp cell SD, within-group correlation -0.5) in place of unsupported denominator precision. Unknown source subgroup counts remain null. Counts and assumptions are separately retained. These choices do not constitute empirical calibration.

Minnesota governor was missing from the registry and is added as Lisa Demuth versus Amy Klobuchar with the user’s R34/D37/I29 shares. Other electorate shares remain unchanged. Every race retains the requested 1pp one-sigma / 3pp three-sigma marginal turnout-share uncertainty and the sum-to-one constraint.

## Remaining sources where user help could close gaps

- **Pennsylvania (5):** the previously identified [September NYT/Inquirer/Siena likely-voter crosstab link](https://www.nytimes.com/interactive/2026/09/24/polls/times-inquirer-siena-pa-poll-lv-crosstabs.html) was not retrieved in this run. The governor rows by party, with field dates and publication date, would add a wave. Bravo’s dashboard yielded only the Republican group (Garrity56/Shapiro24), so it is not sufficient. F&M’s inspected summaries and attached tables lacked the governor party ballot.
- **Georgia (10; target met):** the user supplied the [AJC/UGA October source](https://www.documentcloud.org/documents/28824163-ajc-poll-october-2026-1/?mode=text) governor party table directly. Jackson/Bottoms R93.5/1.6, D4.3/93.4, I38.2/42.9 are included; unshown subgroup Ns stay null with existing assumed measurement covariance. Direct browser access remained blocked and no workaround was used. Separate [InsiderAdvantage September release](https://insideradvantage.com/insideradvantage-georgia-survey-jackson-leads-by-two-in-race-for-governor-ossoff-leads-by-eight-in-senate-contest/) and October governor party charts were not located. Its August chart and September Big Data Poll are included. ActiVote explicitly publishes no Georgia party table.
- **Kansas (7):** GSG September/October and additional older governor tables remain unresolved. Kansas Speaks explicitly withholds Q23 governor results, so no governor cells are inferred from it.
- **Nevada (6):** Hart, GSG, Concord and other campaign surveys had toplines or offered crosstabs on request; no complete public six-cell table was recovered.
- **Wisconsin (6):** City Forward/YouGov, Z to A/Rust Belt Rising and RMG sources did not yield the six governor party cells. Marquette’s generic state-legislature table is not a governor poll. Three Marquette waves, two TIPP waves and Wick’s October wave are included.

Arizona ASU’s six cells remain in raw research but are **held**: its first-publication bounds span September 4–October 6 and cannot establish cutoff eligibility or backfill rank. Arizona has ten other confirmed waves. Newer unrecovered tables may change which older backfills are needed.

## Source conflicts retained

Arizona KStrat/American Encore and Georgia Quantus August contain inconsistencies between party-weighted recompositions and narrative toplines. The original six conditional cells are retained and the conflicts are labeled; reported totals and party percentages are not silently repaired. Quantus August uses conservative assumed covariance rather than its uncertain weighted bases. State Navigate’s Georgia October workbook Note gives N741 while the governor table and release give N679; the actual governor table’s bases are retained. Maine UNH has a lieutenant-governor wording typo despite its governor heading, narrative and candidate pair, recorded in its row. Ohio Suffolk September has a chronology/content anomaly noted for review.

## Verification

The offline audit checks all 129 raw-record review hashes and 114 distinct evidence artifacts, full chronological replay, model snapshot, ingestion ledger, public forecasts and every history/rolling-average value. All 129 Senate feed rows are byte-for-value unchanged; Senate filter means are unchanged and covariance comparisons pass at 1e-15 tolerance. At the governor acquisition there were 27 registered models (14 governor, 12 Senate, one prior-only national generic ballot). The subsequent Nebraska addition is audited separately under research/nebraska_senate_polls_20261101/.

Validation: **98 Python tests passed**, excluding only the historical Maine calibration module that requires the deliberately unimported original datasets; **4 UI tests passed**; JavaScript syntax and whitespace checks passed. No historical forecast accuracy or interval-coverage claim follows from these checks.

Reproduce without network:

```bash
python scripts/ingest_governor_research.py --check
python research/governor_polls_20261101/verification/validate.py
python research/senate_polls_20261101/verification/validate.py
```

Per-row acceptance/hold reasons and precision choices: [review-decisions.json](review-decisions.json). Rebuild manifest: [ingestion-manifest.json](ingestion-manifest.json). Audit output: [verification/validation.json](verification/validation.json). Raw per-race inventories and source originals are retained alongside each report. No commit, push or deployment was performed.
