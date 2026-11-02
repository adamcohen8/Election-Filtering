# Election filtering methodology, version 2

Version 2 addresses the methodology review of November 1, 2026. It retains the
user-selected R/D/I central weights and the audited 2026 candidate registry.
It provides individual race estimates; it does not estimate joint chamber-control
probabilities. No historical polling datasets were imported for this upgrade.

## State, orientation, and calendar

Each race tracks six conditional support probabilities:

```
x = [P(A | R voter), P(B | R voter),
     P(A | D voter), P(B | D voter),
     P(A | I voter), P(B | I voter)]
```

Candidate A is Republican and candidate B is the registered opponent. Candidate B
is Democratic in the other modeled races and Independent Dan Osborn in Nebraska.
`*_rep` and `*_dem` input columns follow those party labels and are rejected for
an independent-opponent race, which must use explicit A/B columns. Explicitly named
candidate-A/B columns can be reversed when the supplied names or party labels
identify an opponent-first matchup. Contradictory labels and conflicting share
aliases are rejected. Unlabeled A/B columns must already follow the canonical
order. Missing party groups remain unobserved. Percent-marked inputs such as
`1%` mean 0.01; unmarked fractional inputs are in [0, 1].

Observations use ISO field-end dates (`YYYY-MM-DD`). All sources are combined
and sorted before updating. Between observation dates the state follows
`x[t] = F x[t-1] + noise`, with default `F = I` and daily process covariance
`Q = 0.00005 I`. Same-day polls add no process noise. An older observation
arriving after a saved state is rejected with a full chronological replay
instruction; it is never silently applied as a current poll.

The Senate acquisition originally admitted publications October 1 through
November 1, 2026. The user subsequently authorized going backward for races
below ten distinct polls, stopping each at ten. Each older addition requires
both a race-level eligibility policy and an individual review authorization;
the original accepted rows remain unchanged. Complete candidate support within
all R/D/I groups remains required for this acquisition. Newer unreadable tables
are documented as gaps, so older selected sources are the latest verified
accessible evidence rather than proof of exhaustive coverage. Alaska and Georgia
include labeled 2025 hypothetical matchups of the same current candidates.
Unknown publication dates retain explicit bounds; older results use their
field-end dates during a full chronological replay.

`RaceModel.forecast()` estimates support at the last observation date.
`forecast(target_date="2026-11-03")` projects to Election Day without mutating
the ingested state. The public forecast uses that election date; historical
charts use each observation date. Daily process variance is a provisional
configuration choice and needs historical calibration.

## Poll likelihood and persistent errors

Crosstab measurement covariance uses multinomial candidate-share variances
and negative covariance between the two candidates. Subgroup effective sample
size is `n / design_effect`. Topline-only observations use a two-row linear
measurement matrix weighted by the central electorate composition. Continuity
floors handle rounded zero/100-percent responses. Dates, finite values, sample
sizes, probability bounds, symmetry, and positive semidefiniteness are validated.

The November 1 reopening also permits an explicit six-by-six measurement
covariance (`crosstab_covariance`) when subgroup counts are absent or the source
publishes model-derived subgroup estimates. The source counts remain unknown;
no synthetic respondent counts are assigned. For this acquisition the working
assumption is a five-percentage-point SD per candidate/group share, correlation
-0.5 between the two candidates within each group, and zero measurement
correlation between groups. The per-group covariance block is therefore
`[[0.0025, -0.00125], [-0.00125, 0.0025]]`, corresponding to a within-group
margin SD of about 8.66 points. This covariance already defines measurement
error and is not multiplied by a design effect again. Persistent errors below
are still added. This is an explicit provisional assumption, not an estimate
of a missing sample size or a calibrated bound on poll error.

Modeled voter-file party, unspecified party classification and source-produced
subgroup predictions are included only with an explicit review authorization,
following the user's instruction to reopen those exclusions. Their source
classification is preserved in the feed and public history. When a published
support cell is interval-censored, the review can explicitly choose its midpoint
and add the squared half-width to its measurement variance; the raw interval
and approximation remain recorded. The ECU `<1%` cell uses a 0.5% midpoint
with an additional 0.5-point SD. This Gaussian moment approximation does not
claim that the source published an exact 0.5% or provide an exact censored-data
likelihood. Candidate orientation also permutes any supplied covariance.

An augmented Gaussian state contains support plus directional error terms:

```
z[poll] = H x + H v (shared_error + pollster_error + survey_error) + noise
v = [0.5, -0.5, 0.5, -0.5, 0.5, -0.5]
```

An error of 0.01 therefore changes the Republican-minus-opponent margin by
one percentage point. The filter retains and updates the joint covariance,
including support/error cross-covariances. Repeated polls cannot erase the
uncertainty from their shared directional errors by averaging alone.

| Parameter | Default | Interpretation |
| --- | --- | --- |
| `design_effect` | 1.5 | Sampling variance multiplier; configurable per poll |
| `shared_margin_sd` | 0.02 | Two-point margin SD shared by every poll in a race |
| `pollster_margin_sd` | 0.01 | One-point margin SD shared by a pollster's releases |
| `survey_margin_sd` | 0.01 | One-point margin SD shared by releases from a survey |
| `process_variance` | 0.00005 | Per-day variance for each conditional support state |

These polling-error defaults are explicit provisional assumptions. The user's
three-point, three-sigma allowance applies to turnout shares separately.
The error parameters can be supplied to `RaceModel.default()` or
`create_2026_election_model()`; the design effect can be supplied to each
observation or normalized poll record. They have not been fitted to held-out
historical elections.

Pollster names are normalized for grouping. A poll's `sample_id` identifies a
shared survey or overlapping release group; without one, the default group is
pollster plus field-end date. This models common directional errors within the
group. It is an approximation to arbitrary respondent-level overlap, for which
sample membership information would be necessary. Exact repeated measurements
from the same pollster/date/race/sample are deduplicated across IDs and source
URLs, and the fingerprint ledger is saved.

## Probability constraints

For each party group, candidate support is non-negative and the pair sums to
at most one, leaving residual undecided/other support. If a Gaussian update
violates a constraint, the filter conditions its joint moments on that
half-space. The one-half-space truncated-normal mean and covariance are used,
including cross-covariances with polling errors. It repeats if another constraint
is violated. It does not independently clip the mean and leave covariance intact.

This is an assumed-density constrained Gaussian filter: sequential moment
matching approximates a jointly truncated posterior. Normal intervals are also
approximations, especially near boundaries. Constraint checks and stress tests
do not establish exact posterior coverage near those boundaries. Material
negative eigenvalues are rejected; only floating-point-sized negative
eigenvalues are repaired. An invalid negative forecast variance raises an error.

## Turnout uncertainty requested by the user

The user updated Maine's central weights to R26/D30/I44, Alaska's to
R40/D24/I36, New Hampshire's to R32/D30/I38, Kansas's to R48/D27/I25,
Iowa's to R38/D27/I35, Ohio's to R42/D30/I28, Nebraska's to R57/D24/I19,
and Nevada's to R38/D34/I28 on November 1, 2026.
These state weights apply to both the Kalman
forecasts and the poll shares used in the rolling averages.
A three-sigma error of three percentage
points gives a marginal standard deviation of **one percentage point per
R/D/I share**. Because the shares sum to one, equal marginal variances imply
pairwise correlation -1/2:

```
Sigma_w = 0.01^2 * [[ 1,   -0.5, -0.5],
                   [-0.5,  1,   -0.5],
                   [-0.5, -0.5,  1  ]]
```

This covariance has zero row sums. It is a local Gaussian moment approximation;
the supplied central weights are all more than three SDs from the boundaries.
Other electorate scenarios can configure `Electorate.share_standard_deviation`.

Let `d` be the three within-party candidate margins, `w` the electorate shares,
and `Sigma_d` the forecast covariance of `d`. The mean margin is `w' d`.
Under the explicit assumption that turnout composition and conditional support
are independent, the variance is:

```
Var(margin) = w' Sigma_d w
            + d' Sigma_w d
            + trace(Sigma_w Sigma_d)
```

The final term includes the interaction between uncertain support and uncertain
turnout. Public exports report SD components for polling, movement to Election
Day, and turnout; those components combine in quadrature. This is an independent
turnout-scenario calculation, including when topline-only polls were used to
estimate conditional support with the central weights. It does not jointly
infer correlations between turnout and conditional support from those polls.

## Export and restart behavior

A race with no dated observations has estimate type `prior_only` and status
`unrated` ("Awaiting polls"): no numerical forecast
or partisan race rating is published. With observations, labels use only the
absolute forecast margin in percentage points: Tossup below 0.5, Tilt from 0.5
to below 2, Lean from 2 to below 5, Likely from 5 to below 8, and Safe at 8 or
above. The uncertainty interval is reported separately and does not override
these labels. They are not empirically calibrated win-probability categories.

Snapshot schema 2 retains dates, observation counts, electorate uncertainty,
transition/process settings, persistent-error settings, bias-state keys, and the
full augmented mean/covariance. Snapshot files are replaced atomically. Older
snapshots are rejected with a replay instruction because their missing chronology
and persistent-error information cannot be reconstructed from a final mean and
covariance alone. The source pipeline and historical export share observation
application, orientation and duplicate handling.

## Seven-poll comparison

The public race history also includes an equal-weight arithmetic average of the
latest seven poll-marker support estimates, using all available polls until
seven exist. The comparator uses the same canonical candidate order, blocked
pollster exclusions, chronological sorting and duplicate checks as the Kalman
history. Crosstabs are combined using the race's central electorate shares;
reported toplines remain toplines. It averages the exported four-decimal shares
separately for each candidate, with Republican-minus-opponent margin computed
from their averages. No sample-size or recency weights are applied.

The window counts polls, including distinct polls on the same date. Charts keep
the final window for each date, and each point retains its constituent poll IDs
and count. Races without polls have no average. This descriptive comparison
does not project to Election Day or supply an uncertainty interval.

## Verification and calibration limits

The November 1 governor acquisition uses the same six conditional R/D/I support
inputs and provisional precision policies as the Senate acquisition. Initial
and leaned ballots, voter registration and self-reported party ID, and broad
independent/other versus narrow independent groups retain their source labels.
Separate Senate and governor questions from one survey update their own race
models once each. The models do not estimate covariance across races sharing
respondents, so their forecasts must not be treated as independent draws when
calculating combined election outcomes.

All recovered complete governor tables published October 1 through November 1
are included. Older verified waves fill sub-ten races toward ten where sources
permit. Missing subgroup sizes remain unknown; their working measurement
covariance uses 5pp cell SD and within-party correlation -0.5. Published
weighted counts and composition-derived estimates are separately labeled.
The Minnesota NYT governor `<0.5%` cell uses a 0.25% midpoint; Maine Marist's
`<1%` cell uses 0.5%. Each retains its original censored interval and adds the
squared interval half-width to the corresponding measurement variance. These
are explicit approximations, not exact published values. Research decisions,
source artifacts and remaining source gaps accompany the normalized feed.

`tests/test_methodology.py` checks chronology, candidate direction, deduplication,
prior-only outputs, covariance validity, constrained moments, turnout moments,
persistent error, restart equivalence, and agreement between ingestion and history.
A deterministic Monte Carlo check compares the turnout variance formula with
independent draws. A separate synthetic-election experiment checks interval
coverage under the declared error assumptions. These checks test implementation
and internal statistical consistency.

Historical forecasting accuracy and interval coverage remain unverified. The
Maine retrospective weight fit explicitly includes the known election outcome in
its objective and is not an independent forecasting backtest. Empirical
calibration must hold out complete races or election cycles, estimate parameters
on training data only, and evaluate both margin error and predictive-interval
coverage on the held-out outcomes.

A useful reference for pollster effects, non-sampling error, time dynamics and
historical calibration is [Heidemanns, Gelman and Morris (2020), *An Updated
Dynamic Bayesian Forecasting Model for the US Presidential Election*](https://stat.columbia.edu/~gelman/research/published/Harvard_Data_Science_Review.pdf).
The defaults above are this repository's provisional settings and are not
estimates adopted from that paper.
