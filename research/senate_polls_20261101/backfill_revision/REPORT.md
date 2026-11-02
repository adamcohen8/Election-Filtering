# Backward extension to ten Senate polls

User authorization: extend before October 1 for races below 10, retaining all R/D/I cells and one observation per distinct survey. Before:96 observations. Added:33. Now:129. Eleven races reach or exceed 10; Kansas 9 remains one short.

| Race | Before | Added | Now |
| --- | ---: | ---: | ---: |
| Florida | 9 | 1 | 10 |
| Texas | 20 | 0 | 20 |
| Georgia | 2 | 8 | 10 |
| Maine | 10 | 0 | 10 |
| New Hampshire | 6 | 4 | 10 |
| Iowa | 7 | 3 | 10 |
| Alaska | 3 | 7 | 10 |
| Michigan | 9 | 1 | 10 |
| Ohio | 10 | 0 | 10 |
| North Carolina | 7 | 3 | 10 |
| Kansas | 7 | 2 | 9 |
| Minnesota | 6 | 4 | 10 |

The original 96 normalized rows are unchanged, not merely their IDs. Their source-record hashes are pinned in the review policy. Newer inaccessible or incomplete source gaps are documented in each backfill inventory; latest verified accessible evidence is not a completeness claim. Alaska and Georgia require five 2025 waves in total, labeled hypothetical where applicable. Missing Ns, weighted bases and proxy party definitions remain labeled. Kansas cannot reach 10 with the located complete evidence; no partial table, satisfaction rating, different candidate or repeated ballot version was added to fill the gap.

`added-records.json` lists all 33 keys. Before-manifest/decisions/report preserve the 96-wave baseline. Current manifests, all source evidence, the offline importer and integrity script reproduce the final model and public exports.94 Python checks and 4 UI checks passed, excluding the historical Maine-calibration test that requires intentionally excluded data. No historical accuracy/calibration claim, commit, push or deployment.
