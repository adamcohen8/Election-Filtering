# National generic House ballot acquisition — November1, 2026

Added **23 distinct waves from14 pollster programs** to `us_house_generic`, all with complete conditional R/D/I candidate support and publication dates or bounds within October1–November1. No earlier backfill was needed. The model uses the user-selected **R37/D33/I30**, with1pp marginal turnout SD (3pp at three sigma).

## Included waves

| Pollster | Count |
|---|---:|
| The Economist/YouGov | 4 |
| Fox News/Beacon Research/Shaw & Co. | 1 |
| CBS News/YouGov | 2 |
| Reuters/Ipsos | 2 |
| NPR/PBS News/Marist | 1 |
| Harvard CAPS/Harris Poll/HarrisX | 1 |
| UMass Lowell/YouGov | 1 |
| Rainey Center | 1 |
| Emerson College | 1 |
| Focaldata/Financial Times | 2 |
| ActiVote | 4 |
| BIG DATA POLL | 1 |
| Clarity Campaign Labs | 1 |
| On Point Polling | 1 |

## Source and measurement distinctions

One version per wave is used. Party tables cover13 LV,7 RV and3 adult populations. Economist party columns refer to the full RV sample, not the adjacent LV toplines. The October19 Reuters table and Focaldata tables cover adults. CBS and Big Data Poll party bases are weighted; Emerson asks registration or affiliation and provides fractional weighted bases. ActiVote party shares are rounded composition, so model subgroup Ns remain null. Focaldata seven-point party categories are pooled with weighted numerators and denominators: strong/not-strong identifiers form R/D and both leaner categories remain with Independent. Exact raw subgroup bases are summed, and missing party responses are not fabricated.

Clarity is explicitly labeled modeled party ID. Two small support values are the arithmetic difference of displayed group support and the corresponding displayed party margin, with rounding uncertainty retained. On Point uses source turnout probabilities and ballot soft targets, labeled modeled subgroup estimate and assigned conservative covariance rather than ordinary interview precision. Its raw interview bases remain metadata. Source binary ballots are kept as published; this pipeline does not discard undecideds, other parties or nonvoters by renormalizing.

Reported bases use provisional DEFF2. Missing or uncertain subgroup precision uses the existing explicit5pp cell SD covariance, within-party correlation−0.5. These are working error assumptions, not empirically calibrated pollster error estimates. Publication bounds are recorded where first-publication date is not independently pinned; all bounds fall entirely within the requested window.

## Gaps

- [Reuters/Ipsos September30–October5](https://www.ipsos.com/sites/default/files/ct/news/documents/2026-10/Reuters%20Ipsos%20October%20Large%20Issue%20Topline%2010.5%20release.pdf): Downloaded four-page public release covers registration and approval; says other questions held for future release. Complete ballot party table not recovered.
- [Echelon/NetChoice October16–23](https://netchoice.org/wp-content/uploads/2026/10/NetChoice-October-2026-Antitrust-Tech-Survey-Topline.pdf): Downloaded28-page topline and companion memo have generic candidate results by state, not conditional candidate support by respondent party. No six-cell table recovered.
- [Echelon October omnibus ending19](https://www.pollingforecast.com/us/polls/1000811): Distinct wave listed in secondary inventory; public six-cell primary source not recovered. Not treated as NetChoice duplicate.
- [Cygnal early October1–2](https://www.cygn.al/wp-content/uploads/2026/10/24822-Cygnal-National-Early-Oct26-NVT-Deck-Midterm-Political.pdf): Downloaded full public deck. Displayed generic/partisanship graphs not verified for all six exact cells; incomplete subgroup labels were not filled from remainder.
- [Cygnal October7–10](https://www.cygn.al/wp-content/uploads/2026/10/Cygnal-National-Poll-on-Foreign-Conflicts-Oct-2026.pdf): Downloaded35-page public deck; no complete six-cell candidate by party table verified.
- [Cygnal late October23–24](https://www.cygn.al/wp-content/uploads/2026/10/Cygnal-National-Late-Oct26-NVT-Deck-Public.pdf): Downloaded full public deck. Page28 shows R91.1/D6.4 among Republicans and R37.4/D51.1 among Independents; Democratic crossover not printed/readable as an exact cell. No missing support inferred from graph area.
- [ABC News/Washington Post/Ipsos October9–13](https://www.ipsos.com/en-us/ABC-News-Washington-Post-Ipsos-Poll-October-2026): Downloaded32-page public trend topline, not the full party crosstabs. Candidate question Q4 is present but no complete party table recovered. Tables may exist elsewhere.
- [Pew September28–October4](https://www.pewresearch.org/wp-content/uploads/sites/20/2026/10/PP_2026.10.8_midterms_report.pdf): Downloaded60-page report. Complete unleaned/leaned three-group ballot cells not recovered; combined party/leaner toplines are not six conditional cells.
- [Prolific October21–22](https://www.prolific.com/resources/poll-democrats-lead-by-11-points-here-s-how-we-reached-that-number): Downloaded linked primary10-page questionnaire; it contains question wording and methodology, not complete reported party-cell results.
- [Penn State/YouGov October14–20](https://democracy.psu.edu/poll-report-archive/democrats-have-tiny-edge-in-congressional-generic-ballot/): Primary article retrieved; chart download returned403 and remaining party table not verified. No values manufactured from vague narrative.
- [Tufts/YouGov October23–27](https://tufts-pol.medium.com/tufts-public-opinion-lab-national-pre-election-poll-shows-a-big-lead-for-democrats-in-the-race-for-57656e85c738): Linked Box report inaccessible; primary article field-year2024 conflicts with2026 framing and needs resolving against original table. No full ballot by party cells verified.
- [Centerline September26–October1](https://centerliners.com/public-polling): October6 primary release and10-page topline checked; release reports only four of six support cells. No full R/D/I table linked on public polling page.
- [I&I/TIPP September29–October1](https://issuesinsights.com/2026/10/19/dems-hold-slim-lead-over-gop-in-midterm-vote-but-can-they-keep-it-ii-tipp-poll/): Six party-group values are shown, but inspected chart explicitly asks preferred party CONTROL OF CONGRESS, not district candidate vote. Different construct; excluded.
- [Bullfinch October1–6](https://www.independentcenter.org/poll-toplines/national-policy-survey-october-2026): Downloaded22-page public toplines; no six-cell ballot by respondent party table verified. Generic independent option is not itself disqualifying.
- [Quantus October national lead](https://quantusinsights.org/f/which-party-will-control-the-us-house?blogcategory=Polling): Indexed article surfaced, but opening primary URL returned homepage instead of report. Full attributable six-cell table not recovered. Party-registration proxy or modeled cells would be eligible if provided.
- [Morning Consult weekly October releases](https://pro-assets.morningconsult.com/wp-uploads/2026/09/MCPI-Midterm-Ballot.html): Public tracker shell retrieved via web; direct acquisition403. Dynamic party-series data not recovered. No weekly observations inferred from headlines or cumulative snapshot.
- [Morning Consult/Deseret October13–20](https://www.deseret.com/): National/Utah report identified in secondary inventory; no complete national candidate by party table recovered. State-only tables would not supply national input.
- [CNBC/Hart/POS October14–18](https://www.cnbc.com/2026/10/22/trump-economic-approval-rating-midterms-poll.html): Primary page returned cache miss; full six-cell source not recovered.
- [RMG/Napolitan October13–14](https://napolitannews.org/posts/generic-ballot-likely-voters-dem-54-gop-43): Public release retrieved; complete party ballot table not recovered.
- [Rasmussen weekly releases](https://www.rasmussenreports.com/): October weekly toplines identified in secondary inventory; no full public six-cell tables verified. Not excluded merely because a pollster is partisan.
- [TrueDot/NewsNation/DDHQ October5–9](https://thehill.com/homenews/campaign/6143963-democrats-lead-congressional-ballot-ddhq/): Primary release link returned cache miss; six-cell source not recovered.
- [The Honest Poll October4–6](https://www.thehonestpoll.com/polls/trump-approval-at-44-among-likely-voters-down-slightly-from-mid-september): Public article has generic topline and party approval splits; no complete ballot by party cells verified. Membership-only material not accessed.
- [NYT/Siena October12–19](https://www.nytimes.com/): Not accessed after explicit earlier tool site-policy denial; no alternate copy sought. Generic national party table remains unrecovered.
- [NYT/Siena September22–26 potential October release](https://www.nytimes.com/): Not accessed after earlier site-policy denial; publication boundary and full table not verified. No cutoff assumption used to admit it.
- Wedgewood: Not verified, no primary attributable source; excluded.

## Replay and preservation

The feed contains285 observations across28 models. All262 preceding feed records are byte-for-byte equal as JSON objects. All27 other race filter states, covariances, electorates and observation counts match the immediate pre-ingestion saved model. During research another workspace update changed Nebraska and Nevada turnout assumptions; the preservation baseline was refreshed before the first successful generic ingestion, and the initially observed snapshot remains archived. Those concurrent settings were preserved.

`python scripts/ingest_generic_ballot_research.py --check` validates compiled rows, all23 source hashes, duplicate measurements, replay, saved model, ledger, public forecasts and history. Existing Senate and governor integrity checks passed.100 Python tests passed (historical Maine calibration excluded because its original datasets were intentionally not imported), and6 UI tests passed. No commit, push or deployment performed.

Rebuild: `python scripts/ingest_generic_ballot_research.py`. The acquisition is separately tagged, so replay keeps Senate, governor and Nebraska inputs. Inspect `review-decisions.json`, `us_house_generic/polls.json`, `ingestion-manifest.json` and `inventory.json` for exact data and evidence.
