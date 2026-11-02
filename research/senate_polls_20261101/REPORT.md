# Senate polling acquisition — November 1, 2026

Loaded **129 distinct reviewed survey waves across all 12 Senate models**. This revision adds **33 older waves** to the previous 96 after the user authorized extending before October 1 for races below 10. **Eleven Senate races now have at least 10 polls; Kansas has 9 and remains one short.** Complete R/D/I candidate support remains required; no partial tables or invented cells were used to meet a count.

The original 96 accepted observations are unchanged, verified against the archived original decisions and full normalized rows. All new observations are explicitly reviewed pre-cutoff exceptions for the nine affected races. Texas retains 20; Maine and Ohio retain 10. The importer preserves every prior source-record hash and prevents backfill beyond 10 for affected races. Source and publication gaps remain documented; this is the most recent **verified accessible** qualifying evidence found, not proof that every newer public table was recovered.

| Senate race | Before extension | Older waves added | Now loaded |
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
| **Total** | **96** | **33** | **129** |

## Eligibility, dates and source coverage

The original window remains **October 1–November 1, 2026**, determined by publication date. The user subsequently authorized older releases only for the sub-10 races, most recent eligible publication first and continuing backward. Same-wave LV/RV, ballot and party-basis alternatives are counted once. Field-end dates determine model chronology, followed by a full global replay. Older observations are never applied as current polls.

Alaska and Georgia require five surveys from 2025 between them, including pre-candidacy hypothetical matchups of the same current candidates. These remain labeled, rather than presented as recent polls. The earliest field end is April 27, 2025; the latest is October 31, 2026. Eight publication dates are bounded rather than exact. The earliest publication bound is April 27–May 1, 2025. Each selected raw record and review preserves its date evidence. Older raw source dates are not inferred from aggregator-added dates.

**Kansas remains below target.** The two verified older additions are Emerson September 18 and Tavern's January fieldwork, publicly available by April 17. PPP August 13 supplies only three of the six required cells; co/efficient supplies toplines and party composition; GSG and GBAO public memos have no verified complete party ballot table. Kansas Speaks 2026 was inspected directly: its party crosstabs measure Marshall satisfaction, not Marshall/Hamilton vote choice. A different-candidate GQR hypothetical and another question from the same Tavern sample cannot supply an independent tenth wave. The source gap is documented in `backfill_ks_sen/REPORT.md` and `inventory.json`.

Newer unresolved tables are also recorded for the other races. Where inaccessible newer waves could qualify, older verified sources are fallbacks; no claim is made that the selected older waves are necessarily the newest published complete tables. Minnesota's recovered September 11 Quantus table replaced its initially identified August SurveyUSA fallback. All selected backfill packages are `backfill_<race>/`; baseline decisions and manifest are in `backfill_revision/`.

The seven user-supplied NYT/Siena tables remain included. Their screenshots establish candidate-by-party cells; unshown methodology and field metadata retain provisional labels. Florida chronology provisionally uses October 26 within conflicting October 25–26 field-end bounds. Minnesota's censored Tafoya-among-Democrats cell retains `<0.5%`, with a labeled 0.25% midpoint and added squared 0.25-point half-width variance. No direct blocked-site access or NYT image generation was used for this revision. Washington Post/Schar Maine and Kansas remain included. Echelon and co/efficient toplines without complete conditional party cells remain excluded. Wedgewood remains excluded as fabricated.

## Party definitions and measurement precision

The 129 waves comprise **72 party-ID, 19 party-registration, 6 modeled-party, 31 unspecified-party, and 1 source-modeled subgroup prediction** observations. Where available, unleaned identification is preferred. Source-specific leaners, independent/other pooling, and Alaska no-party registration groups remain explicitly labeled; these measures are not identical. Proxy classifications require individual review authorization.

| Subgroup precision basis | Waves |
| --- | ---: |
| Reported unweighted interviews | 18 |
| Reported weighted bases | 22 |
| Reported bases, weighting unspecified | 26 |
| Reported effective sizes | 1 |
| Estimated matching total × rounded composition | 26 |
| Published suppression lower bound | 12 |
| Explicit assumed covariance; missing counts stay null | 24 |

Weighted bases are not unweighted interviews. Fractional weighted bases are retained and floored only for integer model inputs. Working design effects follow the existing policy: 1.5 for unweighted, 2 for weighted/unspecified, 3 for composition estimates and selected Quantus/proxy sources, with source-informed exceptions; these are provisional assumptions. For 24 waves with unavailable verified group counts, the explicit measurement covariance assumes 5 pp SD per candidate/group cell, within-pair correlation -0.5 and zero across groups. No subgroup N is invented. Interval approximations retain the original censored values and add half-width-squared variance.

Turnout assumptions are unchanged: **1pp one sigma / 3pp three sigma per party share**, with sum-to-one covariance. Minnesota retains **R34/D37/I29**. Persistent polling-error settings are unchanged; more observations do not establish historical forecast accuracy.

## Reproduction and verification

Run offline from the repository root:

```bash
python scripts/ingest_senate_research.py --check
python scripts/ingest_senate_research.py
python research/senate_polls_20261101/verification/validate.py
```

The feed is `data/ingestion/2026_normalized_polls.json`; model and ledger are in `data/models/2026_election_model.json` and `data/ingestion/2026_seen_polls.json`. Static forecasts and history are `docs/data/forecasts.json` and `race-history.json`. Current controlling records are `review-decisions.json`, `ingestion-manifest.json`, and `verification/validation.json`. Earlier reports preserve historical research status; this report and current decisions control final inclusion.

**94 Python checks and 4 UI checks passed.** The Python suite excludes the historical Maine-calibration test because its original datasets were intentionally not imported. The offline audit verifies 134 reviewed records, 129 accepted distinct samples, 26 registered models, 132 evidence-artifact hashes, original 96 normalized rows unchanged, the exact remaining Kansas shortfall, publication eligibility, proxy authorization, candidate direction, the ledger and full numerical replay. Replayed means and covariances match the saved snapshot within 1e-15. All 12 Senate models have observations; governor and generic-ballot models remain prior-only. Public forecasts project to November 3; histories use observation dates. No commit, push or deployment was performed.
