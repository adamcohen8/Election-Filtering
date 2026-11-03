# AtlasIntel exclusion — November 3, 2026

The user instructed: “I want you to exclude Atlas Intel from the model.” All18 active AtlasIntel race observations are now excluded: ten Senate, seven governor and one national generic ballot. The active feed falls from347 to329 observations across the same28 models. All329 other normalized rows, all electorate weights and all static model settings are unchanged.

The exclusion covers every modeled office and every AtlasIntel wave, including future refreshes and common joint labels such as AtlasIntel/PollsterGraph and Bloomberg/AtlasIntel. It reflects the user's preference; no new judgment about source quality is asserted.

## Application and provenance

The shared ingestion guard in `src/election_modeling/ingestion.py` recognizes AtlasIntel and Atlas Intel aliases. Direct poll application and the ingestion pipeline reject those inputs. Research compilers hold excluded sources; the refresh compiler omits them while retaining original reviewed source records. Public history also filters the exclusion before calculating charts or rolling averages, even if passed an older feed containing AtlasIntel.

Original source archives and raw source-review decisions remain intact. [excluded-polls.json](excluded-polls.json) preserves all18 normalized predecessors and the exclusion reason. The acquisition manifest lists the excluded poll IDs. [results.json](results.json) preserves before/after forecasts, poll counts and margins for all28 races.

All models, seen-poll/fingerprint ledger, public forecasts and public history were rebuilt chronologically from the329 remaining observations. The user-excluded new Texas NYT/Siena Senate wave and Alaska governor remain excluded. Nebraska's Dan Osborn remains Independent. Original turnout weights, including Maine R31/D28/I41 and Nebraska R57/D24/I19, remain unchanged.

## Verification

- 116 applicable Python tests and six UI tests passed.
- All five acquisition `--check` commands passed.
- All329 non-Atlas inputs and all original raw source records/reviews are exactly preserved.
- All28 electorate weights and static model settings match the pre-exclusion snapshot.
- All ten unaffected models retain identical conditional means and covariance within1e-15.
- Active feed, snapshot counts, ledger, forecasts, chart points and rolling averages contain no excluded AtlasIntel input; all agree with independent full replay.
- Every latest seven-poll rolling average was independently recomputed.
- Regression tests cover aliases/joint names, all three offices, direct/pipeline rejection without updates and filtering a contaminated historical feed.
- Earlier source-preparation append commands preserve the later acquisition records byte-for-byte and cannot restore AtlasIntel through replay.

[validation.json](validation.json) records the checks. Historical Maine calibration datasets remain intentionally absent; no empirical forecast-calibration claim is made. The user has requested publication to GitHub and removal of the deployment being replaced. Deployment verification is separate from the model checks recorded here.

```sh
PYTHONPATH=src .venv/bin/python scripts/ingest_poll_refresh.py --check
PYTHONPATH=src .venv/bin/python research/atlas_exclusion_20261103/validate.py
```
