# Senate polling acquisition — November 1, 2026

Loaded **96 distinct reviewed survey waves into all 12 Senate models**, up from the initial 49. The user instructed reopening exclusions for modeled or unspecified party classification, uncertain subgroup counts, and previously inaccessible reports, and expressly retained the October 1 publication cutoff. The reopening added **33 waves**, including all six in-window Quantus reports and four newly recovered CNN/SSRS reports. A subsequent search recovered **7 separately posted InsiderAdvantage crosstabs**, making the increase **40 waves**. Seven user-supplied NYT/Siena tables (Alaska, Ohio, Texas, Kansas, Iowa, Florida, Minnesota) then brought the total increase to **47 waves**. This is documented search coverage, not proof that every public poll was found.

The original race subreports preserve first-pass findings and statuses. The current controlling records are `review-decisions.json`, `ingestion-manifest.json`, the `reopened_*` source packages, and `user_supplied_nyt/`. The initial decisions/manifest and forecast summary are archived in `reopened_revision/`.

The user confirmed **publication date** determines eligibility: October 1 through November 1, 2026 inclusive. The model uses **field-end date** for chronology. Accepted fieldwork ends range from September 22 to October 31. Three publication dates are bounded inside the window rather than known exactly: early New Hampshire Rasmussen, A2 Texas, and NYT/Siena Alaska (October 3–4). First-choice ballots are preferred; candidate-leaner ballots are used where the selected source provides them. Same-wave LV/RV, party-basis and ballot variants are counted once.

Minnesota uses **R34/D37/I29**, with **Michele Tafoya (R) / Peggy Flanagan (DFL)**, verified against the Minnesota Secretary of State primary results. It now has six accepted waves: Big Data Poll, two SurveyUSA waves, two reopened Rasmussen waves, and NYT/Siena. Governor polling is outside this Senate acquisition.

| Senate race | Initial | Added | Now loaded |
| --- | ---: | ---: | ---: |
| Florida | 7 | 2 | 9 |
| Texas | 8 | 12 | 20 |
| Georgia | 1 | 1 | 2 |
| Maine | 6 | 4 | 10 |
| New Hampshire | 3 | 3 | 6 |
| Iowa | 5 | 2 | 7 |
| Alaska | 0 | 3 | 3 |
| Michigan | 5 | 4 | 9 |
| Ohio | 5 | 5 | 10 |
| North Carolina | 4 | 3 | 7 |
| Kansas | 2 | 5 | 7 |
| Minnesota | 3 | 3 | 6 |
| **Total** | **49** | **47** | **96** |

Of the 19 originally held records, 14 are now included; 33 newly recovered records bring the increase to 47. Five reviewed records remain unselected: four same-survey alternatives and a Suffolk Ohio Senate result first published September 30. The September 30 Quantus Iowa release also remains outside the window in the broader inventory. Remaining unreadable or incomplete tables cannot supply invented R/D/I cells. NYT/Siena access limitations remain documented in the source inventories. Wedgewood remains excluded as fabricated.

Newly included polling teams/waves: NYT/Siena (7), InsiderAdvantage (7), Quantus (6), Rasmussen (12), CNN/SSRS (4), Washington Post/Schar (2), UT/YouGov (1), UMass Lowell/YouGov (2), ReconMR/Siena (1), BGSU/YouGov (1), A2 Insights (1), Pollfinity (1), ActiVote (1), and ECU (1).

## Follow-up source searches

Washington Post/Schar's complete Maine (October 9) and Kansas (October 30) party tables were already loaded in the 82-wave revision and remain included. No additional qualifying statewide Senate wave was found in the focused follow-up. See `reopened_wapo/REPORT.md`.

InsiderAdvantage publishes tables separately from toplines. Seven complete original charts were recovered, visually checked, and ingested: Ohio October 1; Kansas October 11 and 15; Maine and Texas October 15; Michigan October 23; Florida October 30. These dates are publication dates, not field-end dates. Reported subgroup bases are retained; the source's unspecified party classification and count-weighting status remain labeled. Six other identified in-window InsiderAdvantage waves still lack verified complete tables in this acquisition; this does not establish that their tables are unavailable. See `reopened_insider_revision/REPORT.md`.

The user reaffirmed that all R/D/I candidate crosstabs remain required. Echelon's state toplines and co/efficient's candidate toplines plus party composition do not supply verified conditional candidate support by party; neither was added. See their respective `reopened_*` reports.

Siena's primary releases link seven NYT/Siena state tables (October 3: AK, IA, KS, OH, TX; October 28: FL, MN). A fresh root browser attempt was explicitly blocked by site-safety policy and the tool prohibited workaround access; no permission or automatic-approval review was attempted. The user subsequently supplied Alaska, Ohio, Texas, Kansas, Iowa, Florida and Minnesota screenshots. Six use null subgroup Ns and the existing assumed covariance; Iowa uses fully visible reported counts R199/D163/I223 with weighting unspecified and working design effect 2. Kansas includes third-party candidates, and its major-party percentages are not rescaled. Field-end metadata remain provisional from the prior inventories because the screenshots omit methodology. All seven requested NYT/Siena state tables are now included. Florida chronology provisionally uses October 26 within conflicting October 25–26 field-end bounds pending methodology. See `user_supplied_nyt/REPORT.md`. No NYT image was generated. The separately published ReconMR/Siena Texas poll is already included and is a different survey. See `reopened_nyt_early/REPORT.md`, `reopened_nyt_other/REPORT.md`, and `reopened_nyt_other/root-access-check.txt`.

## Party measures and precision

Of the loaded waves, **56 use party identification, 13 party registration, 5 modeled party affiliation, 21 unspecified or ambiguous party classification, and 1 model-derived subgroup predictions**. Unleaned ID is preferred where a source offers it. Some tables include partisan leaners or pool other parties with independents. These definitions and source wording remain attached to observations. Proxy inclusion requires an explicit review authorization and remains labeled in the feed and public-history metadata. These measures are not perfectly interchangeable.

Model subgroup-base methods are:

| Method | Waves |
| --- | ---: |
| Reported unweighted interviews | 16 |
| Reported weighted bases | 13 |
| Reported bases, weighting status unspecified | 17 |
| Reported effective subgroup sizes | 1 |
| Estimates from matching total × rounded party composition | 23 |
| Published suppression threshold used as a nominal lower bound | 12 |
| Explicit assumed covariance; no invented subgroup counts | 14 |

The last three categories are **not reported subgroup interview counts**. Exact source bases, rounded composition, size bounds and precision choices are preserved separately. Fractional bases are floored where integer model inputs are used. For the fourteen direct-covariance waves, unknown subgroup counts stay null; there is no implied synthetic N. These waves use an explicit working assumption of **5 percentage points SD per candidate/group share**, with within-group correlation -0.5 and zero measurement correlation across groups. This is about 8.66 points SD for a within-group candidate margin, before the other persistent-error components. It is not an empirically calibrated error bound and is separate from turnout uncertainty.

NYT/Siena Minnesota's `<0.5%` Tafoya-among-Democrats cell uses an explicitly labeled 0.25% midpoint with added variance equal to the squared 0.25-point half-width; the original censored interval remains preserved.

ECU's `<1%` Whatley-among-Democrats cell uses an explicitly labeled 0.5% midpoint with additional variance equal to the squared 0.5-point half-width. The raw interval remains recorded; the source is not represented as publishing an exact 0.5% or zero. Texas Marist still uses its complete RV alternative once. A2's subgroup percentages are model-produced predictions rather than raw subgroup response percentages; Pollfinity's percentages are responses grouped by modeled voter-file party. Those different source methods are retained.

Working design effects are 1.5 for unweighted bases, 2 for weighted or unspecified bases, and 3 for composition estimates, subgroup-size bounds and the newly reopened Quantus/Pollfinity tables, with source-informed larger adjustments where appropriate. Reported effective sizes use factor 1. Direct covariance also uses factor 1 because its measurement error is already specified. These factors are provisional assumptions. Source-reported RedBox weighting effects and checked subgroup MOEs inform its precision. Primary tables are used when narrative summaries conflict, with source discrepancies retained rather than claimed resolved. Details are in `verification/NOTES.md`, `reopened_revision/REPORT.md` and `review-decisions.json`.

The requested turnout uncertainty remains **1 percentage point at one sigma, or 3 points at three sigma**, for each R/D/I share, with the sum-to-one covariance constraint. This acquisition preserves the existing persistent shared/pollster/survey error model.

## Files and reproduction

- Input: `data/ingestion/2026_normalized_polls.json`.
- Replayed snapshot and ledger: `data/models/2026_election_model.json`, `data/ingestion/2026_seen_polls.json`.
- Local static forecast/history: `docs/data/forecasts.json`, `docs/data/race-history.json`.
- Source inventories, transcriptions and originals: each race subdirectory, with additional centrally checked PDFs in `verification/sources/`.
- Central acceptance and provenance: `review-decisions.json`, `ingestion-manifest.json`.

Run from the repository root, with its Python dependencies installed:

```bash
python scripts/ingest_senate_research.py --check
python scripts/ingest_senate_research.py
python research/senate_polls_20261101/verification/validate.py
```

The importer is offline and checks source-record hashes, publication eligibility, named candidates, all three party groups, precision inputs and duplicate survey versions. It replays the merged feed globally in field-date order and validates forecast/history generation before writing outputs. No original excluded repository datasets were imported. No commit, push or deployment was performed.

## Verification

**91 Python checks and 4 UI checks passed.** The Python run excludes `tests/test_maine_calibration.py`, which requires the intentionally excluded historical datasets. No historical calibration or forecast-accuracy claim is made.

The offline integrity check verified 101 reviewed records, 96 distinct accepted surveys, 26 registered models, the ledger, publication eligibility, Minnesota weights, turnout sigma, proxy authorization, null counts for unknown denominators, and hashes of 102 local evidence artifacts. Replaying the feed reproduces the saved state means and covariances within `1e-15`. Governor and national generic-ballot models remain prior only. Public forecasts project Senate models to November 3; histories use observation dates. Full results are in `verification/validation.json`.
