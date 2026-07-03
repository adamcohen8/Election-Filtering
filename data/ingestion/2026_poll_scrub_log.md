# 2026 Poll Crosstab Scrub Log

## 2026-07-03

### Sources Searched

- Live web searches for polls released since the 2026-07-02 run across the modeled 2026 Senate races: Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for polls released since the 2026-07-02 run across the modeled 2026 governor races: Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- New York Times/Siena battleground Senate crosstab package, published July 1 and modified July 2, with state crosstab pages for Alaska, Iowa, Maine, North Carolina, Ohio, and Texas.
- Guardian live coverage item linking to the New York Times/Siena battleground Senate polling package.
- Search-surfaced public aggregation and race pages for 2026 Senate and governor polling, including Race to the WH/RealClearPolling-style public tables and current public race polling summaries.
- Pollster/source-specific searches for July 2026 releases and crosstabs from Emerson College Polling, SurveyUSA, YouGov, Quinnipiac, Marist, Cygnal, Quantus Insights, and other surfaced public pollster pages.

### Polls Applied

- `nyt-siena_ak_sen_2026-06-15_2026-06-29_crosstab` -> `ak_sen`
  - Pollster: New York Times/Siena College.
  - Field dates: June 15-29, 2026; model field date stored as 2026-06-29.
  - Candidate A: Dan Sullivan (Republican). Candidate B: Mary Peltola (Democrat).
  - Party-ID crosstabs from the combined Senate ballot including leaners:
    - Republican self-ID, n=158: Sullivan 0.93, Peltola 0.06.
    - Democratic self-ID, n=82: Sullivan 0.05, Peltola 0.93.
    - Independent self-ID, n=288: Sullivan 0.38, Peltola 0.54.
- `nyt-siena_ia_sen_2026-06-15_2026-06-27_crosstab` -> `ia_sen`
  - Pollster: New York Times/Siena College.
  - Field dates: June 15-27, 2026; model field date stored as 2026-06-27.
  - Candidate A: Ashley Hinson (Republican). Candidate B: Josh Turek (Democrat).
  - Party-ID crosstabs from the combined Senate ballot including leaners:
    - Republican self-ID, n=191: Hinson 0.95, Turek 0.03.
    - Democratic self-ID, n=166: Hinson 0.01, Turek 0.98.
    - Independent self-ID, n=218: Hinson 0.42, Turek 0.48.
- `nyt-siena_nc_sen_2026-06-15_2026-06-27_crosstab` -> `nc_sen`
  - Pollster: New York Times/Siena College.
  - Field dates: June 15-27, 2026; model field date stored as 2026-06-27.
  - Candidate A: Michael Whatley (Republican). Candidate B: Roy Cooper (Democrat).
  - Party-ID crosstabs from the combined Senate ballot including leaners:
    - Republican self-ID, n=183: Whatley 0.91, Cooper 0.04.
    - Democratic self-ID, n=186: Whatley 0.02, Cooper 0.96.
    - Independent self-ID, n=208: Whatley 0.40, Cooper 0.52.
- `nyt-siena_oh_sen_2026-06-15_2026-06-28_crosstab` -> `oh_sen`
  - Pollster: New York Times/Siena College.
  - Field dates: June 15-28, 2026; model field date stored as 2026-06-28.
  - Candidate A: Jon Husted (Republican). Candidate B: Sherrod Brown (Democrat).
  - Party-ID crosstabs from the combined Senate ballot including leaners:
    - Republican self-ID, n=232: Husted 0.95, Brown 0.05.
    - Democratic self-ID, n=194: Husted 0.02, Brown 0.96.
    - Independent self-ID, n=158: Husted 0.36, Brown 0.58.
- `nyt-siena_tx_sen_2026-06-19_2026-06-27_crosstab` -> `tx_sen`
  - Pollster: New York Times/Siena College.
  - Field dates: June 19-27, 2026; model field date stored as 2026-06-27.
  - Candidate A: Ken Paxton (Republican). Candidate B: James Talarico (Democrat).
  - Party-ID crosstabs from the combined Senate ballot including leaners:
    - Republican self-ID, n=251: Paxton 0.91, Talarico 0.05.
    - Democratic self-ID, n=194: Paxton 0.03, Talarico 0.94.
    - Independent self-ID, n=173: Paxton 0.31, Talarico 0.58.

### Polls Skipped As Duplicates

- None.

### Polls Found Without Clear Party-ID Crosstabs

- None newly released since the prior run. The new NYT/Siena modeled-state Senate polls had explicit Democratic, Republican, and Independent party-ID rows and subgroup sample sizes.
- No newly released modeled governor poll with public party-ID crosstabs was found.

### Unclassified Polls

- New York Times/Siena College Maine Senate crosstab release, June 2026: reviewed as part of the battleground package but not ingested because Maine Senate is not in the modeled race list.

### Extraction Uncertainties

- NYT/Siena also publishes party-registration columns for Alaska, Iowa, and North Carolina; these were not used. The extracted rows use the `Party ID` columns labeled Democratic, Republican, and Independent.
- The extracted candidate shares are rounded percentages as published in the public NYT/Siena crosstab tables.
- The applied ballot tables are the combined U.S. Senate ballot including leaners; volunteered another-candidate and don't-know/refused shares were left outside the two-candidate Kalman observation.

## 2026-07-02

### Sources Searched

- Live web searches for polls released since the 2026-07-01 run across the modeled 2026 Senate races: Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for polls released since the 2026-07-01 run across the modeled 2026 governor races: Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Public aggregation/search surfaces for 2026 Senate and governor polling, including Race to the WH, RealClearPolling, FiveThirtyEight/ABC poll data endpoints, and current public race polling tables.
- Pollster/source-specific searches for July 2026 releases and crosstabs from Emerson College Polling, Cygnal, Quantus Insights, YouGov, Quinnipiac, SurveyUSA, and Marist.
- Current public race pages surfaced for North Carolina Senate, Georgia Senate, Texas Senate, Florida governor, Iowa governor, Michigan governor, and the national 2026 Senate/governor election polling tables.

### Polls Applied

- None. No newly released modeled-race poll with clear Republican, Democratic, and Independent party-ID crosstabs was found after the 2026-07-01 run.

### Polls Skipped As Duplicates

- None.

### Polls Found Without Clear Party-ID Crosstabs

- None newly released since the prior run. Search results continued to surface older topline-only or already-reviewed public polling entries, including North Carolina Senate, Texas Senate, Iowa governor, and Echelon/NetChoice state oversample tables already recorded in the 2026-07-01 log.

### Unclassified Polls

- None.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new release was located.
- `docs/data/forecasts.json` was refreshed from the existing model snapshot; the only forecast export diff was the generation timestamp.

## 2026-07-01

### Sources Searched

- Catawba College/YouGov June 2026 North Carolina survey release and accompanying Excel crosstab workbook.
- Echelon Insights/NetChoice April 2026 national antitrust survey topline PDF with state oversamples in Florida, Ohio, Georgia, Iowa, and Maine.
- Public polling tables and cited source pages for Texas Senate, Texas governor, Iowa governor, and Pennsylvania governor.
- Emerson College Polling March 2026 New Hampshire release and linked Google Sheets full results.
- Saint Anselm College Survey Center March 2026 New Hampshire registered voter PDF.
- Public race polling pages and web searches for newly released June/July 2026 Senate and governor polls in the modeled states.

### Polls Applied

- `catawba-yougov_nc_sen_2026-06-01_2026-06-10_yougov-27` -> `nc_sen`
  - Pollster: Catawba College/YouGov.
  - Field dates: 2026-06-01 to 2026-06-10; model field date stored as 2026-06-10.
  - Source workbook sheet: `US Senate Likely Voter`.
  - Candidate A: Michael Whatley (Republican). Candidate B: Roy Cooper (Democrat).
  - Party-ID/self-identification crosstabs applied:
    - Republican self-ID, n=289: Whatley 0.7197, Cooper 0.1038.
    - Democratic self-ID, n=303: Whatley 0.0990, Cooper 0.8251.
    - Independent self-ID, n=275: Whatley 0.2291, Cooper 0.5018.
  - Caveat: the ballot included Libertarian Shannon W. Bray, another candidate, and undecided response options; the Kalman observation uses only the two major-party candidate shares and leaves the remaining response mass unassigned.

### Topline-Only Polls Applied

These rows did not publish usable Party ID crosstabs in the reviewed public source. They were applied as aggregate ballot-test observations using the model's current electorate weights.

- `tpor_tx_sen_2026-04-17_2026-04-20_topline` -> `tx_sen`: Texas Public Opinion Research, n=1,018 LV, Paxton 0.41, Talarico 0.46.
- `slingshot_tx_gov_2026-04-17_2026-04-20_topline` -> `tx_gov`: Slingshot Strategies, n=1,018 LV, Abbott 0.48, Hinojosa 0.43.
- `echelon_netchoice_oh_gov_2026-04-03_2026-04-09_topline` -> `oh_gov`: Echelon Insights/NetChoice, n=413 LV, Ramaswamy 0.49, Acton 0.44.
- `echelon_netchoice_oh_sen_2026-04-03_2026-04-09_topline` -> `oh_sen`: Echelon Insights/NetChoice, n=413 LV, Husted 0.51, Brown 0.45.
- `echelon_netchoice_ga_gov_2026-04-03_2026-04-09_topline` -> `ga_gov`: Echelon Insights/NetChoice, n=407 LV, Jackson 0.43, Bottoms 0.49.
- `echelon_netchoice_ga_sen_2026-04-03_2026-04-09_topline` -> `ga_sen`: Echelon Insights/NetChoice, n=407 LV, Collins 0.44, Ossoff 0.51.
- `echelon_netchoice_ia_sen_2026-04-03_2026-04-09_topline` -> `ia_sen`: Echelon Insights/NetChoice, n=377 LV, Hinson 0.45, Turek 0.46.
- `cygnal_ia_gov_2026-06-16_2026-06-19_topline` -> `ia_gov`: Cygnal, n=600 LV, Lahn 0.43, Sand 0.48.
- `susquehanna_pa_gov_2026-03-18_2026-03-29_topline` -> `pa_gov`: Susquehanna Polling & Research, n=700 LV, Garrity 0.36, Shapiro 0.58.

### Polls Skipped As Duplicates

- None.

### Polls Found Without Clear Party-ID Crosstabs

- Emerson College Polling New Hampshire, March 21-23, 2026: Senate general-election toplines and linked full results were reviewed, but the crosstab variable available in the workbook is party registration, not party-ID self-identification, so it was not applied.
- Saint Anselm College Survey Center New Hampshire, March 16-18, 2026: Senate and governor general-election tables include Democratic, Republican, and `Swing` party-identification rows. Because `Swing` is not the modeled independent party-ID bucket and subgroup sample sizes by party-ID were not clear in the weighted tables, these were logged but not applied.
- Topline-only polls above were applied as aggregate observations, not Party ID observations. They should be replaced or supplemented if source crosstab workbooks become available.

### Unclassified Polls

- None.

### Extraction Uncertainties

- Catawba/YouGov workbook percentages and counts are weighted. The applied subgroup sample sizes are the weighted counts from the `Total` row of `US Senate Likely Voter`.
- No source-specific parser was added; poll rows were normalized manually into `data/ingestion/2026_normalized_polls.json` after inspecting the public source material.
