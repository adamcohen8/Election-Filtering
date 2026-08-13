# 2026 Poll Crosstab Scrub Log

## 2026-08-13

### Sources Searched

- RealClearPolling latest polls page, reviewed August 13, 2026: `https://www.realclearpolling.com/latest-polls`.
- Elon University Poll August 12, 2026 North Carolina poll page, release, and public topline/methodology PDF: `https://www.elon.edu/u/elon-poll/` and `https://eloncdn.blob.core.windows.net/eu3/sites/819/2026/08/Elon-University-Poll-Topline-8-12-26.pdf`.
- Fox News / RealClearPolling-surfaced Maine Senate source path for the August 12, 2026 Collins vs. Jackson row, plus the Fox News official polls page and targeted searches for a public Maine Senate crosstab PDF or methodology file.
- Targeted web searches for August 12-13, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs, including searches for Fox Maine Senate, Elon North Carolina Senate, Cygnal Texas governor, and newly released generic-ballot crosstabs.

### Crosstab-Backed Polls Applied

- `elon-yougov_nc_sen_2026-07-23_2026-07-31_crosstab` -> `nc_sen`: Elon University/YouGov, July 23-31, 2026. The supplemental likely-voter topline is Whatley 0.42, Cooper 0.53, n=466. Party-ID crosstabs are public registered-voter rows with explicit subgroup Ns: Republican n=228, Democratic n=229, Independent n=260. Candidate A is Republican Michael Whatley; candidate B is Democrat Roy Cooper.

### Polls Skipped As Duplicates

- The August 12 Economist/YouGov generic-ballot row remained already present in the seen ledger.
- The recent crosstab-backed Carolina Forward North Carolina Senate, TSU/YouGov Texas Senate and governor, Emerson Iowa Senate and governor, AARP Arizona governor, and prior Economist/YouGov generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Fox News / Maine Senate, surfaced by RealClearPolling August 12, 2026: Troy Jackson 48, Susan Collins 46. Targeted searches, Fox News poll-page review, and direct static Fox filename probes did not locate an inspectable public source with complete Republican, Democratic, and Independent candidate-share crosstabs, so this row was not normalized or applied.
- Cygnal / Texas governor, July 29-31, 2026, n=800 likely voters: Abbott 49, Hinojosa 46. The public memo remains excluded because it does not provide complete R/D/I candidate-share crosstabs for the governor ballot.
- Quantus Insights / Georgia governor, Texas Pulse / Texas A&M Bush School Texas Senate and governor, and recent generic-ballot rows remained excluded unless already ingested from a crosstab-backed public source because reviewed public sources did not expose complete R/D/I candidate-share crosstabs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied. The Elon University/YouGov North Carolina Senate poll used explicit public registered-voter party-ID subgroup Ns.

### Unclassified Or Not Applied

- Fox News / Maine governor was not applied because Maine governor is not in the modeled governor race set.
- New York governor, South Carolina Senate Republican primary, Oklahoma governor Republican runoff, Trump approval, direction-of-country, 2028 nomination, and non-modeled primary rows on RealClearPolling are outside the modeled general-election race set.

### Extraction Uncertainties

- The Elon University/YouGov extraction uses registered-voter party-ID crosstab rows for the model inputs and the likely-voter topline as supplemental display metadata. The public PDF labels crosstabs as registered-voter row percentages and prints explicit 3-point Party ID subgroup Ns.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-12

### Sources Searched

- RealClearPolling latest polls page, reviewed August 12, 2026: `https://www.realclearpolling.com/latest-polls`.
- The Economist/YouGov August 7-10, 2026 crosstab PDF surfaced by RealClearPolling for the generic congressional ballot: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_pKJG0WT.pdf`.
- Cygnal Texas statewide polling memo surfaced by RealClearPolling for Texas governor: `https://www.cygn.al/wp-content/uploads/2026/08/Abbott-Data-Center-Plan-Memo.pdf`.
- Targeted web searches for August 11-12, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs, including searches for Cygnal Texas governor crosstabs.

### Crosstab-Backed Polls Applied

- `economist-yougov_us_house_generic_2026-08-07_2026-08-10_crosstab` -> `us_house_generic`: The Economist/YouGov, August 7-10, 2026, n=1,419 voters for the RCP-visible generic-ballot topline, Republican candidate 0.40, Democratic candidate 0.46. Party-ID subgroup Ns are explicit in the PDF: Republican n=452, Democratic n=523, Independent n=613.

### Polls Skipped As Duplicates

- Prior crosstab-backed Economist/YouGov generic-ballot rows, including July 31-August 3, remained already present in the seen ledger.
- The August 6-11 crosstab-backed rows already in the ledger remained unchanged: TSU/YouGov Texas Senate and governor, Emerson Iowa Senate and governor, AARP Arizona governor, and Carolina Forward/Change Research North Carolina Senate.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Cygnal / Texas governor, July 29-31, 2026, n=800 likely voters: Abbott 49, Hinojosa 46. The public one-page memo gives the aggregate ballot and party splits for data-center issue questions, but not complete Republican, Democratic, and Independent candidate-share crosstabs for the governor ballot, so it was not normalized or applied.
- Quantus Insights / Georgia governor remained excluded because no public complete R/D/I candidate-share crosstab table, methodology file, workbook, or PDF was found.
- Texas Pulse / Texas A&M Bush School Texas Senate and Texas governor remained excluded because reviewed public sources provide aggregate toplines and limited independent splits, but not complete R/D/I candidate-share crosstabs.
- Marquette, Quantus, Reuters/Ipsos, and other recent generic-ballot rows remained excluded unless already ingested from a crosstab-backed public source because reviewed public sources did not expose complete R/D/I candidate-share crosstabs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied. The Economist/YouGov generic-ballot poll used explicit unweighted party-ID subgroup Ns from the public PDF.

### Unclassified Or Not Applied

- South Carolina Senate special Republican primary, Oklahoma governor Republican runoff, Trump approval, direction-of-country, 2028 nomination, and non-modeled primary rows on RealClearPolling are outside the modeled general-election race set.
- No new modeled Senate or governor poll with usable public R/D/I candidate-share crosstabs was found.

### Extraction Uncertainties

- The Economist/YouGov extraction uses the table's `Voters` column for the supplemental topline because it matches the RealClearPolling-visible 46-40 generic-ballot result; R/D/I party-ID shares and subgroup Ns come from the same table's Party ID columns.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-11

### Sources Searched

- RealClearPolling latest polls page, reviewed August 11, 2026: `https://www.realclearpolling.com/latest-polls`.
- Carolina Forward / Change Research August 2026 North Carolina poll article, public toplines, and public crosstab workbook: `https://carolinaforward.org/news/the-august-2026-carolina-forward-poll/` and `https://docs.google.com/spreadsheets/d/12jBv6OEkJoo97MzXh8HOxR8ihcOmm-iGQun2ND467uI/edit?usp=sharing`.
- Quantus Insights Georgia governor source surfaced by RealClearPolling, reviewed August 11, 2026: `https://quantusinsights.org/polling/f/georgia-voters-put-affordability-first-as-2026-races-tighten`.
- Targeted web searches for August 10-11, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `carolina-forward-change-research_nc_sen_2026-08-03_2026-08-06_crosstab` -> `nc_sen`: Carolina Forward/Change Research, August 3-6, 2026, n=915 likely voters, Whatley 0.4293, Cooper 0.5005. The public statewide crosstab workbook gives Party Identification columns and explicit weighted subgroup bases: Republican n=400, Democratic n=389, Pure independent n=122. The record treats `Pure ind` as Independent.

### Polls Skipped As Duplicates

- The August 6-8 crosstab-backed rows already in the ledger remained unchanged: TSU/YouGov Texas Senate and governor, Economist/YouGov generic ballot, Emerson Iowa Senate and governor, and AARP Arizona governor.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Quantus Insights / Georgia governor, surfaced by RealClearPolling August 10, 2026: Lance Bottoms 46, Jackson 45. The RealClearPolling source link resolved only to the Quantus page title in the public text view, and targeted searches did not locate a public PDF, methodology file, workbook, or complete R/D/I candidate-share crosstab table, so this row was not normalized or applied.
- Texas Pulse / Texas A&M Bush School Texas Senate and Texas governor remained excluded. The public PDF and search-surfaced articles provide aggregate toplines and limited independent splits, but not complete R/D/I candidate-share crosstabs.
- Marquette, Quantus, Reuters/Ipsos, and other recent generic-ballot rows remained excluded unless already ingested from a crosstab-backed public source because reviewed public sources did not expose complete R/D/I candidate-share crosstabs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied. The Carolina Forward/Change Research North Carolina Senate poll used explicit weighted subgroup Ns from the public workbook.

### Unclassified Or Not Applied

- South Carolina Senate special Republican primary, Oklahoma governor Republican runoff, Trump approval, direction-of-country, and 2028 nomination rows on RealClearPolling are outside the modeled general-election race set.
- No new national generic congressional ballot poll with usable public R/D/I candidate-share crosstabs was found.

### Extraction Uncertainties

- The Carolina Forward workbook labels the independent party-ID column as `Pure ind`; it was mapped to the model's Independent party-ID bucket.
- The North Carolina Senate extraction uses the workbook's `U.S. Senate Ballot (with leans)` rows to match the RealClearPolling-visible 50-43 topline.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-10

### Sources Searched

- RealClearPolling latest polls page, reviewed August 10, 2026: `https://www.realclearpolling.com/latest-polls`.
- Targeted web searches for August 9-10, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.
- Houston Chronicle and other search-surfaced articles about the Texas Pulse / Texas A&M Bush School Texas Senate and governor toplines, checked for any newly linked public crosstab file.

### Crosstab-Backed Polls Applied

- None. No newly released modeled-race poll with complete public Republican, Democratic, and Independent candidate-share crosstabs was found after the August 9 scrub.

### Polls Skipped As Duplicates

- The August 6-8 crosstab-backed rows already in the ledger remained unchanged: TSU/YouGov Texas Senate and governor, Economist/YouGov generic ballot, Emerson Iowa Senate and governor, and AARP Arizona governor.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Texas Pulse / Texas A&M Bush School Texas Senate and Texas governor remained excluded. The public PDF and newly surfaced news articles provide aggregate toplines and limited independent splits, but not complete R/D/I candidate-share crosstabs.
- Change Research / North Carolina Senate remained excluded because no public complete R/D/I candidate-share crosstab table was found.
- Marquette and Quantus generic-ballot rows remained excluded because reviewed public sources did not expose complete R/D/I candidate-share crosstabs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied.

### Unclassified Or Not Applied

- South Carolina Senate special Republican primary and Minnesota Senate/governor primary rows on RealClearPolling remain outside the modeled general-election race set.
- No new national generic congressional ballot poll with usable public R/D/I candidate-share crosstabs was found.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no new qualifying public source was located.
- Model and public forecast exports were refreshed from the existing 42 crosstab-backed records.

## 2026-08-09

### Sources Searched

- RealClearPolling latest polls page, reviewed August 9, 2026: `https://www.realclearpolling.com/latest-polls`.
- Targeted web searches for August 8-9, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.
- Previously reviewed August 7 Texas Pulse / Texas A&M Texas Senate and governor source path and Change Research North Carolina Senate source path were checked against the latest RealClearPolling surface for any newly exposed crosstab link.

### Crosstab-Backed Polls Applied

- None. No newly released modeled-race poll with complete public Republican, Democratic, and Independent candidate-share crosstabs was found after the August 8 catch-up.

### Polls Skipped As Duplicates

- `emerson_ia_sen_2026-08-02_2026-08-04_crosstab`, `emerson_ia_gov_2026-08-02_2026-08-04_crosstab`, and `aarp-fabrizio-impact_az_gov_2026-07-26_2026-07-28_assumed_n` remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Texas Pulse / Texas A&M Bush School Texas Senate and Texas governor remained excluded because the public PDF exposes toplines and limited independent splits but not complete R/D/I candidate-share crosstabs; the referenced `Crosstabs.TexasPulse.org` disclosure host was not available during the prior scrub.
- Change Research / North Carolina Senate remained excluded because the public post did not expose complete R/D/I candidate-share crosstabs.
- Marquette and Quantus generic-ballot rows remained excluded because reviewed public sources did not expose complete R/D/I candidate-share crosstabs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied.

### Unclassified Or Not Applied

- South Carolina Senate special Republican primary and Minnesota Senate/governor primary rows on RealClearPolling remain outside the modeled general-election race set.
- No new national generic congressional ballot poll with usable public R/D/I candidate-share crosstabs was found.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no new qualifying public source was located.
- Model and public forecast exports were refreshed from the existing 42 crosstab-backed records.

## 2026-08-08

### Sources Searched

- RealClearPolling latest polls page, reviewed August 8, 2026: `https://www.realclearpolling.com/latest-polls`.
- Emerson College Iowa poll release and full-results workbook, fielded August 2-4, 2026: `https://emersoncollegepolling.com/iowa-2026-poll/`.
- AARP Arizona governor poll PDF, fielded July 26-28, 2026: `https://www.aarp.org/content/dam/aarp/research/topics/voter-opinion-research/politics/2026-midterm-election-poll-arizona.doi.10.26419-2fres.01065.007.pdf`.
- Texas Pulse / Texas A&M Bush School poll PDF, released August 7, 2026: `https://reconmr.com/wp-content/uploads/2026/08/Texas-Pulse-August-Release-August-7-2026-Final.pdf`.
- Gary Pearce / Change Research North Carolina Senate poll post, published August 6, 2026: `https://garypearcenc.substack.com/p/cooper-up-by-9-trump-still-slumps`.
- Targeted web searches for August 7-8, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `emerson_ia_sen_2026-08-02_2026-08-04_crosstab` -> `ia_sen`: Emerson College, August 2-4, 2026, n=712 likely voters, Hinson 0.4752, Turek 0.4498. The full-results workbook gives party-registration rows and explicit weighted subgroup bases: Republican n=283, Democratic n=222, Independent/other n=206.
- `emerson_ia_gov_2026-08-02_2026-08-04_crosstab` -> `ia_gov`: Emerson College, August 2-4, 2026, n=712 likely voters, Lahn 0.4269, Sand 0.4837. The full-results workbook gives party-registration rows and explicit weighted subgroup bases: Republican n=283, Democratic n=222, Independent/other n=206.
- `aarp-fabrizio-impact_az_gov_2026-07-26_2026-07-28_assumed_n` -> `az_gov`: AARP/Fabrizio Ward/Impact Research, July 26-28, 2026, n=913 likely voters, Biggs 0.44, Hobbs 0.52. The detailed findings give GOP, Independent, and Democratic party-column candidate shares, but not exact subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 228.

### Polls Skipped As Duplicates

- The TSU/YouGov Texas Senate and governor rows and the Economist/YouGov July 31-August 3 generic-ballot row applied on August 6 remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Texas Pulse / Texas A&M Bush School Texas Senate, July 27-30, 2026, n=619 likely voters: Talarico 47, Paxton 43. The PDF gives toplines and an independent split, but not complete Republican, Democratic, and Independent candidate shares. The disclosed crosstab host printed in the PDF, `Crosstabs.TexasPulse.org`, did not resolve during this scrub, so this row was not normalized or applied.
- Texas Pulse / Texas A&M Bush School Texas governor, July 27-30, 2026, n=619 likely voters: Abbott 46, Hinojosa 45. The PDF does not expose complete R/D/I candidate-share crosstabs and the referenced crosstab host did not resolve, so this row was not normalized or applied.
- Change Research / North Carolina Senate, July 29-August 1, 2026, n=967 North Carolina voters: Cooper 50, Whatley 41. The public post says detailed results will be shared later and does not expose complete R/D/I candidate-share crosstabs, so this row was not normalized or applied.
- Marquette and Quantus generic-ballot rows from August 5 remained excluded because reviewed public sources did not expose complete R/D/I candidate-share crosstabs.

### Polls Applied With Assumed Subgroup Ns

- `aarp-fabrizio-impact_az_gov_2026-07-26_2026-07-28_assumed_n`: total N / 4 = 228 for each R/D/I subgroup.

### Unclassified Or Not Applied

- South Carolina Senate special Republican primary and Minnesota Senate/governor primary rows on RealClearPolling are outside the modeled general-election race set.
- No new national generic congressional ballot poll with usable public R/D/I candidate-share crosstabs was found after the August 6 scrub.

### Extraction Uncertainties

- Emerson's public workbook labels the crosstab variable as party registration; this matches the prior Emerson generic-ballot ingestion convention, and the record text documents the label explicitly.
- AARP Arizona reports GOP, Independent, and Democratic party columns but not party subgroup Ns; the row uses the automation's direct total N / 4 fallback and does not infer subgroup Ns from the party-composition chart.
- Texas Pulse may become ingestible if `Crosstabs.TexasPulse.org` resolves later or ReconMR posts a direct crosstab file with complete R/D/I candidate shares.

## 2026-08-06

### Sources Searched

- RealClearPolling latest polls page, reviewed August 6, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed August 6, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Texas Southern University/YouGov August 2026 Texas statewide report: `https://static1.squarespace.com/static/67aa7aa3e284b002cd6a420e/t/6a713767d4ed824b91ea090d/1785804647961/Texas%2BStatewide%2BAugust2026.pdf`.
- The Economist/YouGov July 31-August 3, 2026 crosstab PDF: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_mjKhx0z.pdf`.
- Reuters/Ipsos August 2026 generic-ballot public source path surfaced by RealClearPolling and Ipsos download paths, reviewed August 6, 2026.
- Marquette Law School July 22-29, 2026 national poll PDF: `https://law.marquette.edu/assets/community/poll/MLSPSC34/MLSPSC34PressRlease_NationalTopics.pdf`.
- Quantus Insights August 3-4, 2026 poll article and linked technical report/crosstabs PDF: `https://quantusinsights.org/polling/f/latest-survey-democrats-hold-the-midterm-edge` and `https://drive.google.com/file/d/1q08S1PDsI_-805Uj_sRI3Nt1Cvr7CgsY/view?usp=sharing`.
- Associated Press Michigan primary results article used to update nominee metadata: `https://apnews.com/article/c957db07eb78ea93c70208ba0a6bceed`.
- PollingSource 2026 Senate polling page, reviewed August 6, 2026: `https://pollingsource.com/senate/polls`.
- Targeted web searches for August 5-6, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs, including Michigan post-primary general-election polling.

### Crosstab-Backed Polls Applied

- `tsu-yougov_tx_sen_2026-07-27_2026-07-30_assumed_n` -> `tx_sen`: Texas Southern University/YouGov, July 27-30, 2026, n=1,200 likely voters, Paxton 0.45, Talarico 0.47. Table 1 gives Republican, Democratic, and Independent candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 300.
- `tsu-yougov_tx_gov_2026-07-27_2026-07-30_assumed_n` -> `tx_gov`: Texas Southern University/YouGov, July 27-30, 2026, n=1,200 likely voters, Abbott 0.49, Hinojosa 0.43. Table 2 gives Republican, Democratic, and Independent candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 300.
- `economist-yougov_us_house_generic_2026-07-31_2026-08-03_crosstab` -> `us_house_generic`: The Economist/YouGov, July 31-August 3, 2026, n=1,472 voters for the RCP-visible generic-ballot topline, Republican candidate 0.42, Democratic candidate 0.46. Party-ID subgroup Ns are explicit in the PDF: Republican n=464, Democratic n=537, Independent n=606.

### Polls Skipped As Duplicates

- `wick_ga_gov_2026-06-27_2026-06-30_crosstab`, `wick_ga_sen_2026-06-27_2026-06-30_crosstab`, `tpor_tx_sen_2026-07-15_2026-07-17_assumed_n`, `fox_tx_sen_2026-07-23_2026-07-27_assumed_n`, `fox_nc_sen_2026-07-23_2026-07-27_assumed_n`, and `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n` remained already present in the seen ledger.
- Reuters/Ipsos July 24-26, Economist/YouGov July 25-27, and the existing July crosstab-backed generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Marquette Law School / generic congressional ballot, July 22-29, 2026, published by RealClearPolling August 5: Democrats 51, Republicans 45 among likely voters. The public PDF includes aggregate generic-ballot results and party-ID turnout certainty, but not R/D/I party-ID candidate shares for the ballot question, so it was not normalized or applied.
- Quantus Insights / generic congressional ballot, August 3-4, 2026, n=1,048 likely voters: Democrats 49.0, Republicans 42.6. The public article and linked PDF include the aggregate ballot result, response counts, and party-ID composition, but not ballot choice crossed by R/D/I party ID, so it was not normalized or applied.
- Reuters/Ipsos / generic congressional ballot, published by RealClearPolling August 4, 2026: Democrats 42, Republicans 37. The reviewed Reuters path and Ipsos wrapper/download paths did not expose a directly inspectable public PDF/table with complete R/D/I party-ID candidate shares during this scrub, so it was not normalized or applied.
- Wedgewood Polls / Texas Senate, surfaced by PollingSource with a July 31, 2026 field date, remained excluded because targeted searches did not locate a public release, PDF, methodology file, or R/D/I party-ID crosstab table.
- Big Data Poll, CNN/SSRS, and Manhattan Institute generic-ballot rows remained excluded for the same missing-complete-party-ID-crosstab reasons logged in prior scrubs.
- PennLive / Pennsylvania governor and Morning Consult / generic congressional ballot remained excluded for the same missing-complete-party-ID-crosstab reasons logged in prior scrubs.

### Polls Applied With Assumed Subgroup Ns

- `tsu-yougov_tx_sen_2026-07-27_2026-07-30_assumed_n`: total N / 4 = 300 for each R/D/I subgroup.
- `tsu-yougov_tx_gov_2026-07-27_2026-07-30_assumed_n`: total N / 4 = 300 for each R/D/I subgroup.

### Unclassified Or Not Applied

- Michigan nominee metadata was updated after the August 4, 2026 primary: `mi_sen` now tracks Mike Rogers (R) vs. Abdul El-Sayed (D), and `mi_gov` now tracks John James (R) vs. Jocelyn Benson (D).
- EPIC-MRA / Michigan Senate Rogers vs. El-Sayed and Michigan governor James vs. Benson rows remain not applied because no public complete R/D/I party-ID crosstab table was found.
- MIRS/Mitchell Research / Michigan Senate Rogers vs. El-Sayed and Michigan governor James vs. Benson rows remain not applied because no public complete R/D/I party-ID crosstab table was found.
- WFSB-TV/CT Insider / Connecticut governor Democratic primary, South Carolina Senate special Republican primary, Florida governor Republican primary, Michigan primary-only rows, Wisconsin governor Democratic primary, and 2028 presidential nomination rows are outside the modeled general-election race set.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.

### Extraction Uncertainties

- TSU/YouGov party shares were extracted from Tables 1 and 2 of the public PDF. Exact subgroup Ns were not public, so the records use the total N / 4 fallback, not any inferred party composition from the report's partisan profile.
- Economist/YouGov party-ID shares and subgroup Ns were extracted from the PDF's `Generic Congressional Vote` table. The supplemental topline uses the RCP-visible voters result, corresponding to the PDF's `Voters` column.
- Quantus's linked PDF was rendered for visual inspection because PDF text extraction was blank; the rendered pages showed no ballot-choice-by-party-ID table for the generic ballot.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-04

### Sources Searched

- RealClearPolling latest polls page, reviewed August 4, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed August 4, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- PollingSource 2026 Senate polling page, reviewed August 4, 2026: `https://pollingsource.com/senate/polls`.
- Dave Leip's Atlas 2026 governor polling page was checked again, but the site returned a 403 response during this scrub: `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for August 3-4, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs, including EPIC-MRA Michigan, Wedgewood Polls Texas Senate, Economist/YouGov, Quinnipiac, and Napolitan/RMG generic-ballot searches.

### Crosstab-Backed Polls Applied

- None. No newly released modeled-race poll with complete public Republican, Democratic, and Independent party-ID candidate shares was found.

### Polls Skipped As Duplicates

- `wick_ga_gov_2026-06-27_2026-06-30_crosstab`, `wick_ga_sen_2026-06-27_2026-06-30_crosstab`, `tpor_tx_sen_2026-07-15_2026-07-17_assumed_n`, `fox_tx_sen_2026-07-23_2026-07-27_assumed_n`, `fox_nc_sen_2026-07-23_2026-07-27_assumed_n`, and `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n` remained already present in the seen ledger.
- Reuters/Ipsos July 24-26, Economist/YouGov July 25-27, and the existing July crosstab-backed generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Wedgewood Polls / Texas Senate, surfaced by PollingSource with a July 31, 2026 field date, n=800 likely voters: Talarico 48, Paxton 46. Targeted searches again did not locate a public release, PDF, methodology file, or R/D/I party-ID crosstab table, so it was not normalized or applied.
- Big Data Poll / generic congressional ballot, published by RealClearPolling July 30, 2026, remained excluded because no current public complete R/D/I party-ID candidate table was accessible.
- CNN/SSRS / generic congressional ballot, published by RealClearPolling July 30, 2026, remained excluded because the reviewed public article and linked DocumentCloud path did not expose complete Republican, Democratic, and Independent party-ID candidate shares in an accessible public table.
- Manhattan Institute / generic congressional ballot, fielded July 1-6 and published by RealClearPolling July 27, 2026, remained excluded because the public topline PDF does not include R/D/I party-ID candidate shares for the ballot question.
- PennLive / Pennsylvania governor and Morning Consult / generic congressional ballot remained excluded for the same missing-complete-party-ID-crosstab reasons logged in prior scrubs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today.

### Unclassified Or Not Applied

- WFSB-TV/CT Insider / Connecticut governor Democratic primary, published by RealClearPolling August 3, 2026, is outside the modeled race set.
- EPIC-MRA / Michigan Senate and Michigan governor August 2, 2026 alternate matchup rows remained not applied because `mi_sen` and `mi_gov` lack settled nominee metadata and no public complete R/D/I party-ID crosstab table was found.
- South Carolina Senate special Republican primary, Florida governor Republican primary, Michigan Senate Democratic primary, Michigan governor Republican primary, Wisconsin governor Democratic primary, and 2028 presidential nomination rows are outside the modeled general-election race set.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new crosstab-backed release was located.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-03

### Sources Searched

- RealClearPolling latest polls page, reviewed August 3, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed August 3, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- PollingSource 2026 Senate polling page, reviewed August 3, 2026: `https://pollingsource.com/senate/polls`.
- Dave Leip's Atlas 2026 governor polling page was checked again, but the site returned a 403 response during this scrub: `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for August 2-3, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs, including EPIC-MRA Michigan and Wedgewood Polls Texas Senate searches.

### Crosstab-Backed Polls Applied

- None. No newly released modeled-race poll with complete public Republican, Democratic, and Independent party-ID candidate shares was found.

### Polls Skipped As Duplicates

- `wick_ga_gov_2026-06-27_2026-06-30_crosstab`, `wick_ga_sen_2026-06-27_2026-06-30_crosstab`, `tpor_tx_sen_2026-07-15_2026-07-17_assumed_n`, `fox_tx_sen_2026-07-23_2026-07-27_assumed_n`, `fox_nc_sen_2026-07-23_2026-07-27_assumed_n`, and `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n` remained already present in the seen ledger.
- Reuters/Ipsos July 24-26, Economist/YouGov July 25-27, and the existing July crosstab-backed generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Wedgewood Polls / Texas Senate, surfaced by PollingSource with a July 31, 2026 field date, n=800 likely voters: Talarico 48, Paxton 46. Targeted searches did not locate a public release, PDF, methodology file, or R/D/I party-ID crosstab table, so it was not normalized or applied.
- Big Data Poll / generic congressional ballot, published by RealClearPolling July 30, 2026, remained excluded because no current public complete R/D/I party-ID candidate table was accessible.
- CNN/SSRS / generic congressional ballot, published by RealClearPolling July 30, 2026, remained excluded because the reviewed public article and linked DocumentCloud path did not expose complete Republican, Democratic, and Independent party-ID candidate shares in an accessible public table.
- Manhattan Institute / generic congressional ballot, fielded July 1-6 and published by RealClearPolling July 27, 2026, remained excluded because the public topline PDF does not include R/D/I party-ID candidate shares for the ballot question.
- PennLive / Pennsylvania governor and Morning Consult / generic congressional ballot remained excluded for the same missing-complete-party-ID-crosstab reasons logged in prior scrubs.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today.

### Unclassified Or Not Applied

- EPIC-MRA / Michigan Senate, published by RealClearPolling August 2, 2026: Rogers 46, El-Sayed 43; Stevens 44, Rogers 42. These rows were not applied because they are alternate matchups for `mi_sen`, the repo has no settled nominee metadata for the Democratic nominee, and no public complete R/D/I party-ID crosstab table was found in this scrub.
- EPIC-MRA / Michigan governor, published by RealClearPolling August 2, 2026: Benson 48, Johnson 36; Benson 47, James 38. These rows were not applied because they are alternate matchups for `mi_gov`, the repo has no settled Republican nominee metadata, and no public complete R/D/I party-ID crosstab table was found in this scrub.
- South Carolina Senate special Republican primary, Florida governor Republican primary, Michigan Senate Democratic primary, Michigan governor Republican primary, Wisconsin governor Democratic primary, and 2028 presidential nomination rows are outside the modeled general-election race set.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new crosstab-backed release was located.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-02

### Sources Searched

- RealClearPolling latest polls page, reviewed August 2, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed August 2, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Wick Research Georgia Statewide Poll resources page and complete crosstab workbook, reviewed August 2, 2026: `https://wick.io/research-georgia-election-survey-june-2026-questionnaire`.
- Big Data Poll generic ballot page, reviewed August 2, 2026: `https://www.bigdatapoll.com/project/generic-ballot/`.
- Manhattan Institute July welfare poll topline PDF, surfaced on the RealClearPolling House feed and reviewed August 2, 2026: `https://media4.manhattan-institute.org/wp-content/uploads/sites/5/Manhattan_Institute_July_Welfare_Toplines.pdf`.
- PollingSource 2026 Senate polling page and Dave Leip's Atlas 2026 governor polling page, reviewed August 2, 2026: `https://pollingsource.com/senate/polls` and `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for August 1-2, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `wick_ga_gov_2026-06-27_2026-06-30_crosstab` -> `ga_gov`: Wick Research, June 27-30, 2026, n=1,175 likely voters, Jackson 0.432, Lance Bottoms 0.427. The public complete crosstab workbook gives Party ID candidate shares and weighted subgroup bases on sheet `Q9 Governor Ballot`: Republican n=459, Democratic n=405, Independent n=253.
- `wick_ga_sen_2026-06-27_2026-06-30_crosstab` -> `ga_sen`: Wick Research, June 27-30, 2026, n=1,175 likely voters, Collins 0.429, Ossoff 0.467. The public complete crosstab workbook gives Party ID candidate shares and weighted subgroup bases on sheet `Q11 Senate Ballot`: Republican n=459, Democratic n=405, Independent n=253.

### Polls Skipped As Duplicates

- `tpor_tx_sen_2026-07-15_2026-07-17_assumed_n`, `fox_tx_sen_2026-07-23_2026-07-27_assumed_n`, `fox_nc_sen_2026-07-23_2026-07-27_assumed_n`, and `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n` remained already present in the seen ledger.
- Reuters/Ipsos July 24-26, Economist/YouGov July 25-27, and the existing July crosstab-backed generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Big Data Poll / generic congressional ballot, published by RealClearPolling July 30, 2026: Democrats 50, Republicans 39. The reviewed public project page states that interactive crosstabs are available on MarketSight with each press release, but no current public complete R/D/I party-ID candidate table was accessible in this scrub, so it was not normalized or applied.
- CNN/SSRS / generic congressional ballot, published by RealClearPolling July 30, 2026, remained excluded because the reviewed public article and linked DocumentCloud path did not expose complete Republican, Democratic, and Independent party-ID candidate shares in an accessible public table.
- Manhattan Institute / generic congressional ballot, fielded July 1-6 and published by RealClearPolling July 27, 2026: Democrats 47, Republicans 43. The public topline PDF includes aggregate generic-ballot results and party-ID composition, but not R/D/I party-ID candidate shares for the ballot question, so it was not normalized or applied.
- PennLive / Pennsylvania governor, published by RealClearPolling July 29, 2026, remained excluded because the reviewed public source/search path did not expose complete Republican, Democratic, and Independent party-ID candidate shares.
- Morning Consult / generic congressional ballot, published by RealClearPolling July 27, 2026, remained excluded because the reviewed public tracker path did not expose complete Republican, Democratic, and Independent party-ID candidate shares.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today. The Wick Georgia records use explicit weighted subgroup bases from the public workbook.

### Unclassified Or Not Applied

- MIRS/Mitchell July 31, 2026 Michigan Senate and Michigan governor general-election rows remained not applied because the RCP feed includes alternate matchups for the same `mi_sen` and `mi_gov` contests, and the repo has no settled nominee metadata for those race IDs.
- South Carolina Senate special Republican primary, Florida governor Republican primary, Michigan Senate Democratic primary, Michigan governor Republican primary, Wisconsin governor Democratic primary, and 2028 presidential nomination rows are outside the modeled general-election race set.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.

### Extraction Uncertainties

- Wick workbook bases are weighted column bases, as printed in the workbook. The applied R/D/I subgroup Ns are those weighted bases, not unweighted respondent counts.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-08-01

### Sources Searched

- RealClearPolling latest polls page, reviewed August 1, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed August 1, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Texas Tribune July 28, 2026 TPOR Texas Senate article: `https://www.texastribune.org/2026/07/28/texas-senate-poll-james-talarico-ken-paxton-july-2026/`.
- Texas Public Opinion Research Substack advisory path surfaced by RealClearPolling and targeted searches: `https://texaspublicopinionresearch.substack.com/`.
- Big Data Poll generic ballot page, reviewed August 1, 2026: `https://www.bigdatapoll.com/project/generic-ballot/`.
- MIRS/Mitchell Michigan Senate and governor rows surfaced by RealClearPolling's July 31 latest-polls feed and targeted searches for public crosstabs.
- PollingSource 2026 Senate polling page and Dave Leip's Atlas 2026 governor polling page, reviewed August 1, 2026: `https://pollingsource.com/senate/polls` and `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for July 31-August 1, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `tpor_tx_sen_2026-07-15_2026-07-17_assumed_n` -> `tx_sen`: Texas Public Opinion Research, July 15-17, 2026, n=1,048 likely voters, Paxton 0.40, Talarico 0.45. The Texas Tribune public report gives Republican, Democratic, and Independent candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 262.

### Polls Skipped As Duplicates

- `fox_tx_sen_2026-07-23_2026-07-27_assumed_n`, `fox_nc_sen_2026-07-23_2026-07-27_assumed_n`, and `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n` remained already present in the seen ledger from the July 31 scrub.
- `economist-yougov_us_house_generic_2026-07-25_2026-07-27_crosstab`, Reuters/Ipsos July 24-26, and the existing July crosstab-backed generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Big Data Poll / generic congressional ballot, published by RealClearPolling July 30, 2026: Democrats 50, Republicans 39. The reviewed public project page states that interactive crosstabs are available on MarketSight with each press release, but no current public complete R/D/I party-ID candidate table was accessible in this scrub, so it was not normalized or applied.
- CNN/SSRS / generic congressional ballot, published by RealClearPolling July 30, 2026, remained excluded because the reviewed public article and linked DocumentCloud path did not expose complete Republican, Democratic, and Independent party-ID candidate shares in an accessible public table.
- PennLive / Pennsylvania governor, published by RealClearPolling July 29, 2026, remained excluded because the reviewed public source/search path did not expose complete Republican, Democratic, and Independent party-ID candidate shares.
- Morning Consult / generic congressional ballot, published by RealClearPolling July 27, 2026, remained excluded because the reviewed public tracker path did not expose complete Republican, Democratic, and Independent party-ID candidate shares.

### Polls Applied With Assumed Subgroup Ns

- `tpor_tx_sen_2026-07-15_2026-07-17_assumed_n`: total N / 4 = 262 for each R/D/I subgroup.

### Unclassified Or Not Applied

- MIRS/Mitchell July 31, 2026 Michigan Senate and Michigan governor general-election rows were not applied because the RCP feed includes alternate matchups for the same `mi_sen` and `mi_gov` contests, and the repo has no settled nominee metadata for those race IDs. Applying multiple variants would double-count the poll; selecting one would be arbitrary.
- South Carolina Senate special Republican primary, Florida governor Republican primary, Michigan Senate Democratic primary, Michigan governor Republican primary, and 2028 presidential nomination rows are outside the modeled general-election race set.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.

### Extraction Uncertainties

- TPOR party shares were extracted from the Texas Tribune public article text. Exact subgroup Ns were not public, so the record uses the total N / 4 fallback, not any inferred party composition or subgroup margin of error.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-31

### Sources Searched

- RealClearPolling latest polls page, reviewed July 31, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed July 31, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Fox News July 23-27, 2026 Texas poll article: `https://www.foxnews.com/politics/fox-news-poll-gop-divisions-shape-texas-senate-race`.
- Fox News July 23-27, 2026 North Carolina topline and crosstab PDFs: `https://static.foxnews.com/foxnews.com/content/uploads/2026/07/fox_july-23-27-2026_north-carolina_topline_july-29-release.pdf` and `https://static.foxnews.com/foxnews.com/content/uploads/2026/07/fox_july-23-27-2026_north-carolina_cross-tabs_july-29-release.pdf`.
- Quinnipiac University July 23-27, 2026 national release PDF: `https://poll.qu.edu/images/polling/us/us07292026_uhgq69.pdf`.
- CNN/SSRS July 2026 generic congressional ballot public article and linked DocumentCloud path, reviewed July 31, 2026.
- PennLive July 2026 Pennsylvania governor poll path surfaced by RealClearPolling, reviewed July 31, 2026.
- PollingSource 2026 Senate polling page and Dave Leip's Atlas 2026 governor polling page, reviewed July 31, 2026: `https://pollingsource.com/senate/polls` and `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for July 30-31, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `fox_tx_sen_2026-07-23_2026-07-27_assumed_n` -> `tx_sen`: Fox News, July 23-27, 2026, n=1,006 registered voters, Paxton 0.48, Talarico 0.51. The public article gives Republican, Democratic, and Independent candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 252.
- `fox_nc_sen_2026-07-23_2026-07-27_assumed_n` -> `nc_sen`: Fox News, July 23-27, 2026, n=1,005 registered voters, Whatley 0.44, Cooper 0.53. The crosstab PDF gives Republican, Democratic, and Independent candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 251.
- `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n` -> `us_house_generic`: Quinnipiac University, July 23-27, 2026, n=963 registered voters, Republican Party 0.41, Democratic Party 0.48. The release gives Republican, Democratic, and Independent party-ID crosstab shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 241.

### Polls Skipped As Duplicates

- `economist-yougov_us_house_generic_2026-07-25_2026-07-27_crosstab`, Reuters/Ipsos July 24-26, and the existing July generic-ballot crosstab rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- CNN/SSRS / generic congressional ballot, published by RealClearPolling July 30, 2026: Democrat 47, Republican 39. The reviewed public article and linked DocumentCloud path did not expose complete Republican, Democratic, and Independent party-ID candidate shares in an accessible public table, so it was not normalized or applied.
- PennLive / Pennsylvania governor, published by RealClearPolling July 29, 2026: Shapiro 53, Garrity 28. The reviewed public source/search path did not expose complete Republican, Democratic, and Independent party-ID candidate shares, so it was not normalized or applied.
- Morning Consult / generic congressional ballot, published by RealClearPolling July 27, 2026, remained excluded because the reviewed public tracker path did not expose complete Republican, Democratic, and Independent party-ID candidate shares.

### Polls Applied With Assumed Subgroup Ns

- `fox_tx_sen_2026-07-23_2026-07-27_assumed_n`: total N / 4 = 252 for each R/D/I subgroup.
- `fox_nc_sen_2026-07-23_2026-07-27_assumed_n`: total N / 4 = 251 for each R/D/I subgroup.
- `quinnipiac_us_house_generic_2026-07-23_2026-07-27_assumed_n`: total N / 4 = 241 for each R/D/I subgroup.

### Unclassified Or Not Applied

- Fox News / Texas governor, July 23-27, 2026: Abbott 0.50, Hinojosa 0.49. The reviewed public Texas article gave the topline and some crossover/support detail but did not expose complete R/D/I candidate shares for the governor ballot test, so it was not normalized or applied.
- RealClearPolling's July 30 Iowa and New Hampshire items were 2028 presidential primary rows, outside the modeled 2026 race set.
- RealClearPolling's July 29 Montana Senate row remains outside the modeled state list.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.

### Extraction Uncertainties

- Fox Texas Senate party shares were extracted from the public article text. Because the article prints party support shares but not subgroup Ns, the record uses the total N / 4 fallback, not any inferred party composition.
- Fox North Carolina Senate party shares were extracted from the public crosstab PDF. The PDF provides party candidate shares but not subgroup Ns, so the total N / 4 fallback is used.
- Quinnipiac's release prints the party-ID candidate shares for the generic House ballot but not exact subgroup Ns; the record uses the total N / 4 fallback.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-30

### Sources Searched

- RealClearPolling latest polls page, reviewed July 30, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed July 30, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- The Economist/YouGov July 25-27, 2026 crosstab PDF, rechecked as the latest RCP-visible crosstab-backed generic-ballot row already applied on July 29: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_0t0YpHo.pdf`.
- YouGov survey-results page and Fox News poll archive, reviewed July 30, 2026: `https://yougov.com/en-us/survey-results` and `https://www.foxnews.com/official-polls/fox-news-poll-archive`.
- PollingSource 2026 Senate polling page and Dave Leip's Atlas 2026 governor polling page, reviewed July 30, 2026: `https://pollingsource.com/senate/polls` and `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Rasmussen Reports Mood of America and generic-ballot archive pages, reviewed July 30, 2026: `https://www.rasmussenreports.com/public_content/politics/mood_of_america` and `https://www.rasmussenreports.com/public_content/archive/mood_of_america_archive/generic_congressional_ballot/`.
- Targeted web searches for July 29-30, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- None. No newly released modeled Senate, governor, or national generic congressional ballot poll with usable Republican, Democratic, and Independent party-ID candidate shares was found after the July 29 scrub.

### Polls Skipped As Duplicates

- `economist-yougov_us_house_generic_2026-07-25_2026-07-27_crosstab` remained already applied from the July 29 scrub.
- Reuters/Ipsos July 24-26 and the existing July crosstab-backed generic-ballot rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- No newly released aggregate-topline-only modeled-race poll was found after the July 29 scrub.
- Morning Consult / generic congressional ballot, published by RealClearPolling July 27, 2026, remained excluded because the reviewed public tracker path did not expose complete Republican, Democratic, and Independent party-ID candidate shares.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today.

### Unclassified Or Not Applied

- RealClearPolling's visible July 29-30 additions were presidential approval, direction-of-country, and presidential nomination rows, not modeled 2026 election ballot tests.
- PollingSource's newest visible Senate row remained Montana Senate, outside the modeled state list.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.
- Dave Leip's Atlas governor polling page did not surface a newer modeled governor poll than the already reviewed July 17 University of North Florida row.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no new qualifying modeled-race release was located.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-29

### Sources Searched

- RealClearPolling latest polls page, reviewed July 29, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed July 29, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- The Economist/YouGov July 25-27, 2026 crosstab PDF: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_0t0YpHo.pdf`.
- YouGov survey-results page for current source-document discovery, reviewed July 29, 2026: `https://yougov.com/en-us/survey-results`.
- Fox News poll archive, reviewed July 29, 2026: `https://www.foxnews.com/official-polls/fox-news-poll-archive`.
- PollingSource 2026 Senate polling page and Dave Leip's Atlas 2026 governor polling page, reviewed July 29, 2026: `https://pollingsource.com/senate/polls` and `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for July 28-29, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `economist-yougov_us_house_generic_2026-07-25_2026-07-27_crosstab` -> `us_house_generic`: The Economist/YouGov, July 25-27, 2026, n=1,405 voters for the RCP-visible generic-ballot topline, Republican candidate 0.42, Democratic candidate 0.46. Party-ID subgroup Ns are explicit in the PDF: Republican n=439, Democratic n=513, Independent n=605.

### Polls Skipped As Duplicates

- Previously applied Economist/YouGov generic-ballot rows through July 20, Reuters/Ipsos July 24-26, and the other existing crosstab-backed modeled-race rows remained already present in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Morning Consult / generic congressional ballot, published by RealClearPolling July 27, 2026: Democrat 46, Republican 43. The reviewed public tracker path remained aggregate-topline-only and did not expose complete Republican, Democratic, and Independent party-ID candidate shares, so it was not normalized or applied.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today. The Economist/YouGov row used explicit subgroup Ns printed in the crosstab PDF.

### Unclassified Or Not Applied

- RealClearPolling's July 28 presidential nomination and job-approval rows are outside the modeled 2026 race set.
- PollingSource's newest July 27 Senate row was a Montana Senate poll, outside the modeled state list.
- PollingSource's latest House-district rows are district-specific and not the modeled national `us_house_generic` race.
- Dave Leip's Atlas governor polling page did not surface a newer modeled governor poll than the already reviewed July 17 University of North Florida row.

### Extraction Uncertainties

- The Economist/YouGov PDF reports the full generic-ballot table among adult citizens, plus a `Voters` column that matches the RCP-visible 46-42 Democratic lead. The record uses the `Voters` column as supplemental topline metadata and the printed Dem/Ind/Rep Party ID columns for the model update.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-28

### Sources Searched

- RealClearPolling latest polls page, reviewed July 28, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed July 28, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Reuters/Ipsos July Core Political release and topline PDF, reviewed July 28, 2026: `https://www.ipsos.com/en-us/americans-unimpressed-ideas-both-major-parties` and `https://www.ipsos.com/sites/default/files/ct/news/documents/2026-07/Reuters%20Ipsos%20July%20Core%20Political%20Topline%207.27.26.pdf`.
- PollingSource 2026 Senate and House polling pages, reviewed July 28, 2026: `https://pollingsource.com/senate.php` and `https://pollingsource.com/house/`.
- Dave Leip's Atlas 2026 governor polling page, reviewed July 28, 2026: `https://uselectionatlas.org/POLLS/GOVERNOR/2026/polls.php`.
- Targeted web searches for July 27-28, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- `reuters-ipsos_us_house_generic_2026-07-24_2026-07-26_crosstab` -> `us_house_generic`: Reuters/Ipsos July Core Political, July 24-26, 2026, n=1,003 registered voters for the RCP-visible generic-ballot topline, Republican candidate 0.38, Democratic candidate 0.40. Party-ID subgroup Ns are explicit in the topline PDF: Republican n=385, Democratic n=384, Independent/Something else/Other n=479.

### Polls Skipped As Duplicates

- Previously applied July 17-20 through July 23 generic-ballot rows from Economist/YouGov, Fox News, Emerson, Pew, AARP/Fabrizio/Impact Georgia, and other existing modeled-race rows remained in the seen ledger.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- No newly released aggregate-topline-only modeled-race poll was found after the July 27 scrub. The previously logged Daily Mail generic congressional ballot row remained RCP-visible without public complete R/D/I crosstabs and was not normalized or applied.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today. The Reuters/Ipsos row used explicit subgroup Ns printed in the topline PDF.

### Unclassified Or Not Applied

- RealClearPolling's July 27 Daily Mail and Rasmussen rows for 2028 presidential nomination are outside the modeled 2026 race set.
- RealClearPolling's July 26 South Carolina Senate Republican special primary remains outside the modeled general-election race list.
- PollingSource's latest district-specific House rows are not the modeled national `us_house_generic` race.
- Dave Leip's Atlas governor polling page did not surface a newer modeled governor poll than the already reviewed July 17 University of North Florida row.

### Extraction Uncertainties

- Reuters/Ipsos provides the RCP-visible generic-ballot topline among registered voters, while the party-ID crosstab columns in the topline PDF are labeled by Republican, Democrat, and Independent/Something else/Other respondents with explicit unweighted subgroup Ns. The record uses the registered-voter topline as display metadata and the printed party-ID crosstab columns for the model update.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-27

### Sources Searched

- RealClearPolling latest polls page, reviewed July 27, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed July 27, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Vote-Scope generic ballot polling table, reviewed July 27, 2026: `https://vote-scope.com/en/us/house/polls/`.
- Silver Bulletin generic congressional ballot tracker, reviewed July 27, 2026: `https://www.natesilver.net/p/generic-ballot-average-2026-nate-silver-bulletin-congress-polls`.
- PollingSource 2026 Senate polls and 2026 House polling overview, reviewed July 27, 2026: `https://pollingsource.com/senate/polls` and `https://pollingsource.com/house/`.
- Targeted web searches for July 26-27, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- None. No newly released modeled Senate, governor, or national generic congressional ballot poll with usable Republican, Democratic, and Independent party-ID candidate shares was found after the July 26 scrub.

### Polls Skipped As Duplicates

- Existing July 23 AARP/Fabrizio/Impact Georgia Senate and Governor, Emerson national generic ballot, Pew national generic ballot, and July 22 Fox national generic ballot rows remained already applied.
- Existing July 22 Marquette Wisconsin governor alternate-matchup rows remained already reviewed and not applied because the repo still has no settled `wi_gov` nominee metadata.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- No newly released aggregate-topline-only modeled-race poll was found after the July 26 scrub. The previously logged Daily Mail generic congressional ballot row remained RCP-visible as an aggregate Democratic lead without public complete R/D/I crosstabs, so it was not normalized or applied.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today.

### Unclassified Or Not Applied

- RealClearPolling's July 27 additions were Rasmussen presidential job approval and direction-of-country rows, not modeled election ballot tests.
- RealClearPolling's July 26 South Carolina Senate Republican special primary row is not a modeled general-election race.
- PollingSource's latest House-district rows are district-specific, not the modeled national `us_house_generic` race.
- Vote-Scope's generic-ballot table still lists July 20, 2026 as the most recent fieldwork in the current visible table; no newer national generic ballot was applied.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no new qualifying modeled-race release was located.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-26

### Sources Searched

- RealClearPolling latest polls page, reviewed July 26, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate, Governor, House, and generic congressional vote pages, reviewed July 26, 2026: `https://www.realclearpolling.com/latest-polls/senate`, `https://www.realclearpolling.com/latest-polls/governor`, `https://www.realclearpolling.com/latest-polls/house`, and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Silver Bulletin generic congressional ballot tracker, reviewed July 26, 2026: `https://www.natesilver.net/p/generic-ballot-average-2026-nate-silver-bulletin-congress-polls`.
- Vote-Scope generic ballot polling table, reviewed July 26, 2026: `https://vote-scope.com/en/us/house/polls/`.
- Targeted web searches for July 24-26, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Crosstab-Backed Polls Applied

- None. No newly released modeled Senate, governor, or national generic congressional ballot poll with usable Republican, Democratic, and Independent party-ID candidate shares was found after the July 24 scrub.

### Polls Skipped As Duplicates

- July 23 AARP/Fabrizio/Impact Georgia Senate and Governor, Emerson national generic ballot, Pew national generic ballot, and July 22 Fox national generic ballot remained already applied from the July 24 scrub.
- July 22 Marquette Wisconsin governor alternate-matchup rows remained already reviewed and not applied for the same reason logged on July 24.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- No newly released aggregate-topline-only modeled-race poll was found after the July 24 scrub. The previously logged Daily Mail generic congressional ballot row remained without public complete R/D/I crosstabs and was not normalized or applied.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today.

### Unclassified Or Not Applied

- RealClearPolling's July 24 additions were president/job-approval or issue-approval rows, not modeled election ballot tests.
- Primary-only and non-modeled races visible on RealClearPolling's latest surfaces remained outside the modeled general-election race list.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no new qualifying modeled-race release was located.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-24

### Sources Searched

- RealClearPolling latest polls page, reviewed July 24, 2026: `https://www.realclearpolling.com/latest-polls`.
- AARP / Fabrizio Ward / Impact Research Georgia July 13-16, 2026 detailed findings PDF: `https://www.aarp.org/content/dam/aarp/research/topics/voter-opinion-research/politics/2026-midterm-election-poll-georgia.doi.10.26419-2fres.01065.004.pdf`.
- Emerson College July 19-20, 2026 national poll release and public full-results workbook: `https://emersoncollegepolling.com/july-2026-national-poll-democrats-with-11-point-generic-ballot-advantage/`.
- Fox News July 17-20, 2026 national poll article and crosstab PDF: `https://www.foxnews.com/politics/fox-news-poll-voters-want-major-change-amid-economic-political-discontent` and `https://static.foxnews.com/foxnews.com/content/uploads/2026/07/fox_july-17-20-2026_national_cross-tabs_july-22-release.pdf`.
- Pew Research Center July 6-12, 2026 midterm voting preference report and detailed table workbook: `https://www.pewresearch.org/politics/2026/07/23/as-the-2026-midterms-approach-economy-is-front-and-center/`.
- Marquette Law School July 9-16, 2026 Wisconsin poll release and crosstab tables: `https://law.marquette.edu/poll/2026/07/22/marquette-law-school-poll-finds-almost-half-of-democratic-primary-voters-undecided-amid-rapid-shifts-in-the-race-for-the-gubernatorial-nomination/`.
- Targeted web searches for July 22-24, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs, including Daily Mail / J.L. Partners generic-ballot crosstab searches.

### Crosstab-Backed Polls Applied

- `aarp-fabrizio-impact_ga_sen_2026-07-13_2026-07-16_assumed_n` -> `ga_sen`: AARP/Fabrizio Ward/Impact Research, July 13-16, 2026, n=1,060 likely voters, Collins 0.43, Ossoff 0.52. The detailed findings give GOP, Independent, and Democratic candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 265.
- `aarp-fabrizio-impact_ga_gov_2026-07-13_2026-07-16_assumed_n` -> `ga_gov`: AARP/Fabrizio Ward/Impact Research, July 13-16, 2026, n=1,060 likely voters, Jackson 0.46, Lance Bottoms 0.48. The detailed findings give GOP, Independent, and Democratic candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 265.
- `emerson_us_house_generic_2026-07-19_2026-07-20_crosstab` -> `us_house_generic`: Emerson College, July 19-20, 2026, n=1,100 likely 2026 voters, Republican candidate 0.4149, Democratic candidate 0.5287. The public workbook gives explicit weighted party-registration bases, rounded here as Republican n=371, Democratic n=353, Independent/other n=376.
- `fox_us_house_generic_2026-07-17_2026-07-20_assumed_n` -> `us_house_generic`: Fox News, July 17-20, 2026, n=1,003 registered voters, Republican candidate 0.46, Democratic candidate 0.53. The crosstab PDF gives R/D/I party-ID candidate shares, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 251.
- `pew_us_house_generic_2026-07-06_2026-07-12_assumed_n` -> `us_house_generic`: Pew Research Center, July 6-12, 2026, n=2,779 registered voters, Republican candidate 0.37, Democratic candidate 0.43. The detailed tables give Republican, Democrat, and NET Independent/Other rows, but not subgroup Ns; each R/D/I subgroup n uses the total N / 4 fallback = 695.

### Polls Skipped As Duplicates

- Existing July 17-20 Economist/YouGov generic-ballot and July 15-20 UNH Maine Senate rows remained already applied from the July 22 scrub.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Daily Mail / generic congressional ballot, published by RealClearPolling July 23, 2026: Democrat 52, Republican 43. Targeted public searches did not surface complete Republican, Democratic, and Independent party-ID candidate shares, so it was not normalized or applied.

### Polls Applied With Assumed Subgroup Ns

- `aarp-fabrizio-impact_ga_sen_2026-07-13_2026-07-16_assumed_n`: total N / 4 = 265 for each R/D/I subgroup.
- `aarp-fabrizio-impact_ga_gov_2026-07-13_2026-07-16_assumed_n`: total N / 4 = 265 for each R/D/I subgroup.
- `fox_us_house_generic_2026-07-17_2026-07-20_assumed_n`: total N / 4 = 251 for each R/D/I subgroup.
- `pew_us_house_generic_2026-07-06_2026-07-12_assumed_n`: total N / 4 = 695 for each R/D/I subgroup.

### Unclassified Or Not Applied

- AARP Georgia generic congressional ballot was treated as a state-level generic ballot rather than the modeled national `us_house_generic` race, so it was not normalized or applied.
- Marquette Law School Wisconsin governor ballot tests were not applied because the same poll includes alternate Democratic matchups against Tom Tiffany (including Mandela Barnes and Francesca Hong) and the repo has no settled `wi_gov` nominee metadata. Applying multiple variants would double-count one survey; choosing one variant would be arbitrary.
- Rasmussen, primary-only rows, and non-modeled state races visible in latest-polls surfaces were outside the modeled general-election race list.

### Extraction Uncertainties

- AARP, Fox, and Pew subgroup sample sizes use the user's total N / 4 fallback because the reviewed public tables provide party candidate shares without exact R/D/I subgroup Ns.
- Pew's Independent row is labeled `NET Ind/Other (includes leaners)` in the detailed tables; it was mapped to Independent because it is the only public non-Republican/non-Democratic party grouping for the generic House ballot.

## 2026-07-22

### Sources Searched

- RealClearPolling latest polls page, reviewed July 22, 2026: `https://www.realclearpolling.com/latest-polls`.
- University of New Hampshire Survey Center July 21, 2026 Maine release PDF: `https://scholars.unh.edu/cgi/viewcontent.cgi?article=1980&context=survey_center_polls`.
- University of North Florida PORL July 20, 2026 Florida statewide release and accessible crosstab workbook: `https://www.unfporl.org/presser-page` and `https://www.unfporl.org/s/PORL-2026-Summer-Statewide-Xtabs-ADA.xlsx`.
- The Economist/YouGov July 17-20, 2026 crosstab PDF: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_ESdiNMa.pdf`.
- Morning Consult Political Intelligence / midterm ballot public tracker path surfaced by RealClearPolling: `https://pro-assets.morningconsult.com/wp-uploads/2026/06/MCPI-PI-Weekly_260622.html`.
- Targeted web searches for July 20-22, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Polls Applied

- `unh_me_sen_2026-07-15_2026-07-20_crosstab` -> `me_sen`: University of New Hampshire, July 15-20, 2026, n=1,168 likely general-election voters for the Collins-vs-Jackson table, Collins 0.46, Jackson 0.49. Party-ID subgroup Ns are explicit in the UNH table: Republican n=433, Democratic n=575, Independent n=149.
- `unf_fl_gov_2026-07-08_2026-07-17_crosstab` -> `fl_gov`: University of North Florida PORL, July 8-17, 2026, n=848 likely midterm voters, Donalds 0.461, Jolly 0.414. Party-registration subgroup Ns are explicit in the accessible workbook: Republican n=425, Democratic n=250, NPA/Oth n=173; NPA/Oth is normalized as Independent.
- `economist-yougov_us_house_generic_2026-07-17_2026-07-20_crosstab` -> `us_house_generic`: The Economist/YouGov, July 17-20, 2026, n=1,432 voters for the RCP-visible generic-ballot topline, Republican 0.41, Democratic 0.46. Party-ID subgroup Ns are explicit in the PDF: Republican n=451, Democratic n=545, Independent n=606.

### Polls Skipped As Duplicates

- No newly surfaced July 20-22 crosstab-backed modeled-race poll duplicated an existing `poll_id`.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- Morning Consult / generic congressional ballot, published by RealClearPolling July 20, 2026: Democrat 46, Republican 43. The RCP-linked public tracker path showed the aggregate D+3 ballot reference but did not expose complete Republican, Democratic, and Independent party-ID candidate shares in the reviewed public text, so it was not normalized or applied.

### Polls Applied With Assumed Subgroup Ns

- None. All three applied July 22 records had explicit subgroup Ns in the reviewed source tables.

### Unclassified Or Not Applied

- University of New Hampshire / Maine governor, published by RealClearPolling July 21, 2026: Pingree 49, Charles 35, Bennett 6. The repo does not currently model `me_gov`, so it was not normalized or applied.
- KSTP/SurveyUSA Minnesota Senate and governor primary polls, Rasmussen job approval rows, and Cygnal Florida governor Republican primary were visible in the latest-polls feed but are outside the modeled general-election race set.
- University of North Florida / Florida Senate special election: Moody 50 vs. Vindman 40 and Moody 50 vs. Nixon 42. The workbook has party-registration crosstabs, but it contains two alternate Democratic matchups for the same `fl_sen` race. To avoid double-counting one poll with two competing Democratic ballot tests, neither Senate variant was applied in this run.

### Extraction Uncertainties

- The UNH PDF required manual extraction from embedded PDF text streams because ordinary local PDF text tools were unavailable. The extracted Collins-vs-Jackson party-ID table was cross-checked against the narrative statement that 88% of Democrats support Jackson, 99% of Republicans support Collins, and a plurality of Independents support Jackson.
- UNF uses party registration columns (`Dem`, `Rep`, `NPA/Oth`) rather than self-reported party ID. The row was applied because the automation accepts clear R/D/I-like party group candidate shares, and NPA/Oth was mapped to Independent.
- Maine Senate is now included in the automation prompt and the repo's modeled race registry; older log notes saying Maine Senate was outside the model are superseded by the Troy Jackson nominee update.

## 2026-07-20

### Sources Searched

- RealClearPolling latest polls page, reviewed July 20, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 20, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 20, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 20, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Targeted web searches for July 19-20, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Polls Applied

- None. No newly released modeled-race poll with clear Republican, Democratic, and Independent party-ID candidate shares was found after the July 19 run.

### Polls Skipped As Duplicates

- Washington Post/Ipsos July 8-13, 2026 generic House ballot remained already applied through `washington-post-ipsos_us_house_generic_2026-07-08_2026-07-13_assumed_n`.
- CNBC July 17, 2026 generic ballot, RMG Research July 15, 2026 generic ballot, Echelon July 9-13, 2026 generic ballot, Quinnipiac July 9-13 Pennsylvania governor/generic House, PPP July 10-11 North Carolina Senate, Fox Iowa/Georgia, and older explicit-crosstab rows remained already reviewed, ingested where usable, or logged as insufficient.

### Aggregate Topline-Only Polls Found Without Party-ID Crosstabs

- CNBC / generic congressional ballot, published by RealClearPolling July 17, 2026: Democrat 49, Republican 45. No public R/D/I party-ID candidate shares were found in the reviewed public source path or targeted searches, so it remained excluded.
- RMG Research / generic congressional ballot, published by RealClearPolling July 15, 2026: Democrat 47, Republican 45. Public crosstabs remain restricted/confidential, so it remained excluded.

### Polls Applied With Assumed Subgroup Ns

- None newly applied today. The existing assumed-N records from the July 19 policy backfill remained in the normalized feed.

### Unclassified Polls

- South Carolina Senate Republican special primary, Michigan Senate Democratic primary, PPIC California governor, and South Dakota governor GOP runoff remained visible in latest polling pages but are not modeled general-election races.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no new qualifying modeled-race release was located.
- No aggregate-topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-19 Assumed-N Policy Backfill

### Sources Searched

- Existing scrub log entries and git history for polls previously skipped or removed because party-ID shares were available but exact subgroup sample sizes were not public.
- Fox News Iowa and Georgia June 23-27, 2026 public releases and prior normalized rows.
- Public Policy Polling North Carolina July 10-11, 2026 full results PDF: `https://e1.nmcdn.io/assets/ppp/wp-content/uploads/2026/07/NorthCarolinaPollJuly2026.pdf`.
- Quinnipiac Pennsylvania July 9-13, 2026 release and question tables: `https://poll.qu.edu/poll-release?releaseid=3962`.
- Washington Post/Ipsos July 8-13, 2026 public registered-voter crosstab workbook: `https://docs.google.com/spreadsheets/d/1U1aahGHx-oKANEspTjAX7RmTIAgYV5wjzr_hKLHfFNk/edit?gid=0`.
- Rasmussen Reports July 7, 2026 generic-ballot release, reviewed again for whether all R/D/I two-candidate shares were public: `https://www.rasmussenreports.com/public_content/politics/mood_of_america/generic_congressional_ballot_july07`.

### Polls Applied

- `fox_ia_sen_2026-06-23_2026-06-27_assumed_n` -> `ia_sen`: Fox News, June 23-27, 2026, n=1,003 registered voters, Hinson 0.46, Turek 0.50. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 251 each using total N / 4.
- `fox_ia_gov_2026-06-23_2026-06-27_assumed_n` -> `ia_gov`: Fox News, June 23-27, 2026, n=1,003 registered voters, Lahn 0.44, Sand 0.53. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 251 each using total N / 4.
- `fox_ga_sen_2026-06-23_2026-06-27_assumed_n` -> `ga_sen`: Fox News, June 23-27, 2026, n=1,002 registered voters, Collins 0.43, Ossoff 0.56. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 251 each using total N / 4.
- `fox_ga_gov_2026-06-23_2026-06-27_assumed_n` -> `ga_gov`: Fox News, June 23-27, 2026, n=1,002 registered voters, Jackson 0.47, Lance Bottoms 0.52. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 251 each using total N / 4.
- `ppp_nc_sen_2026-07-10_2026-07-11_assumed_n` -> `nc_sen`: Public Policy Polling, July 10-11, 2026, n=759 voters, Whatley 0.44, Cooper 0.48. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 190 each using total N / 4.
- `quinnipiac_pa_gov_2026-07-09_2026-07-13_assumed_n` -> `pa_gov`: Quinnipiac University, July 9-13, 2026, n=895 registered voters, Garrity 0.40, Shapiro 0.53. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 224 each using total N / 4.
- `quinnipiac_us_house_generic_2026-07-09_2026-07-13_assumed_n` -> `us_house_generic`: Quinnipiac University Pennsylvania generic House preference, July 9-13, 2026, n=895 registered voters, Republican Party 0.43, Democratic Party 0.49. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 224 each using total N / 4.
- `washington-post-ipsos_us_house_generic_2026-07-08_2026-07-13_assumed_n` -> `us_house_generic`: Washington Post/Ipsos, July 8-13, 2026, n=2,092 registered voters, Republican candidate 0.45, Democratic candidate 0.48. Exact party-ID subgroup Ns were not public; R/D/I subgroup Ns were set to 523 each using total N / 4.

### Polls Skipped As Duplicates

- Previously ingested crosstab-backed rows with explicit or already accepted subgroup bases remained unchanged.

### Polls Still Found Without Clear Party-ID Crosstabs

- Rasmussen Reports July 7, 2026 generic-ballot release remained excluded after review. It publishes total N and some party-group preference percentages, but not all Republican, Democratic, and Independent two-candidate shares needed by `PartyIDCrosstab`.
- Morning Consult, CNBC, and A2 Insights rows remained excluded because the reviewed public material did not expose full R/D/I two-candidate party-ID shares for all three groups.

### Unclassified Polls

- Fox Maine Senate remained excluded because Maine Senate is not in the modeled race list.

### Extraction Uncertainties

- This backfill implements the user's July 19 instruction to assume `total N / 4` when R/D/I party-ID candidate shares are public but subgroup sizes are missing.
- Assumed subgroup sample sizes are deliberately not inferred from party-composition percentages or subgroup MOEs; every applied fallback row uses the same integer sample size for Republican, Democratic, and Independent party-ID groups.

## 2026-07-19

### Sources Searched

- RealClearPolling latest polls page, reviewed July 19, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 19, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 19, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 19, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Washington Post/Ipsos July 8-13, 2026 article and public crosstab workbook: `https://www.washingtonpost.com/politics/2026/07/18/democrats-have-slim-lead-race-house-washington-post-ipsos-poll-finds/` and `https://docs.google.com/spreadsheets/d/1U1aahGHx-oKANEspTjAX7RmTIAgYV5wjzr_hKLHfFNk/edit?gid=0`.
- Ipsos public methodology page for the Washington Post/Ipsos July 2026 poll: `https://www.ipsos.com/en-us/Washington-Post-Ipsos-Poll-July-2026`.
- Targeted web searches for July 18-19, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Polls Applied

- None. No newly released modeled-race poll with usable Republican, Democratic, and Independent party-ID crosstabs and subgroup sample sizes was found.

### Polls Skipped As Duplicates

- The July 9-13 Echelon Insights generic-ballot crosstab, July 10-13 Economist/YouGov generic-ballot crosstab, July 9-10 2Way/HarrisX generic-ballot crosstab, and older NYT/Siena Senate crosstabs remain already ingested.

### Polls Found Without Clear Party-ID Crosstabs

- Washington Post/Ipsos / generic congressional ballot, published by RealClearPolling July 18, 2026: Democrat 48, Republican 45 among registered voters. The public workbook includes Party ID shares for Democrats, Republicans, and Indep/Other voters, but it does not publish explicit subgroup sample sizes; it publishes subgroup margins of error instead. Because subgroup Ns would have to be inferred from MOEs or weighting benchmarks, this poll was not normalized or applied.

### Unclassified Polls

- South Carolina Senate Republican special primary, PPIC California governor, and South Dakota governor GOP runoff remained visible in the latest RCP pages but are not modeled general-election races.

### Extraction Uncertainties

- The Washington Post/Ipsos workbook's registered-voter House ballot row shows Democratic candidate shares of 0.97 among Democrats, 0.05 among Republicans, and 0.47 among Indep/Other voters; Republican candidate shares are 0.02, 0.93, and 0.35 respectively. These shares were not ingested because the corresponding subgroup sample sizes were not public.
- No topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-18

### Sources Searched

- RealClearPolling latest polls page, reviewed July 18, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 18, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 18, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 18, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- RealClearPolling-linked CNBC July 17, 2026 generic congressional ballot source PDF path: `https://fm.cnbc.com/applications/cnbc.com/resources/editorialfiles/2026/07/17/CNBC_Q2_2026_Topline.pdf`.
- Targeted web searches for July 17-18, 2026 modeled Senate, governor, and generic congressional ballot releases with public party-ID crosstabs.

### Polls Applied

- None. No newly released modeled-race poll with usable Republican, Democratic, and Independent party-ID crosstabs and subgroup sample sizes was found.

### Polls Skipped As Duplicates

- The July 9-13 Echelon Insights generic-ballot crosstab, July 10-13 Economist/YouGov generic-ballot crosstab, July 9-10 2Way/HarrisX generic-ballot crosstab, and older NYT/Siena Senate crosstabs remain already ingested.

### Polls Found Without Clear Party-ID Crosstabs

- CNBC / generic congressional ballot, published by RealClearPolling July 17, 2026: Democrat 49, Republican 45. The RCP-linked public source is a topline PDF path, direct retrieval returned access denied, and targeted searches did not find a public crosstab file or Republican, Democratic, and Independent party-ID subgroup sample sizes. It was not normalized or applied.

### Unclassified Polls

- South Carolina Senate Republican special primary, PPIC California governor, and South Dakota governor GOP runoff remained visible in the latest RCP pages but are not modeled general-election races.

### Extraction Uncertainties

- No crosstab extraction was attempted because the only new modeled poll located was public topline-only.
- No topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-17

### Sources Searched

- RealClearPolling latest polls page, reviewed July 17, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 17, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 17, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 17, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Echelon Insights July 2026 Verified Voter Omnibus release and public crosstab workbook: `https://echeloninsights.com/insights/july-2026-verified-voter-omnibus-1` and `https://docs.google.com/spreadsheets/d/16gGhnRTle2nutw2RjHL3mnDVou3PVRzd/edit?gid=892273807`.
- Quinnipiac Pennsylvania July 15, 2026 release, release PDF, and sample/methodology PDF: `https://poll.qu.edu/poll-release?releaseid=3962`.
- Napolitan News/RMG Research July 15, 2026 generic-ballot public post and mini-toplines: `https://napolitannews.org/posts/generic-ballot-dem-47-percent-gop-45-dems-still-have-healthy-enthusiasm-edge`.
- Targeted web searches for newly released July 2026 modeled Senate, governor, and generic congressional ballot releases and party-ID crosstabs from public pollsters and aggregators.

### Polls Applied

- `echelon_us_house_generic_2026-07-09_2026-07-13_crosstab` -> `us_house_generic`: Echelon Insights, July 9-13, 2026, n=1,004 likely electorate, generic Republican 0.44, generic Democrat 0.50.
  - Republican party ID, unweighted n=350: Republican 0.94, Democrat 0.04.
  - Democratic party ID, unweighted n=393: Republican 0.01, Democrat 0.97.
  - Independent party ID, unweighted n=261: Republican 0.30, Democrat 0.52.

### Polls Skipped As Duplicates

- The July 10-13 Economist/YouGov generic-ballot crosstab, July 9-10 2Way/HarrisX generic-ballot crosstab, and older NYT/Siena Senate crosstabs remain already ingested.

### Polls Found Without Clear Party-ID Crosstabs

- Quinnipiac / Pennsylvania governor, July 9-13, 2026: Shapiro 53, Garrity 40. The release published Republican, Democratic, and Independent party-ID candidate shares, but the methodology PDF published only rounded party-composition percentages and said subgroup margins of sampling error are available upon request. Because usable subgroup sample sizes were not public, this poll was not normalized or applied.
- Quinnipiac / Pennsylvania generic House preference, July 9-13, 2026: Democratic Party 49, Republican Party 43. Same issue as above: party-ID shares were public, but public subgroup sample sizes were not.
- Napolitan News/RMG Research / generic congressional ballot, July 13-14, 2026: Democrat 47, Republican 45 including leaners. The public post states that full crosstabs are restricted/confidential and not for public release, so it was not normalized or applied.

### Unclassified Polls

- Emerson South Carolina Senate Republican special primary, July 16 RCP row: not a modeled race.
- PPIC California governor, July 16 RCP row: not a modeled governor state.
- Emerson South Dakota governor GOP runoff, July 15 RCP row: not a modeled race.

### Extraction Uncertainties

- Echelon's crosstab workbook reports weighted subgroup bases on the question row and an explicit `Unweighted Total` row. The normalized record uses the weighted candidate shares from the `Party` columns and the unweighted Republican, Independent, and Democratic subgroup counts as the sample-size inputs.
- No topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-15

### Sources Searched

- RealClearPolling latest polls page, reviewed July 15, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 15, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 15, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 15, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- The Economist/YouGov July 10-13, 2026 crosstab PDF: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_ie0SzVb.pdf`.
- Harvard CAPS/Harris July 2026 polling page and downloaded all-files bundle, reviewed July 15, 2026: `https://harvardharrispoll.com/all-polls/`.
- Morning Consult tracker page linked by RealClearPolling's July 14 generic-ballot row: `https://intel.morningconsult.com/mc-content/trackers/donald-trump-congress-policy-republicans-polling`.
- 2026 United States elections public polling table, reviewed July 15, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- Targeted web searches for newly released July 2026 modeled Senate, governor, and generic congressional ballot releases and party-ID crosstabs from major public pollsters and aggregators.

### Polls Applied

- `economist-yougov_us_house_generic_2026-07-10_2026-07-13_crosstab` -> `us_house_generic`: The Economist/YouGov, July 10-13, 2026, n=1,447 voters, generic Republican 0.42, generic Democrat 0.46.
  - Republican party ID, unweighted n=463: Republican 0.90, Democrat 0.02.
  - Democratic party ID, unweighted n=567: Republican 0.01, Democrat 0.92.
  - Independent party ID, unweighted n=582: Republican 0.15, Democrat 0.25.

### Polls Skipped As Duplicates

- The July 11 2Way/HarrisX generic-ballot crosstab and July 3-6 Economist/YouGov generic-ballot crosstab remained already ingested.
- Previously reviewed Wick Georgia Senate/Governor, Public Policy Polling North Carolina Senate, Quantus/Cygnal generic-ballot, and other topline-only rows remained logged but excluded from model inputs under the crosstab-only policy.

### Polls Found Without Clear Party-ID Crosstabs

- Morning Consult / generic congressional ballot, published by RealClearPolling July 14, 2026: Democrat 46, Republican 43. The public tracker surface did not expose Republican, Democratic, and Independent party-ID crosstabs with subgroup sample sizes, so it was not normalized or applied.
- Harvard-Harris / generic congressional ballot, published by RealClearPolling July 14, 2026: Democrat 51, Republican 49. The July 2026 Harvard CAPS/Harris all-files bundle available from the public polling page contained only a key-results PDF, not a crosstab file, so it was not normalized or applied.

### Unclassified Polls

- Detroit News/Glengariff July 14 Michigan Senate Democratic primary row was reviewed from RealClearPolling but not classified into `mi_sen` because it is a Democratic primary, not a modeled general-election ballot test.

### Extraction Uncertainties

- The Economist/YouGov crosstab row uses the PDF's `Voters` column for the aggregate result and the PDF's `Party ID` columns for subgroup shares. The subgroup Ns are the unweighted Democratic, Independent, and Republican party-ID counts printed in the same table.
- No topline-only poll IDs were added to `data/ingestion/2026_seen_polls.json`.

## 2026-07-14 Crosstab-Only Policy Correction

### Sources Searched

- No new web sources searched for this correction. This was a data-policy cleanup based on the user's instruction that polls without usable party-ID crosstabs must not be included in the model.

### Polls Applied

- None added. The normalized feed was filtered from 84 records to 10 records, retaining only polls with explicit Republican, Democratic, and Independent party-ID candidate shares plus usable subgroup sample sizes.

### Polls Removed From Model Inputs

- Removed 74 observations from `data/ingestion/2026_normalized_polls.json` and the rebuilt seen-poll ledger: 70 topline-only observations plus four Fox News rows whose party-ID subgroup sample sizes had been estimated from subgroup MOEs rather than printed. Removed rows include the July 14 Public Policy Polling North Carolina Senate topline and all previously ingested generic-ballot, Maine Senate, RCP topline, and other aggregate-only rows that lacked usable party-ID crosstabs.

### Polls Skipped As Duplicates

- None for this correction pass.

### Polls Found Without Clear Party-ID Crosstabs

- All removed topline-only records remain source-discovery evidence only. They should be logged as missing party-ID crosstabs in future scrubs, not normalized into model inputs unless Republican, Democratic, and Independent party-ID crosstab shares and usable subgroup bases or sample sizes are available.

### Unclassified Polls

- None.

### Extraction Uncertainties

- Existing crosstab-backed records that also include topline fields were retained because they have usable party-ID crosstabs; the topline fields are supplemental display metadata only.
- Added a regression test requiring every record in `data/ingestion/2026_normalized_polls.json` to include the complete R/D/I party-ID crosstab field set.

## 2026-07-14

### Sources Searched

- RealClearPolling latest polls page, reviewed July 14, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 14, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 14, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 14, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- Public Policy Polling July 13, 2026 North Carolina Senate release and full results PDF: `https://www.publicpolicypolling.com/polls/cooper-leads-but-whatley-has-a-path/` and `https://e1.nmcdn.io/assets/ppp/wp-content/uploads/2026/07/NorthCarolinaPollJuly2026.pdf`.
- 2026 United States elections public polling table, reviewed July 14, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- Targeted web searches for newly released July 2026 modeled Senate, governor, and generic congressional ballot releases and party-ID crosstabs from major public pollsters and aggregators.

### Polls Applied

- `ppp_nc_sen_2026-07-10_2026-07-11_topline` -> `nc_sen`: Public Policy Polling, July 10-11, 2026, n=759 North Carolina voters, Michael Whatley 0.44, Roy Cooper 0.48.

### Polls Skipped As Duplicates

- RealClearPolling's latest modeled generic-ballot row remained the July 11 2Way/HarrisX row already ingested on July 12.
- RealClearPolling July 8 generic-ballot rows from Quantus Insights and Cygnal remained duplicates from the July 9 generic ballot backfill.
- RealClearPolling July 7 generic-ballot rows from The Economist/YouGov, Morning Consult, and Rasmussen Reports remained represented after the July 10 run.
- RealClearPolling July 8 Wick Georgia Senate and Governor rows remained reviewed but not applied because no public sample/methodology details or crosstabs were located.
- Previously reviewed modeled Senate/governor rows from Fox News, NYT/Siena, AARP, Cygnal, UNH, St. Anselm, Noble Predictive Insights, SoCal/Red Eagle, and Morning Scrapple remained duplicates or already-reviewed entries.

### Polls Found Without Clear Party-ID Crosstabs

- Public Policy Polling / North Carolina Senate, July 10-11, 2026: the PDF includes party-ID ballot shares for Cooper vs. Whatley but does not publish explicit party-ID subgroup sample sizes. Crosstab values were reviewed as Democrat ID Cooper 0.89 / Whatley 0.09, Republican ID Cooper 0.09 / Whatley 0.79, and Independent Cooper 0.48 / Whatley 0.44, but the poll was applied as topline-only because the subgroup Ns would have to be inferred from rounded party-composition percentages.

### Unclassified Polls

- None.

### Extraction Uncertainties

- PPP reports party ID composition as Democrat 30%, Republican 31%, Independent 39% of n=759, but does not print exact subgroup sample sizes. The crosstab was therefore not used for the Kalman party-ID update.
- No newly released modeled governor or generic congressional ballot poll was located beyond rows already ingested or logged in prior runs.

## 2026-07-13

### Sources Searched

- RealClearPolling latest polls page, reviewed July 13, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 13, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 13, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 13, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- 2026 United States elections public polling table, reviewed July 13, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- Targeted web searches for newly released July 2026 modeled Senate, governor, and generic congressional ballot releases and party-ID crosstabs from major public pollsters and aggregators.

### Polls Applied

- None. No newly released public modeled Senate, governor, or generic congressional ballot poll with usable party-ID crosstabs or a new clear topline was located after the July 12 run.

### Polls Skipped As Duplicates

- RealClearPolling's latest modeled generic-ballot row remained the July 11 2Way/HarrisX row already ingested on July 12.
- RealClearPolling July 8 generic-ballot rows from Quantus Insights and Cygnal remained duplicates from the July 9 generic ballot backfill.
- RealClearPolling July 7 generic-ballot rows from The Economist/YouGov, Morning Consult, and Rasmussen Reports remained represented after the July 10 run.
- RealClearPolling July 8 Wick Georgia Senate and Governor rows remained reviewed but not applied because no public sample/methodology details or crosstabs were located.
- Previously reviewed modeled Senate/governor rows from Fox News, NYT/Siena, AARP, Cygnal, UNH, St. Anselm, Noble Predictive Insights, SoCal/Red Eagle, and Morning Scrapple remained duplicates or already-reviewed entries.

### Polls Found Without Clear Party-ID Crosstabs

- No additional newly released modeled Senate, governor, or generic congressional ballot poll without party-ID crosstabs was located beyond the Wick, Financial Times, and Daily Mail rows logged on July 11.

### Unclassified Polls

- None.

### Extraction Uncertainties

- The public 2026 United States elections polling table still did not list the July 9-10 2Way/HarrisX generic-ballot row during this run; the project already uses the HarrisX crosstab/RCP source pair from the July 12 ingestion.
- No new crosstab extraction was attempted because no new qualifying source table or release was located.

## 2026-07-12

### Sources Searched

- RealClearPolling latest polls page, reviewed July 12, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 12, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 12, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 12, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- 2Way/HarrisX July 2026 NATO Summit survey crosstab page and embedded HTML crosstab, reviewed July 12, 2026: `https://www.harrisx.com/content/july-2026-nato-summit-survey-findings-crosstabs` and `https://html-crosstabs.s3.us-east-1.amazonaws.com/HarrisX_NATO_HOP.html`.
- 2026 United States elections public polling table, reviewed July 12, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- Targeted web searches for newly released July 2026 modeled Senate, governor, and generic congressional ballot releases and party-ID crosstabs.

### Polls Applied

- `2way-harrisx_us_house_generic_2026-07-09_2026-07-10_crosstab` -> `us_house_generic`: 2Way/HarrisX, July 9-10, 2026, n=1,019 RV, forced-choice generic Republican 0.48, generic Democrat 0.52 among all registered voters. RealClearPolling reported the likely-voter forced-choice column as Republican 0.49, Democrat 0.51, n=787.
  - Republican party ID, n=379: Republican 0.95, Democrat 0.05.
  - Democratic party ID, n=358: Republican 0.02, Democrat 0.98.
  - Independent party ID, n=270: Republican 0.42, Democrat 0.58.

### Polls Skipped As Duplicates

- RealClearPolling July 8 generic-ballot rows from Quantus Insights and Cygnal remained duplicates from the July 9 generic ballot backfill.
- RealClearPolling July 7 generic-ballot rows from The Economist/YouGov, Morning Consult, and Rasmussen Reports remained represented after the July 10 run.
- RealClearPolling July 8 Wick Georgia Senate and Governor rows remained reviewed but not applied because no public sample/methodology details or crosstabs were located.
- Previously reviewed modeled Senate/governor rows from Fox News, NYT/Siena, AARP, Cygnal, UNH, St. Anselm, Noble Predictive Insights, SoCal/Red Eagle, and Morning Scrapple remained duplicates or already-reviewed entries.

### Polls Found Without Clear Party-ID Crosstabs

- No additional newly released modeled Senate, governor, or generic congressional ballot poll without party-ID crosstabs was located beyond the Wick, Financial Times, and Daily Mail rows logged on July 11.

### Unclassified Polls

- None.

### Extraction Uncertainties

- The 2Way/HarrisX crosstab page's forced-choice table gives total RV results of Democrat 52 and Republican 48, while RealClearPolling's July 11 generic-ballot row reports the likely-voter forced-choice column as Democrat 51 and Republican 49. The normalized row stores the Party ID crosstabs from the forced-choice table and the RCP/HarrisX likely-voter column as the topline for public poll display.
- The 2026 United States elections public polling table did not yet list the July 9-10 2Way/HarrisX row during this run, so the HarrisX crosstab and RealClearPolling pages were treated as the primary sources.

## 2026-07-11

### Sources Searched

- RealClearPolling latest polls page, reviewed July 11, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 11, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 11, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 11, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- RealClearPolling Georgia Senate race page, reviewed July 11, 2026: `https://www.realclearpolling.com/polls/senate/general/2026/georgia/ossoff-vs-collins`.
- RealClearPolling Georgia Governor race page, reviewed July 11, 2026: `https://www.realclearpolling.com/polls/governor/general/2026/georgia/lance-bottoms-vs-jackson`.
- Wick public site, reviewed July 11, 2026: `https://wick.io/`.
- 2026 United States elections public polling table, reviewed July 11, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- Financial Times public article linked from RealClearPolling's July 6 generic-ballot row, reviewed July 11, 2026. The page was paywalled/static-limited and did not expose a public polling table, sample size, or party-ID crosstabs.
- Targeted web searches for July 2026 Wick Georgia Senate/Governor releases, Financial Times generic-ballot releases, Daily Mail generic-ballot releases, modeled-race public polling releases, and party-ID crosstabs.

### Polls Applied

- None. No newly released public poll located in this run had both a modeled race classification and enough public sample/methodology detail to normalize a new observation safely.

### Polls Skipped As Duplicates

- RealClearPolling July 8 generic-ballot rows from Quantus Insights and Cygnal were already ingested in the July 9 generic ballot backfill.
- RealClearPolling July 7 generic-ballot rows from The Economist/YouGov, Morning Consult, and Rasmussen Reports were already represented after the July 10 run.
- Previously reviewed modeled Senate/governor rows from Fox News, NYT/Siena, AARP, Cygnal, UNH, St. Anselm, Noble Predictive Insights, SoCal/Red Eagle, and Morning Scrapple remained duplicates or already-reviewed entries.

### Polls Found Without Clear Party-ID Crosstabs

- Wick / Georgia Senate, published by RealClearPolling July 8, 2026: Ossoff 47, Collins 43. The accessible Wick site and search results did not provide field dates, sample size, margin of error, methodology, or party-ID crosstabs, so this row was not normalized or applied.
- Wick / Georgia Governor, published by RealClearPolling July 8, 2026: Lance Bottoms 43, Jackson 43. The accessible Wick site and search results did not provide field dates, sample size, margin of error, methodology, or party-ID crosstabs, so this row was not normalized or applied.
- Financial Times / generic congressional ballot, published by RealClearPolling July 6, 2026: Democrat 49, Republican 42. The accessible FT page did not expose the underlying poll table, sample size, methodology, or party-ID crosstabs, so this row was not normalized or applied.
- Daily Mail / generic congressional ballot, published by RealClearPolling July 6, 2026: Democrat 50, Republican 42. No accessible primary source or public data table with sample size, methodology, or party-ID crosstabs was located, so this row was not normalized or applied.

### Unclassified Polls

- None.

### Extraction Uncertainties

- RealClearPolling latest-poll rows provide useful discovery signals but did not expose enough structured metadata in static access for the July 8 Wick rows or July 6 Financial Times/Daily Mail generic-ballot rows. The ingestion schema requires clear sample sizes for topline-only observations, so these rows were logged but not applied.
- No party-ID crosstab extraction was attempted for the four new RCP-visible rows because the underlying public releases or tables were not accessible.

## 2026-07-10

### Sources Searched

- RealClearPolling latest polls page, reviewed July 10, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 10, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 10, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- RealClearPolling latest House polls and generic congressional vote pages, reviewed July 10, 2026: `https://www.realclearpolling.com/latest-polls/house` and `https://www.realclearpolling.com/polls/state-of-the-union/generic-congressional-vote`.
- 2026 United States elections public polling table, reviewed July 10, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- The Economist/YouGov July 3-6, 2026 crosstab PDF: `https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_Qxo6bev.pdf`.
- Morning Consult July 6, 2026 midterm ballot tracker page: `https://pro-assets.morningconsult.com/wp-uploads/2026/07/MCPI-Midterm-Ballot_260706.html`.
- Rasmussen Reports July 7, 2026 generic congressional ballot release: `https://www.rasmussenreports.com/public_content/politics/mood_of_america/generic_congressional_ballot_july07`.
- Live web searches for newly released public modeled-race Senate polls and crosstabs since the 2026-07-09 run across Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for newly released public modeled-race governor polls and crosstabs since the 2026-07-09 run across Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Pollster/source-specific searches for July 2026 modeled-race releases and party-ID crosstabs from Emerson College Polling, Quinnipiac University, Marist, SurveyUSA, Fox News, New York Times/Siena College, AARP, Cygnal, Quantus Insights, Noble Predictive Insights, RealClearPolling, Race to the WH, 270toWin, Decision Desk HQ, and generic-ballot public polling table surfaces.

### Polls Applied

- `economist-yougov_us_house_generic_2026-07-03_2026-07-06_crosstab` -> `us_house_generic`: The Economist/YouGov, July 3-6, 2026, n=1,442 voters, generic Republican 0.43, generic Democrat 0.46.
  - Republican party ID, unweighted n=436: Republican 0.89, Democrat 0.02.
  - Democratic party ID, unweighted n=547: Republican 0.01, Democrat 0.93.
  - Independent party ID, unweighted n=619: Republican 0.16, Democrat 0.29.
- `rasmussen_us_house_generic_2026-06-24_2026-07-01_topline` -> `us_house_generic`: Rasmussen Reports, June 24-25 and June 28-July 1, 2026, n=2,224 LV, generic Republican 0.42, generic Democrat 0.46.

### Polls Skipped As Duplicates

- RealClearPolling July 8 generic-ballot rows from Quantus Insights and Cygnal were already ingested in the July 9 generic ballot backfill.
- Existing modeled Senate/governor rows from Fox Iowa/Georgia, NYT/Siena, AARP Ohio, Cygnal Iowa, Morning Scrapple Pennsylvania, SoCal/Red Eagle Texas, UNH, St. Anselm, and older public table rows remained duplicates or already-reviewed entries.

### Polls Found Without Clear Party-ID Crosstabs

- Rasmussen Reports published party-group percentages but not Republican, Democratic, and Independent subgroup sample sizes in the public release, so it was applied as topline-only.
- Morning Consult's July 6 midterm ballot tracker was already represented as `morning-consult_us_house_generic_2026-06-29_2026-07-05_topline`; this run corrected its Democratic topline from 0.46 to the primary-source 0.45. The public tracker did not expose party-ID subgroup sample sizes, so it remains topline-only.
- No newly released post-2026-07-09 modeled Senate or governor general-election public poll with usable party-ID crosstabs was located.

### Unclassified Polls

- None.

### Extraction Uncertainties

- The Economist/YouGov crosstab row uses the PDF's `Voters` topline column for the aggregate result and the PDF's `Party ID` columns for subgroup shares. The subgroup Ns are the unweighted Democratic, Independent, and Republican party-ID counts printed in the same table.
- Rasmussen's public text contains an apparent arithmetic/typographical inconsistency in the undecided sentence, but the major-party generic ballot figures and total sample size are clear.
- No source-specific parser was added; rows were normalized manually after inspecting the public source pages/PDF.

## 2026-07-09 Generic Ballot Backfill

### Sources Searched

- 2026 United States elections public polling table, reviewed July 9, 2026: `https://en.wikipedia.org/wiki/2026_United_States_elections#Polling`.
- RealClearPolling latest polls and generic congressional vote surfaces, reviewed July 9, 2026, as cross-checks for recently posted generic-ballot rows.
- Targeted web searches for July 2026 generic congressional ballot releases and crosstabs from Quantus Insights, Morning Consult, Talker Research, Cygnal, Focaldata/Financial Times, The Economist/YouGov, Big Data Poll, ActiVote, Morning Consult/Cato Institute, and McLaughlin & Associates.

### Polls Applied

Applied 13 topline-only `us_house_generic` observations that were missing from `data/ingestion/2026_normalized_polls.json`. Candidate A is the generic Republican and candidate B is the generic Democrat in each row.

- `quantus_us_house_generic_2026-07-03_2026-07-07_topline`: Quantus Insights, July 3-7, 2026, n=1,140 LV, Republican 0.42, Democrat 0.47.
- `morning-consult_us_house_generic_2026-06-29_2026-07-05_topline`: Morning Consult, June 29-July 5, 2026, n=24,000 RV, Republican 0.42, Democrat 0.46.
- `talker_us_house_generic_2026-06-25_2026-07-02_topline`: Talker Research, June 25-July 2, 2026, n=2,000 RV, Republican 0.39, Democrat 0.48.
- `cygnal_us_house_generic_2026-06-30_2026-07-01_topline`: Cygnal, June 30-July 1, 2026, n=1,500 LV, Republican 0.44, Democrat 0.50.
- `focaldata-ft_us_house_generic_2026-06-26_2026-06-30_topline`: Focaldata/Financial Times, June 26-30, 2026, n=1,723 RV, Republican 0.44, Democrat 0.51.
- `economist-yougov_us_house_generic_2026-06-26_2026-06-29_topline`: The Economist/YouGov, June 26-29, 2026, n=1,426 RV, Republican 0.42, Democrat 0.45.
- `morning-consult_us_house_generic_2026-06-26_2026-06-28_topline`: Morning Consult, June 26-28, 2026, n=2,202 RV, Republican 0.42, Democrat 0.46.
- `big-data_us_house_generic_2026-06-26_2026-06-28_topline`: Big Data Poll, June 26-28, 2026, n=2,604 LV, Republican 0.41, Democrat 0.50.
- `morning-consult_us_house_generic_2026-06-22_2026-06-28_topline`: Morning Consult, June 22-28, 2026, n=24,000 RV, Republican 0.42, Democrat 0.46.
- `activote_us_house_generic_2026-06-06_2026-06-28_topline`: ActiVote, June 6-28, 2026, n=1,000 LV, Republican 0.47, Democrat 0.53.
- `morning-consult-cato_us_house_generic_2026-06-25_2026-06-26_topline`: Morning Consult/Cato Institute, June 25-26, 2026, n=1,797 RV, Republican 0.39, Democrat 0.45.
- `mclaughlin_us_house_generic_2026-06-17_2026-06-23_topline`: McLaughlin & Associates, June 17-23, 2026, n=1,000 LV, Republican 0.43, Democrat 0.46.
- `morning-consult_us_house_generic_2026-06-19_2026-06-22_topline`: Morning Consult, June 19-22, 2026, n=24,000 RV, Republican 0.42, Democrat 0.46.

### Polls Skipped As Duplicates

- Existing generic-ballot rows through June 22, 2026 remained in the normalized feed and were not duplicated.

### Polls Found Without Clear Party-ID Crosstabs

- All 13 applied generic-ballot rows were topline-only in the reviewed public table. No clear Republican, Democratic, and Independent party-ID crosstabs with subgroup sample sizes were found in the public sources reviewed during this sweep.

### Unclassified Polls

- None.

### Extraction Uncertainties

- The public polling table lists Democratic share before Republican share; normalized rows store Republican as candidate A and Democrat as candidate B to match the `us_house_generic` convention.
- When a pollster reported multiple universes for the same field period, this backfill used the voter-screened row preferred by the existing generic-ballot feed convention: likely voters when available, otherwise registered voters, and skipped adult-only alternatives.
- Several Morning Consult rows have overlapping field windows and large tracking samples. They were ingested because they are distinct public table rows, but the current model treats overlapping toplines as independent observations, so generic-ballot uncertainty may remain too narrow.

## 2026-07-09

### Sources Searched

- RealClearPolling latest polls page, reviewed July 9, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 9, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 9, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- Noble Predictive Insights July 7, 2026 Arizona governor Republican primary release and linked poll report, rechecked July 9, 2026: `https://www.noblepredictiveinsights.com/post/azgov-gop-primary-biggs-goes-big-before-primary-day`.
- Live web searches for newly released public modeled-race Senate polls and crosstabs since the 2026-07-08 run across Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for newly released public modeled-race governor polls and crosstabs since the 2026-07-08 run across Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Pollster/source-specific searches for July 2026 modeled-race releases and party-ID crosstabs from Emerson College Polling, Quinnipiac University, Marist, SurveyUSA, Fox News, New York Times/Siena College, AARP, Cygnal, Quantus Insights, Noble Predictive Insights, RealClearPolling, Race to the WH, 270toWin, Decision Desk HQ, and public polling table surfaces.

### Polls Applied

- None. No newly released post-2026-07-08 modeled Senate or governor general-election public poll with clear Republican, Democratic, and Independent party-ID crosstabs plus subgroup sample sizes was located.

### Polls Skipped As Duplicates

- RealClearPolling and web searches continued to surface already-reviewed or already-ingested modeled-race rows, including Fox Iowa/Georgia, NYT/Siena Senate and governor rows, Cygnal Iowa, AARP Ohio, Morning Scrapple Pennsylvania, SoCal/Red Eagle Texas, older Michigan/UNH/St. Anselm public polling table rows, and the Noble Arizona governor Republican primary release already logged on July 8.

### Polls Found Without Clear Party-ID Crosstabs

- None newly released after the 2026-07-08 run for the modeled Senate/governor general-election race list.
- RealClearPolling surfaced newly posted national/generic-ballot rows from Quantus Insights and Cygnal on July 8, plus national approval polling on July 9. These were reviewed but are outside today's modeled Senate/governor crosstab update, and no state-level modeled-race party-ID crosstabs were available from those rows.
- Noble Predictive Insights' Arizona governor Republican primary poll remained visible in public sources, but it was not applied because it is a Republican primary poll rather than an `az_gov` general-election observation.

### Unclassified Polls

- None.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new modeled-race general-election release was located.

## 2026-07-08

### Sources Searched

- RealClearPolling latest polls page, reviewed July 8, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling latest Senate polls page, reviewed July 8, 2026: `https://www.realclearpolling.com/latest-polls/senate`.
- RealClearPolling latest Governor polls page, reviewed July 8, 2026: `https://www.realclearpolling.com/latest-polls/governor`.
- Noble Predictive Insights July 7, 2026 Arizona governor Republican primary release and linked poll report: `https://www.noblepredictiveinsights.com/post/azgov-gop-primary-biggs-goes-big-before-primary-day`.
- Live web searches for newly released public modeled-race Senate polls and crosstabs since the 2026-07-07 run across Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for newly released public modeled-race governor polls and crosstabs since the 2026-07-07 run across Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Pollster/source-specific searches for July 2026 modeled-race releases and party-ID crosstabs from Emerson College Polling, Quinnipiac University, Marist, SurveyUSA, Fox News, New York Times/Siena College, AARP, Cygnal, Noble Predictive Insights, RealClearPolling, Race to the WH, 270toWin, Decision Desk HQ, and public polling table surfaces.

### Polls Applied

- None. No newly released post-2026-07-07 modeled Senate or governor general-election public poll with clear Republican, Democratic, and Independent party-ID crosstabs plus subgroup sample sizes was located.

### Polls Skipped As Duplicates

- RealClearPolling and web searches continued to surface already-reviewed or already-ingested modeled-race rows, including Fox Iowa/Georgia, NYT/Siena Senate and governor rows, Cygnal Iowa, AARP Ohio, Morning Scrapple Pennsylvania, SoCal/Red Eagle Texas, and older Michigan/UNH/St. Anselm public polling table rows.

### Polls Found Without Clear Party-ID Crosstabs

- None newly released after the 2026-07-07 run for the modeled Senate/governor general-election race list.
- Noble Predictive Insights released a July 7 Arizona governor Republican primary poll showing Biggs 60, Schweikert 10, Neely 2, and Miceli 1 among 425 likely GOP primary voters fielded June 29-July 1, 2026. It was reviewed but not applied because it is a Republican primary poll, not an `az_gov` general-election observation; no Republican/Democratic/Independent general-election party-ID crosstabs were extracted.
- RealClearPolling also surfaced newly posted national generic-ballot rows from Economist/YouGov and Rasmussen, but today's automation scope is the modeled Senate and governor race list, and no state-level modeled-race party-ID crosstabs were available from those rows.

### Unclassified Polls

- None.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new modeled-race general-election release was located.

## 2026-07-07

### Sources Searched

- RealClearPolling latest polls page and Senate/governor latest-polls surfaces, reviewed July 7, 2026: `https://www.realclearpolling.com/latest-polls`.
- Live web searches for newly released public modeled-race Senate polls and crosstabs since the 2026-07-06 run across Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for newly released public modeled-race governor polls and crosstabs since the 2026-07-06 run across Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Pollster/source-specific searches for July 2026 modeled-race releases and party-ID crosstabs from Emerson College Polling, Quinnipiac University, Marist, SurveyUSA, Fox News, New York Times/Siena College, AARP, Cygnal, RealClearPolling, Race to the WH, 270toWin, and public polling table surfaces.
- Direct terminal checks of RealClearPolling latest-polls URLs returned a JavaScript/captcha interstitial, so no extraction relied on terminal HTML from those pages.

### Polls Applied

- None. No newly released post-2026-07-06 modeled-race public poll with clear Republican, Democratic, and Independent party-ID crosstabs plus subgroup sample sizes was located.

### Polls Skipped As Duplicates

- Search results continued to surface already-reviewed or already-ingested modeled-race rows, including Fox Iowa/Georgia, NYT/Siena Senate crosstabs, Cygnal Iowa, AARP Ohio, Morning Scrapple Pennsylvania, SoCal/Red Eagle Texas, and older modeled-state public polling table rows.

### Polls Found Without Clear Party-ID Crosstabs

- None newly released after the 2026-07-06 run for the modeled Senate/governor race list.
- Search also surfaced national/generic-ballot polling references and older primary or hypothetical matchup rows; these were outside today's modeled Senate/governor crosstab update.

### Unclassified Polls

- None.

### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new release was located.
- `python3 scripts/rebuild_2026_model.py` applied 67 existing normalized observations, duplicates 0, and rewrote `data/models/2026_election_model.json`.
- `python3 scripts/export_public.py` refreshed `docs/data/forecasts.json` and `docs/data/race-history.json`; observed public forecast changes were generated timestamp/rounding churn only.

## 2026-07-06

### Sources Searched

- RealClearPolling latest polls page, reviewed July 6, 2026: `https://www.realclearpolling.com/latest-polls`.
- Fox News Iowa release, crosstab PDF, and topline PDF for the June 23-27, 2026 registered-voter survey covering `ia_sen` and `ia_gov`.
- Fox News Georgia release, crosstab PDF, and topline PDF for the June 23-27, 2026 registered-voter survey covering `ga_sen` and `ga_gov`.
- Live web searches for newly released public modeled-race Senate polls and crosstabs since the 2026-07-05 run across Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for newly released public modeled-race governor polls and crosstabs since the 2026-07-05 run across Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Pollster/source-specific searches for July 2026 modeled-race releases and crosstabs from Emerson College Polling, SurveyUSA, Fox News, RealClearPolling, and search-surfaced public polling tables.

### Polls Applied

Upgraded four existing Fox News rows from topline-only observations to party-ID crosstab observations. The existing poll IDs were retained for ledger continuity; `election_modeling.ingestion` prefers crosstabs when both crosstab and topline fields are present.

- `fox_ia_sen_2026-06-23_2026-06-27_topline` -> `ia_sen`: Fox News, June 23-27, 2026, n=1,003 RV, Hinson vs. Turek.
  - Republican self-ID, estimated n=384: Hinson 0.88, Turek 0.08.
  - Democratic self-ID, estimated n=474: Hinson 0.02, Turek 0.96.
  - Independent self-ID, estimated n=133: Hinson 0.28, Turek 0.59.
- `fox_ia_gov_2026-06-23_2026-06-27_topline` -> `ia_gov`: Fox News, June 23-27, 2026, n=1,003 RV, Lahn vs. Sand.
  - Republican self-ID, estimated n=384: Lahn 0.84, Sand 0.13.
  - Democratic self-ID, estimated n=474: Lahn 0.02, Sand 0.97.
  - Independent self-ID, estimated n=133: Lahn 0.27, Sand 0.60.
- `fox_ga_sen_2026-06-23_2026-06-27_topline` -> `ga_sen`: Fox News, June 23-27, 2026, n=1,002 RV, Collins vs. Ossoff.
  - Republican self-ID, estimated n=384: Collins 0.89, Ossoff 0.10.
  - Democratic self-ID, estimated n=474: Collins 0.03, Ossoff 0.96.
  - Independent self-ID, estimated n=133: Collins 0.28, Ossoff 0.68.
- `fox_ga_gov_2026-06-23_2026-06-27_topline` -> `ga_gov`: Fox News, June 23-27, 2026, n=1,002 RV, Jackson vs. Lance Bottoms.
  - Republican self-ID, estimated n=384: Jackson 0.93, Lance Bottoms 0.07.
  - Democratic self-ID, estimated n=474: Jackson 0.05, Lance Bottoms 0.95.
  - Independent self-ID, estimated n=133: Jackson 0.43, Lance Bottoms 0.52.

### Polls Skipped As Duplicates

- RealClearPolling continued to surface the same July 1-3 poll set reviewed on July 5, including already-ingested Fox, NYT/Siena, Cygnal, AARP Ohio, and Morning Scrapple/PennLive/Bravo Group rows.
- Search results re-surfaced already-ingested NYT/Siena Senate crosstabs for `ak_sen`, `ia_sen`, `nc_sen`, `oh_sen`, and `tx_sen`.

### Polls Found Without Clear Party-ID Crosstabs

- No newly released post-2026-07-05 modeled-race poll lacking party-ID crosstabs was found.
- The Fox Iowa and Georgia PDFs still do not print exact R/D/I subgroup sample sizes. They do print party-ID subgroup MOEs, so this run treated the R/D/I crosstab shares as usable with estimated sample sizes and logged that uncertainty explicitly.

### Unclassified Polls

- None.

### Extraction Uncertainties

- Fox's exact party-ID subgroup Ns are not printed in the crosstab PDFs. The normalized rows use estimated subgroup Ns from the standard 95% margin-of-error relationship `n ~= (0.98 / subgroup_moe)^2`, using Fox's published party-ID subgroup MOEs: Democratic 4.5 points -> n=474, Republican 5.0 points -> n=384, Independent 8.5 points -> n=133.
- The Fox crosstab rows are registered-voter observations, not likely-voter observations.
- Existing Fox poll IDs still end in `_topline` because the rows were upgraded in place to preserve duplicate-tracking continuity.

## 2026-07-05

### RealClearPolling Latest-Polls Scrape

#### Sources Searched

- RealClearPolling latest polls page, reviewed July 5, 2026: `https://www.realclearpolling.com/latest-polls`.
- RealClearPolling race pages linked from the latest-polls feed for Iowa Senate, Iowa governor, Georgia Senate, Georgia governor, New Hampshire Senate, New Hampshire governor, Michigan Senate, Texas governor, Maine Senate, Pennsylvania governor, Ohio Senate, and Ohio governor.
- Fox News Iowa release and linked crosstab/topline PDFs for the June 23-27, 2026 Iowa poll.
- Fox News Georgia release for the June 23-27, 2026 Georgia poll.
- Fox News Maine release for the June 23-27, 2026 Maine poll.
- Iowans for Tax Relief Foundation/Cygnal June 16-19, 2026 Iowa statewide topline PDF.
- Morning Scrapple/PennLive/Bravo Group Pennsylvania polling dashboard page for the June 18-25, 2026 Pennsylvania poll.
- AARP Ohio June 14-16, 2026 survey release.
- Existing NYT/Siena state crosstab pages already used for the July 1 Senate crosstab batch, cross-checked against RCP's latest-polls governor toplines.

#### Polls Applied

Applied 12 RCP-surfaced topline observations that were not already in `data/ingestion/2026_normalized_polls.json`:

- `fox_ia_sen_2026-06-23_2026-06-27_topline` -> `ia_sen`: Fox News, n=1,003 RV, Hinson 0.46, Turek 0.50.
- `fox_ia_gov_2026-06-23_2026-06-27_topline` -> `ia_gov`: Fox News, n=1,003 RV, Lahn 0.44, Sand 0.53.
- `fox_ga_sen_2026-06-23_2026-06-27_topline` -> `ga_sen`: Fox News, n=1,002 RV, Collins 0.43, Ossoff 0.56.
- `fox_ga_gov_2026-06-23_2026-06-27_topline` -> `ga_gov`: Fox News, n=1,002 RV, Jackson 0.47, Lance Bottoms 0.52.
- `fox_me_sen_2026-06-23_2026-06-27_topline` -> `me_sen`: Fox News, n=1,003 RV, Collins 0.50, Platner 0.47.
- `cygnal_ia_sen_2026-06-16_2026-06-19_topline` -> `ia_sen`: Cygnal/Iowans for Tax Relief Foundation, n=600 LV, Hinson 0.460, Turek 0.442.
- `morning-scrapple_pa_gov_2026-06-18_2026-06-25_topline` -> `pa_gov`: Morning Scrapple/PennLive/Bravo Group, n=644 LV, Garrity 0.29, Shapiro 0.54.
- `aarp_fabrizio-impact_oh_sen_2026-06-14_2026-06-16_topline` -> `oh_sen`: AARP/Fabrizio Ward/Impact Research, n=800 LV, Husted 0.45, Brown 0.48.
- `aarp_fabrizio-impact_oh_gov_2026-06-14_2026-06-16_topline` -> `oh_gov`: AARP/Fabrizio Ward/Impact Research, n=800 LV, Ramaswamy 0.44, Acton 0.47.
- `nyt-siena_ia_gov_2026-06-15_2026-06-27_topline` -> `ia_gov`: New York Times/Siena College, n=575 from the already-ingested Iowa NYT/Siena party-ID total, Lahn 0.47, Sand 0.48.
- `nyt-siena_oh_gov_2026-06-15_2026-06-28_topline` -> `oh_gov`: New York Times/Siena College, n=584 from the already-ingested Ohio NYT/Siena party-ID total, Ramaswamy 0.47, Acton 0.47.
- `nyt-siena_tx_gov_2026-06-19_2026-06-27_topline` -> `tx_gov`: New York Times/Siena College, n=618 from the already-ingested Texas NYT/Siena party-ID total, Abbott 0.51, Hinojosa 0.44.

#### Polls Skipped As Duplicates

- RCP re-surfaced already-ingested NYT/Siena Senate crosstabs for `ia_sen`, `oh_sen`, `ak_sen`, `nc_sen`, and `tx_sen`.
- RCP re-surfaced the already-ingested Cygnal/Iowans for Tax Relief Foundation Iowa governor topline.
- RCP re-surfaced existing Maine Senate toplines, including the June NYT/Siena/Portland Press Herald row already in the feed.

#### Polls Found Without Clear Party-ID Crosstabs

- All 12 rows applied in this RCP scrape were applied as toplines only. Fox's Iowa crosstab PDF includes Democratic, Republican, and Independent columns, but the reviewed static PDF text did not expose clear subgroup sample sizes for those party-ID groups.
- Fox Georgia, Fox Maine, AARP Ohio, Morning Scrapple Pennsylvania, Cygnal Iowa Senate, and the RCP-visible NYT/Siena governor rows did not provide clear public R/D/I party-ID crosstabs with subgroup sample sizes in the reviewed material.

#### Unclassified Or Not Applied

- New Hampshire Senate and governor rows from UNH and Saint Anselm were not applied because the modeled races do not yet have settled nominees and the RCP feed includes multiple Republican Senate matchups (`Sununu` vs. `Pappas` and `Brown` vs. `Pappas`) for the same `nh_sen` race.
- Michigan Senate Quantus rows were not applied because the Democratic primary is unresolved and the RCP feed includes multiple hypothetical Democratic general-election opponents (`El-Sayed`, `Stevens`, and `McMorrow`) against `Rogers` for the same `mi_sen` race.
- Maine governor, Massachusetts, New York, Louisiana, and other state rows on the latest-polls page were outside the current modeled race registry.
- RCP generic-ballot/latest national issue rows were not part of this modeled Senate/governor scrape.

#### Extraction Uncertainties

- For NYT/Siena governor toplines, RCP exposed the ballot result but not a separate static sample size. The normalized rows use the already-ingested NYT/Siena party-ID total for the same state poll as the topline sample size.
- The Morning Scrapple source page provides the June poll's field dates and sample size, while the Shapiro-vs-Garrity topline came from RCP's latest-polls row.
- The AARP Ohio source page provides field dates and sample size, while the all-voter Senate/governor toplines came from RCP's latest-polls row; the article text itself emphasized voters age 50+.
- `python3 scripts/rebuild_2026_model.py` applied 67 observations, duplicates 0, and updated `data/models/2026_election_model.json` plus `data/ingestion/2026_seen_polls.json`.
- `python3 scripts/export_public.py` refreshed `docs/data/forecasts.json` and `docs/data/race-history.json`.

### Daily Modeled-Race Sweep

#### Sources Searched

- Live web searches for newly released public polls since the 2026-07-04 run across modeled 2026 Senate races: Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, North Carolina, and already-modeled Maine context that surfaced in aggregator results.
- Live web searches for newly released public polls since the 2026-07-04 run across modeled 2026 governor races: Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Search-surfaced July 1 Guardian coverage of the New York Times/Siena battleground Senate package, checked against the existing ledger.
- Pollster/source-specific searches for July 2026 releases and party-ID crosstabs from New York Times/Siena College, Siena College Research Institute, Emerson College Polling, Quinnipiac University, Marist, SurveyUSA, Echelon Insights, Cygnal, Quantus Insights, RealClearPolling, Race to the WH, 270toWin, Decision Desk HQ, and FiveThirtyEight-style public poll data surfaces.
- Direct public feed checks attempted for FiveThirtyEight poll CSVs and RealClearPolling 2026 Senate/governor pages; the sandboxed `curl` calls returned empty bodies, so these were used only as attempted checks, not as extraction sources.

#### Polls Applied

- None. No newly released post-2026-07-04 modeled-race poll with clear public Republican/Democratic/Independent party-ID crosstabs and subgroup sample sizes was located.

#### Polls Skipped As Duplicates

- Search results re-surfaced the New York Times/Siena battleground Senate package published July 1, 2026. Its modeled-race crosstabs for `ak_sen`, `ia_sen`, `nc_sen`, `oh_sen`, and `tx_sen` were already present in `data/ingestion/2026_normalized_polls.json` and `data/ingestion/2026_seen_polls.json`.
- The previously applied SoCal Strategies/Red Eagle Politics Texas Senate and governor crosstab workbook remained in the normalized feed and ledger.

#### Polls Found Without Clear Party-ID Crosstabs

- None newly released after the 2026-07-04 run. The search sweep continued to surface older/topline-only or already-reviewed items, including Texas and generic-ballot materials logged on July 4.

#### Unclassified Polls

- None.

#### Extraction Uncertainties

- No new crosstab extraction was attempted because no qualifying new release was located.
- `python3 scripts/rebuild_2026_model.py` reapplied 55 existing normalized observations into a fresh snapshot and rewrote `data/ingestion/2026_seen_polls.json` without changing the seen-poll count.
- `python3 scripts/export_public.py` refreshed `docs/data/forecasts.json` and `docs/data/race-history.json`; the observed public-data diffs were generated timestamp updates only.

## 2026-07-04

### Maine Senate RCP Backfill

#### Sources Searched

- RealClearPolling 2026 Maine Senate page for Susan Collins vs. Graham Platner, reviewed July 4, 2026.
- Search-surfaced public polling table snippets for the same Collins-vs-Platner matchup, used to recover rows not visible in the static RCP text extraction.
- Public news reports for the June New York Times/Portland Press Herald/Siena College and June Fabrizio/Pine Tree Results toplines surfaced around the current RCP average.

#### Polls Applied

Applied 14 Maine U.S. Senate topline observations to `me_sen`, with Susan Collins as candidate A/Republican and Graham Platner as candidate B/Democrat:

- `nyt-siena-pph_me_sen_2026-06-19_2026-06-26_topline`: New York Times/Portland Press Herald/Siena College, n=608 LV, Collins 0.47, Platner 0.49.
- `fabrizio-pine-tree_me_sen_2026-06-01_2026-06-03_topline`: Fabrizio, Lee & Associates/Pine Tree Results, n=800 LV, Collins 0.46, Platner 0.46.
- `echelon_me_sen_2026-04-03_2026-04-09_topline`: Echelon Insights, n=378 LV, Collins 0.45, Platner 0.51.
- `maine-peoples-resource-center_me_sen_2026-03-20_2026-03-31_topline`: Maine People's Resource Center, n=1,167 LV, Collins 0.39, Platner 0.48.
- `emerson_me_sen_2026-03-21_2026-03-23_topline`: Emerson College, n=1,075 LV, Collins 0.41, Platner 0.48.
- `onmessage_me_sen_2026-03-03_2026-03-08_topline`: OnMessage Public Strategies, n=600 LV, Collins 0.42, Platner 0.44.
- `quantus_me_sen_2026-03-05_topline`: Quantus Insights, n=800 LV, Collins 0.42, Platner 0.49.
- `pan-atlantic_me_sen_2026-02-13_2026-03-02_topline`: Pan Atlantic Research, n=810 LV, Collins 0.40, Platner 0.44.
- `unh_me_sen_2026-02-12_2026-02-16_topline`: University of New Hampshire, n=1,105 LV, Collins 0.38, Platner 0.49.
- `fabrizio_me_sen_2026-01-20_2026-01-24_topline`: Fabrizio, Lee & Associates, n=800 LV, Collins 0.45, Platner 0.44.
- `workbench_me_sen_2025-12-11_2025-12-16_topline`: Workbench Strategy, n=900 LV, Collins 0.50, Platner 0.50.
- `pan-atlantic_me_sen_2025-11-29_2025-12-07_topline`: Pan Atlantic Research, n=820 LV, Collins 0.42, Platner 0.43.
- `maine-peoples-resource-center_me_sen_2025-10-26_2025-10-29_topline`: Maine People's Resource Center, n=783 LV, Collins 0.41, Platner 0.45.
- `zenith_me_sen_2025-10-07_2025-10-10_topline`: Zenith Research, n=501 LV, Collins 0.38, Platner 0.38.

#### Polls Skipped Or Not Applied

- RealClearPolling and other aggregate averages were not ingested as observations.
- Collins-vs-Janet Mills, Collins-vs-Dan Kleban, and Collins-vs-generic-Democrat rows were not applied to the Collins-vs-Platner model.
- No clear public Republican/Democratic/Independent party-ID crosstabs with subgroup sample sizes were found for these rows in this pass, so all applied Maine rows are toplines.

#### Extraction Uncertainties

- RCP's rendered page showed the current Collins-vs-Platner average, but its static extraction did not expose every individual table row. The row set was cross-checked against indexed public polling-table snippets and public reports.
- The June news reports were used for the current post-primary NYT/Siena and Fabrizio/Pine Tree toplines because they appear to explain the tightened RCP average on the linked page.

### Generic Ballot Sweep

#### Sources Searched

- Live web searches for 2026 generic congressional ballot polling and crosstabs.
- Wikipedia 2026 United States elections generic congressional ballot polling table, reviewed July 4, 2026, including individual public poll rows through June 22, 2026.
- Search-surfaced aggregator references for RealClearPolling, Race to the WH, Silver Bulletin, Decision Desk HQ, VoteHub, and FiftyPlusOne generic-ballot averages. These were used for orientation only; aggregate averages were not ingested as polls.

#### Generic Ballot Polls Applied

Applied 24 national generic congressional ballot topline observations to `us_house_generic`, using voter-screened samples from the public polling table and the requested electorate weighting of 35% Republican, 35% Democratic, and 30% Independent:

- `economist-yougov_us_house_generic_2026-06-19_2026-06-22_topline`: The Economist/YouGov, n=1,517 RV, Republican 0.43, Democratic 0.45.
- `reuters-ipsos_us_house_generic_2026-06-18_2026-06-22_topline`: Reuters/Ipsos, n=978 RV, Republican 0.36, Democratic 0.41.
- `echelon_us_house_generic_2026-06-18_2026-06-22_topline`: Echelon Insights, n=1,008 LV, Republican 0.45, Democratic 0.51.
- `quinnipiac_us_house_generic_2026-06-18_2026-06-22_topline`: Quinnipiac University, n=1,165 RV, Republican 0.42, Democratic 0.49.
- `strength-verasight_us_house_generic_2026-06-17_2026-06-22_topline`: Strength In Numbers/Verasight, n=1,896 RV, Republican 0.43, Democratic 0.50.
- `bullfinch_us_house_generic_2026-06-12_2026-06-16_topline`: The Bullfinch Group, n=1,000 RV, Republican 0.36, Democratic 0.44.
- `economist-yougov_us_house_generic_2026-06-13_2026-06-15_topline`: The Economist/YouGov, n=1,402 RV, Republican 0.44, Democratic 0.46.
- `echelon_us_house_generic_2026-06-11_2026-06-14_topline`: Echelon Insights, n=1,012 LV, Republican 0.44, Democratic 0.50.
- `emerson_us_house_generic_2026-06-07_2026-06-08_topline`: Emerson College, n=1,200 LV, Republican 0.40, Democratic 0.50.
- `economist-yougov_us_house_generic_2026-06-05_2026-06-08_topline`: The Economist/YouGov, n=1,393 RV, Republican 0.41, Democratic 0.45.
- `reuters-ipsos_us_house_generic_2026-06-03_2026-06-08_topline`: Reuters/Ipsos, n=3,578 RV, Republican 0.37, Democratic 0.41.
- `morning-consult_us_house_generic_2026-06-01_2026-06-07_topline`: Morning Consult, n=24,849 RV, Republican 0.42, Democratic 0.46.
- `hart-pos_us_house_generic_2026-05-29_2026-06-07_topline`: Hart Research Associates/Public Opinion Strategies, n=2,400 RV, Republican 0.44, Democratic 0.49.
- `harrisx-forbes_us_house_generic_2026-05-20_2026-06-07_topline`: HarrisX/Forbes, n=1,565 LV, Republican 0.45, Democratic 0.46.
- `clarity_us_house_generic_2026-05-28_2026-06-05_topline`: Clarity Campaign Labs, n=1,045 LV, Republican 0.45, Democratic 0.48.
- `noble-center-square_us_house_generic_2026-06-01_2026-06-04_topline`: Noble Predictive Insights/The Center Square, n=2,585 RV, Republican 0.41, Democratic 0.47.
- `rmg_us_house_generic_2026-06-01_2026-06-04_topline`: RMG Research, n=2,000 RV, Republican 0.45, Democratic 0.49.
- `cygnal_us_house_generic_2026-06-02_2026-06-03_topline`: Cygnal, n=1,500 LV, Republican 0.44, Democratic 0.49.
- `argument-verasight_us_house_generic_2026-05-29_2026-06-03_topline`: The Argument/Verasight, n=3,008 RV, Republican 0.47, Democratic 0.53.
- `quantus_us_house_generic_2026-06-01_2026-06-02_topline`: Quantus Insights, n=1,050 LV, Republican 0.42, Democratic 0.47.
- `bullfinch_us_house_generic_2026-05-29_2026-06-02_topline`: The Bullfinch Group, n=1,000 RV, Republican 0.36, Democratic 0.42.
- `focaldata-ft_us_house_generic_2026-05-29_2026-06-01_topline`: Focaldata/Financial Times, n=1,483 RV, Republican 0.45, Democratic 0.50.
- `economist-yougov_us_house_generic_2026-05-29_2026-06-01_topline`: The Economist/YouGov, n=1,452 RV, Republican 0.42, Democratic 0.46.
- `harvard-harris-harrisx_us_house_generic_2026-05-29_2026-05-31_topline`: Harvard/Harris Poll/HarrisX, n=1,725 RV, Republican 0.49, Democratic 0.51.

#### Generic Ballot Polls Skipped Or Not Applied

- All-adult-only rows were skipped where no voter-screened sample was available in the reviewed public table.
- Generic-ballot aggregate averages from Decision Desk HQ, FiftyPlusOne, RealClearPolling, Silver Bulletin, VoteHub, and Race to the WH were not ingested as poll observations.
- No clear public Republican/Democratic/Independent party-ID crosstabs with subgroup sample sizes were found in this sweep; all applied generic-ballot rows are aggregate toplines.

#### Generic Ballot Extraction Uncertainties

- The applied generic-ballot observations share a public aggregator table as the immediate source, even when the pollster has a separate release. Source-specific party-ID workbooks/PDFs should replace these toplines if located later.
- The model currently treats these toplines as independent aggregate observations. Because several polls overlap in field dates and house effects are not yet modeled for generic ballot, the current margin uncertainty is probably too narrow.

### Sources Searched

- Live web searches for polls released since the 2026-07-03 run across the modeled 2026 Senate races: Florida, Texas, Georgia, New Hampshire, Iowa, Alaska, Michigan, Ohio, and North Carolina.
- Live web searches for polls released since the 2026-07-03 run across the modeled 2026 governor races: Florida, Georgia, Texas, North Carolina, New Hampshire, Iowa, Pennsylvania, Arizona, Ohio, Michigan, and Wisconsin.
- Search-surfaced public aggregation pages for 2026 Senate and governor polling, including Race to the WH-style public pages and current public race polling summaries.
- Pollster/source-specific searches for July 2026 releases and crosstabs from Emerson College Polling, SurveyUSA, YouGov, Quinnipiac, Marist, Cygnal, Quantus Insights, Catawba College/YouGov, High Point University/YouGov, New York Times/Siena College, A2 Insights, Texas Politics Project, and SoCal Strategies.
- SoCal Strategies/Red Eagle Politics Texas poll release page and linked public Google Sheets crosstab workbook, fielded June 21, 2026.
- A2 Insights Texas statewide survey PDF, fielded June 23-28, 2026.
- University of Texas/Texas Politics Project June 2026 Texas topline PDF.

### Polls Applied

- `socal-red-eagle_tx_gov_2026-06-21_crosstab` -> `tx_gov`
  - Pollster: SoCal Strategies/Red Eagle Politics.
  - Field date: June 21, 2026.
  - Candidate A: Greg Abbott (Republican). Candidate B: Gina Hinojosa (Democrat).
  - Party-ID crosstabs from the linked workbook's Q5/Q6 Governor table with undecided leaners allocated:
    - Republican self-ID, weighted n=336: Abbott 0.930309688788526, Hinojosa 0.0515427141102821.
    - Democratic self-ID, weighted n=269: Abbott 0.0716499583213411, Hinojosa 0.893328632982937.
    - Independent self-ID, weighted n=195: Abbott 0.50869381988781, Hinojosa 0.411161461658662.
- `socal-red-eagle_tx_sen_2026-06-21_crosstab` -> `tx_sen`
  - Pollster: SoCal Strategies/Red Eagle Politics.
  - Field date: June 21, 2026.
  - Candidate A: Ken Paxton (Republican). Candidate B: James Talarico (Democrat).
  - Party-ID crosstabs from the linked workbook's Q7/Q8 U.S. Senate table with undecided leaners allocated:
    - Republican self-ID, weighted n=336: Paxton 0.90241878641925, Talarico 0.0618821250628544.
    - Democratic self-ID, weighted n=269: Paxton 0.0242967965131829, Talarico 0.963450406375171.
    - Independent self-ID, weighted n=195: Paxton 0.401813149321734, Talarico 0.495251201544853.

### Polls Skipped As Duplicates

- No duplicate poll IDs were skipped by the full rebuild. Already-ingested NYT/Siena and Catawba/YouGov records remained in the normalized feed and ledger.

### Polls Found Without Clear Party-ID Crosstabs

- A2 Insights Texas statewide survey, June 23-28, 2026, `tx_sen`: the PDF includes Republican, Democratic, and Independent party rows for Paxton vs. Talarico, but does not publish party-ID subgroup sample sizes or weighted subgroup shares. It was logged but not applied.
- University of Texas/Texas Politics Project June 2026 Texas survey, `tx_sen` and `tx_gov`: the reviewed public topline PDF did not include usable party-ID crosstabs.
- No newly released July 3-4 modeled-race poll with public party-ID crosstabs was found beyond the previously unlogged SoCal/Red Eagle Texas crosstab workbook.

### Unclassified Polls

- None.

### Extraction Uncertainties

- The SoCal/Red Eagle workbook reports `% of Sample (weighted)` rather than integer party-ID counts. The applied subgroup sample sizes use the 800 likely-voter sample multiplied by the weighted party shares in the workbook and rounded to whole respondents: Republican 336, Democratic 269, Independent 195.
- SoCal/Red Eagle candidate shares are the workbook's weighted crosstab proportions with undecided leaners allocated; any residual undecided/other response mass is left outside the two-candidate Kalman observation.
- The A2 Insights Texas PDF has party rows but no published subgroup sizes, so it was treated as insufficient for the current `PartyIDCrosstab` schema.

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
