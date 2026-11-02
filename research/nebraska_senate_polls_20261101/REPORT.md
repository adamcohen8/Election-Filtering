# Nebraska Senate addition — November 1, 2026

Nebraska Senate is now modeled as **Pete Ricketts (Republican) / Dan Osborn (Independent)**. Candidate affiliation is verified by the [AP Nebraska election guide](https://apnews.com/article/78b5008f5c41597306574eccabec630f). Osborn is not assigned to a Democratic caucus or treated as a Democratic nominee. Other ballot candidates remain outside the two-candidate model, with no renormalization of the observed shares.

The user selected **R57/D24/I19** on November1, replacing R55/D25/I20 and the earlier interim R45/D27/I28. These are user-selected turnout assumptions, not exit-poll estimates. The existing turnout-share standard deviation remains 1pp (3pp at three sigma) with the sum-to-one constraint.

## Poll coverage

Four source-backed waves have all six conditional R/D/I candidate support cells:

| Publication | Pollster | Status |
|---|---|---|
| October 30, 2026 | [On Point](https://onpointpolitics.substack.com/p/new-nebraska-poll-osborn-and-ricketts) | In window; registration groups and source-produced modeled allocation of undecideds |
| September 14, 2026 | [SurveyUSA](https://results.surveyusa.com/client/PollReport.aspx?g=d94236a7-5861-4b7f-9d81-d5a81ab786cc) | Older backfill; party affiliation; exact subgroup Ns unavailable |
| May 11, 2026 | [Tavern Research](https://www.tavernresearch.com/research-and-writings/nebraska-senate-poll) | Older backfill; self-reported party, table bases of unspecified weighting; hypothetical of the same pair |
| January 22, 2026 | [Lake Research](https://drive.google.com/file/d/1Izlk1L3prsXm04d-1ZRi8cLSliHvySnC/view) | Older backfill; December 2025 fieldwork, registration proxy, first-choice rounded component sums |

The target of ten remains **six polls short**. The [per-race inventory](ne_sen/inventory.json) records other sources screened: YouGov, NPA, co/efficient and Echelon public releases lack complete party-ballot cells; Concord offers tabs on request; GBAO's linked report was unreadable; NYT was not accessed after the prior site-policy denial. No missing cells are inferred from toplines, sample composition or a forecast's model crosstabs.

On Point's allocated ballot is labeled `modeled_subgroup_estimate`, retaining its original registration basis and counts. Under the previously authorized source-model inclusion policy it uses explicit assumed measurement covariance, not ordinary interview-count precision. SurveyUSA also uses explicit covariance because exact subgroup counts are unavailable; source Ns stay null. The working covariance is 5pp SD per cell, within-party correlation -0.5, no across-party correlation. Tavern uses DEFF2 for the reported bases with unknown weighting status. These are provisional uncertainty assumptions, not empirical calibration.

## Model and display

The registry, nominee metadata, canonical candidate orientation, public exports and UI support Independent candidate B. Reversed A/B inputs also permute measurement covariance correctly. Party-named Republican/Democratic aliases are rejected for Nebraska to prevent labeling Osborn's support as Democratic support. Osborn-led ratings and map colors are purple; the chart legend says Independent and the Senate seat summary gives an independent outcome its own count without assigning a caucus.

All **258 prior feed rows and 27 prior race states/electorates are preserved**. The combined feed now has 262 observations across 28 race models: 13 Senate, 14 governor and one prior-only generic ballot.

Validation: **100 Python tests and 6 UI tests passed**; the historical Maine calibration module remains excluded because its original datasets were deliberately not imported. Complete replay, snapshot, ledger, public forecasts/history, source hashes and preservation audits pass. These checks do not validate historical predictive accuracy. No commit, push or deployment was performed.

Offline rebuild/check:

```bash
python scripts/ingest_nebraska_research.py --check
python scripts/ingest_nebraska_research.py
python research/senate_polls_20261101/verification/validate.py
python research/governor_polls_20261101/verification/validate.py
```

[Reviewed records and decisions](review-decisions.json) · [Manifest and preservation counts](ingestion-manifest.json) · [Source research](ne_sen/REPORT.md)

Re-audit: the [older-source review](reopened_older/REPORT.md) recovered Lake Research; the [October-source review](recheck_20261101/REPORT.md) records each outstanding public-release gap. Lake uses the same explicit 5pp cell SD covariance as other missing-base inputs. Its printed group bases are retained as metadata, with model Ns null. The January22 release date is explicitly stated in the campaign release republished by Huskeradio January27. The December2025 field dates are intentional: user authorized backfilling before October until ten qualifying waves.

Re-audit validation passed: all four selected source hashes checked; 258 pre-Nebraska feed rows and all27 prior race states/electorates preserved; full262-row replay matches snapshot, ledger, public forecasts and history. Existing Senate and governor acquisition integrity checks and git diff whitespace checks passed.
