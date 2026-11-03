# November 3 polling scrub

**Subsequently superseded by the user's AtlasIntel exclusion.** This report and its validation describe the347-observation pre-exclusion snapshot. The current feed has329 observations; use [the exclusion report and validator](../atlas_exclusion_20261103/REPORT.md) for current-state checks.

Added **18 newly verified race observations: ten Senate and eight governor**, taking the feed **329 → 347** across the existing28 models. These are15 AtlasIntel observations and three Rasmussen observations. All329 earlier normalized inputs and all45 earlier raw acquisition records/reviews remain exactly preserved. All28 electorate weights, turnout uncertainty and other model assumptions are unchanged. The new November1 NYT/Siena Texas Senate wave remains excluded; Texas Senate stays at22 inputs. Alaska governor remains excluded.

## Accepted sources

[AtlasIntel's public exclusive-polls page](https://www.atlasintel.org/polls/exclusive-polls) now supplies downloadable Atlas/PollsterGraph reports for nine states, each released November2 and fielded October28–November1. Add Senate observations for Alaska, Iowa, Kansas, Maine, Michigan, Minnesota, New Hampshire, North Carolina and Ohio; add governor observations for Iowa, Kansas, Maine, Michigan, New Hampshire and Ohio. Minnesota's report has no governor ballot. Alaska governor is omitted under the user's instruction. Initial/raw ballot percentages from the PARTISANSHIP D/R/I columns are used, preserving nonvoters, other candidates and undecideds. Valid-vote alternatives and recalled-presidential-vote columns are not used. Alaska incumbent Dan S. Sullivan is distinguished from the similarly named other Republican.

Rasmussen's complete public tables add [Maine Senate](https://www.rasmussenreports.com/public_content/politics/public_surveys/crosstabs_2_maine_senate_october_27_november_2_2026), [Michigan governor](https://www.rasmussenreports.com/public_content/politics/public_surveys/crosstabs_2_michigan_governor_october_28_29_2026) and [Ohio governor](https://www.rasmussenreports.com/public_content/politics/public_surveys/crosstabs_2_ohio_governor_october_27_31_2026). Maine's November2 release covers October27–November2, n896. Michigan's original release HTML establishes October30 publication, covering October28–29, n745. Ohio's November2 release covers October27–31, n1119. The previously held Michigan table is public without a login, even though its full article is restricted. Ohio and Michigan governor complete surveys already represented by Senate observations; they do not create additional Senate waves. The original release date is used, not the index-added timestamp. Ohio Independent is separate from Another party; published Ind/Other groups remain pooled for Maine/Michigan.

| Race | New inputs | Total inputs |
|---|---:|---:|
| Alaska Senate |1|12|
| Iowa Senate |1|13|
| Iowa Governor |1|12|
| Kansas Senate |1|11|
| Kansas Governor |1|9|
| Maine Senate |2|14|
| Maine Governor |1|13|
| Michigan Senate |1|12|
| Michigan Governor |2|13|
| Minnesota Senate |1|14|
| New Hampshire Senate |1|12|
| New Hampshire Governor |1|12|
| North Carolina Senate |1|12|
| Ohio Senate |1|15|
| Ohio Governor |2|15|

Each accepted input has all six conditional party-support cells. Applicable subgroup respondent counts are not reported, so Ns remain null with the existing explicit5pp cell SD and−.5 within-pair correlation; the headline sample is not converted into artificial precision. Atlas uses its PARTISANSHIP grouping with leaner treatment unspecified, consistent with the existing Atlas records. Rasmussen's ambiguous Party label remains an explicitly authorized proxy. These are provisional measurement assumptions, not empirical calibration.

## Sources still held

- Emerson/Poll Vault: current indexes identify new Texas, Ohio, Maine and Michigan waves. The primary sponsor briefing remains paid and exposes no full public party tables; Emerson's website and signed-in public X profile still show October30 releases. No new Emerson inputs were added.
- John Zogby Strategies: the Michigan Senate/governor and national PDFs publish only decided-voter two-way tables. Full respondent party bases/undecided counts were not recovered, so these are held instead of treating decided-only shares as full-sample support. No analyst renormalization is performed.
- Targoz Florida: the new40-page report provides marginal ballot tables and party composition, without candidate support within R/D/I groups.
- Concord Michigan: original release says crosstabs available upon request; only toplines are publicly supplied. No outreach was performed.
- GOTV Iowa: party tables require email signup; none submitted. The sample's very small No Party group also does not establish usable independent support under its published suppression rule. No gated or hidden data was used.
- Morning Consult's tracker still returns403, and NBC's original release remains unavailable. Prior incomplete tables, policy-restricted NYT/AJC sources and the explicit Texas NYT exclusion remain held.

No qualifying new national generic-ballot observation was added; it remains at27. [held-inventory.json](held-inventory.json) records the source-specific outcomes. [discovery-inventory.json](discovery-inventory.json) preserves the28 race-index checks. This was a bounded public-source scrub, not proof of exhaustive private or unpublished coverage.

## Rebuild and validation

New inputs and review hashes are in [new-records.json](new-records.json) and [new-review-decisions.json](new-review-decisions.json). The established November2 acquisition remains the owner of deterministic replay; its window starts October30 to accommodate the newly recovered Michigan release and ends November3. Earlier inputs/reviews are immutable in this increment. [results.json](results.json) preserves before/after model outputs and rolling averages.

- 103 applicable Python tests and six UI tests passed.
- All five acquisition checks and both historical provenance/replay audits passed.
- All329 previous rows,45 raw records and reviews, and28 electorate/model configurations were preserved.
- All13 races without new observations retain identical conditional means and covariance within1e-15.
- Snapshot, ledger, forecasts and history match complete chronological replay. All rolling averages were independently recomputed; no duplicate IDs, sample IDs or same-race survey waves exist.
- All60 downloaded source/discovery artifacts pass hash and credential-pattern checks. No redactions were necessary.
- Historical Maine calibration data remains intentionally absent; no empirical forecast-calibration claim is made.

See [validation.json](validation.json). These changes are **local**; this scrub did not commit, push or deploy them.

```sh
.venv/bin/python research/poll_scrub_20261103/prepare_records.py
PYTHONPATH=src .venv/bin/python scripts/ingest_poll_refresh.py --check
PYTHONPATH=src .venv/bin/python research/poll_scrub_20261103/validate.py
```
