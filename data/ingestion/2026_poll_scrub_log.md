# 2026 Poll Crosstab Scrub Log

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
