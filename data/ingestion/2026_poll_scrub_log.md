# 2026 Poll Crosstab Scrub Log

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
