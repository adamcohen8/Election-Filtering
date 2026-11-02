# Separate-crosstab follow-up — November 1, 2026

Added seven InsiderAdvantage survey waves to the prior 82, bringing the accepted total to 89 across all 12 Senate models. The before-review and before-manifest files preserve the baseline; `added-records.json` lists the exact seven keys. All original 82 accepted waves remain included.

| State | Publication | Fieldwork | Original chart |
| --- | --- | --- | --- |
| Ohio | Oct 1 | Sep 28–29 | `../reopened_insider/sources/oh01.jpg` |
| Kansas | Oct 11 | Oct 9–10 | `../reopened_insider/sources/ks11_x.jpg` |
| Kansas | Oct 15 | Oct 13–14 | `../reopened_insider/sources/ks16_x.jpg` |
| Maine | Oct 15 | Oct 13–14 | `../reopened_insider/sources/me_x.jpg` |
| Texas | Oct 15 | Oct 13–14 | `../reopened_insider/sources/tx_x.jpg` |
| Michigan | Oct 23 | Oct 21–22 | `../reopened_insider/sources/mi_x.jpg` |
| Florida | Oct 30 | Oct 28–29 | `../reopened_insider/sources/fl_x.jpg` |

The separately published original charts were centrally visually checked against every R/D/I candidate cell and subgroup base. Publication evidence and original URLs are retained in `../reopened_insider/inventory.json` and `polls.json`. Party classification and count weighting are not established by the chart labels and remain explicitly unspecified. Working design effect 2 follows the existing policy. Each wave has explicit review authorization and a raw-record hash; no population or ballot alternatives are counted twice.

Six further identified in-window InsiderAdvantage waves remain unresolved: AK and MI October 11; IA and OH October 23; MN and OH November 1. A Minnesota September 30 release is outside the cutoff despite a later chart repost.

Washington Post/Schar Maine October 9 and Kansas October 30 were already included; the focused search found no additional qualifying wave. Echelon and co/efficient add zero because complete state candidate-by-party tables have not been verified. The user explicitly retained the R/D/I requirement, so topline-only releases remain excluded.

Siena confirms seven NYT/Siena crosstab links, but the root browser's site-safety policy blocked reading and explicitly forbade workarounds. No automatic approval review or permission prompt occurred. No NYT images were generated, and no unverified cells were ingested. User-provided files or pasted party rows are needed to complete that source with the available access.

The importer rebuilds the model and public outputs from all 89 accepted waves. The central `../verification/validation.json` records counts, evidence hashes, ledger consistency and numerical replay checks. The Python suite excludes the Maine historical-calibration test because its intentionally excluded historical data were not imported.
