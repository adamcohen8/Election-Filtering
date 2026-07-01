# 2026 Poll Crosstab Scrub Log

## 2026-07-01

### Sources Searched

- Catawba College/YouGov June 2026 North Carolina survey release and accompanying Excel crosstab workbook.
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

### Polls Skipped As Duplicates

- None.

### Polls Found Without Clear Party-ID Crosstabs

- Emerson College Polling New Hampshire, March 21-23, 2026: Senate general-election toplines and linked full results were reviewed, but the crosstab variable available in the workbook is party registration, not party-ID self-identification, so it was not applied.
- Saint Anselm College Survey Center New Hampshire, March 16-18, 2026: Senate and governor general-election tables include Democratic, Republican, and `Swing` party-identification rows. Because `Swing` is not the modeled independent party-ID bucket and subgroup sample sizes by party-ID were not clear in the weighted tables, these were logged but not applied.

### Unclassified Polls

- None.

### Extraction Uncertainties

- Catawba/YouGov workbook percentages and counts are weighted. The applied subgroup sample sizes are the weighted counts from the `Total` row of `US Senate Likely Voter`.
- No source-specific parser was added; the only applied poll was normalized manually into `data/ingestion/2026_normalized_polls.json` after inspecting the official workbook.
