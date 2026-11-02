# Reopened exclusions — November 1, 2026

The user authorized adding polls previously excluded for modeled affiliation, unclear party basis/counts, and source-access limitations. The October 1 publication cutoff was explicitly reaffirmed. This revision adds **33 waves**, increasing the feed from 49 to **82** and giving all 12 Senate models polling inputs. The original 49 accepted wave IDs are retained.

`changed-records.json` lists all 33 additions. Original decisions, manifest and forecast summary are saved alongside this report. Current counts and exact review/source hashes are in the parent `ingestion-manifest.json` and `review-decisions.json`; original first-pass race subreports are historical evidence, not the current acceptance list.

## Source recovery and inclusion

- All six eligible Quantus PDFs were recovered and the first-choice party tables checked centrally: Alaska, Georgia, Michigan, North Carolina and two Texas waves. Original PDFs are under `reopened_quantus/sources/`. Georgia, Michigan and Texas use modeled voter-file party; North Carolina explicitly uses actual registration. Alaska's self-report versus voter-file wording conflicts, so it is classified as unspecified. Published table bases stay labeled weighting-unspecified; working design effect 3 is used.
- Twelve Rasmussen waves are now included: six previously held and six newly recovered. Their party basis is explicitly unspecified. Rounded party shares provide derived bases, not actual group counts. The direct tables control where Alaska or Minnesota articles contradict them; the conflicting summaries remain documented. The earlier NH publication date is bounded October 4–5 rather than fabricated as exact.
- Four additional CNN/SSRS tables were read in the ordinary DocumentCloud browser viewer for Texas, Maine, Kansas and Ohio. The report's minimum 125 unweighted cases for displayed groups supplies only a nominal size bound; registered-voter totals are not substituted for the likelihood-weighted LV base. Existing Iowa and Michigan SSRS waves are not duplicated.
- BGSU/YouGov Ohio was recovered with reported unweighted group counts. The previously held WaPo/Schar, UT/YouGov, UMass Lowell/YouGov and ReconMR/Siena complete tables are now included despite missing subgroup counts.
- ActiVote NC is labeled party-basis-unspecified, preserving possible mixed or modeled classification. Pollfinity Texas uses modeled voter-file categories, including a nonpartisan group of only 17 and a conflict between its RV description and registration-screen results. A2 Texas uses fitted subgroup predictions, with unknown actual group sizes and a publication interval October 27–29; it is not described as a raw crosstab.
- ECU NC's interval-censored cell is included through an explicit approximation, not an invented exact source response.

## Measurement uncertainty without invented N

The model now accepts a validated explicit six-state measurement covariance. Eight waves use a declared working SD of 5 points per candidate/group share, correlation -0.5 within the pair and zero measurement covariance across party groups. This gives within-group margin SD about 8.66 points; shared/pollster/survey errors still apply. No sample count is inferred from this assumption, and unknown `*_n` fields stay null. A direct covariance is not multiplied by a design effect a second time. Its shape, symmetry, finite entries and positive semidefiniteness are checked; candidate reversal permutes the covariance consistently.

The ECU `<1%` cell uses the midpoint 0.5% and adds squared half-width `0.005^2` to that cell's variance. The original null/censor metadata, interval and approximation remain in the feed. This is an approximate Gaussian observation, not a claim that the publisher reported an exact midpoint or an exact censored-data likelihood.

These measurement assumptions are provisional and do not modify the requested turnout covariance: each electorate share still has one-point marginal SD, equivalent to three points at three sigma, with the sum-to-one constraint. Classification and precision method are exported with each public history point and shown in poll tooltips. Missing sample counts export as null rather than zero.

## Remaining limits and verification

Five reviewed records remain unselected: four duplicate survey alternatives and the September-publication Suffolk Ohio wave. Quantus Iowa's September 30 release remains outside the window. The inventories still record unreadable or incomplete sources, including NYT/Siena access restrictions. User authorization does not create missing candidate-support figures; no such figures were invented. Wedgewood remains blocked.

All inputs were replayed chronologically into fresh models, then the feed, ledger, snapshot, forecast and history exports were updated. **91 Python checks and 4 UI checks passed**, with the historical Maine calibration suite excluded because its original data was intentionally not cloned. Offline integrity checks verify 82 distinct survey IDs, source hashes, explicit proxy authorizations, publication dates/bounds, state weights, null unknown Ns and snapshot replay. No forecast calibration or accuracy claim follows from these implementation checks. No commit, push or deployment was performed.
