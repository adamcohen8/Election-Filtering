# Minnesota Senate backfill

Four distinct pre-October survey waves have complete candidate support among Republican, Democratic, and independent groups. Combined with the six previously identified October-release waves, this provides ten observations subject to their existing review and denominator qualifications. The oldest, August SurveyUSA, is a fallback: Quantus's September 11 survey is newer and its party table was not recovered, so the four are the latest **verified accessible** waves, not conclusively the latest published qualifying waves.

| First release | Survey / field end | Tafoya / Flanagan, Republicans | Democrats | Independents | Party subgroup n R/D/I |
|---|---|---|---|---|---|
| Sep 30 | InsiderAdvantage, Sep 29 | 93.8 / 1.4 | 4.5 / 89.5 | 41.3 / 38.6 | 383 / 445 / 371, weighting status unknown |
| Sep 15 | SurveyUSA, Sep 14 | 88 / 5 | 4 / 87 | 43 / 29 | unavailable |
| Sep 8 | TIPP, Sep 2 | 88.49 / 3.34 | 5.45 / 83.77 | 36.66 / 36.79 | 440 / 473 / 256, explicitly unweighted |
| Aug 18 | SurveyUSA, Aug 17 | 87 / 5 | 4 / 87 | 39 / 38 | unavailable |

All values are percentages and retain other and undecided voters outside the two major candidates; no two-party renormalization. TIPP workbook stores full-precision ratios and the table displays rounded values; extra digits do not imply measurement precision. TIPP likely-voter table E5LV supplies unweighted subgroup counts, while vote percentages are weighted; party classification wording is unspecified. InsiderAdvantage labels groups “Party” without specifying how classified and displays party bases without identifying their weighting. The party cells for both SurveyUSA reports are labeled Party Affiliation; exact question and leaner treatment not established. SurveyUSA provides only rounded composition percentages, not actual subgroup counts. Insider's ballot includes those leaning; other included ballots are initial full ballots. Every row is one survey, not a second population or question from the same survey.

September SurveyUSA report #28000 itself dates release September 15, while KSTP's related article dates September 16. Insider's Minnesota image was posted October 3 but matches its [September 30 release](https://insideradvantage.com/insideradvantage-survey-u-s-senate-minnesota-contest-a-one-point-race-flanagan-46-tafoya-45/), and is included because the authorized backfill uses original publication date.

Newer unresolved waves: [co/efficient's September 14–15 survey](https://battlegrounds.coefficient.org/mn/) currently provides toplines and overall party composition but no party-by-candidate cells; [Quantus's September 11 release](https://quantusinsights.org/f/new-quantus-polls-moody-leads-in-florida-flanagan-in-minnesota) advertises a technical report and crosstabs in search results but its current page returned the homepage, and all six cells could not be verified. A full Quantus table would supersede the August fallback. Deep Root's August campaign survey also lacks recovered complete crosstabs. Wedgewood is excluded as a disclosed fabricated pollster. No NYT source was accessed or fabricated. No statewide Rasmussen wave earlier than its October 9 release was established in the checked Minnesota race lists; sources and limitations are recorded in inventory.json. Poll lists are not proof that no other release exists.

Original pollster evidence is preserved in `sources/`; SurveyUSA text extracts are convenience copies. Exact source locations, raw Excel precision, dates, and denominator caveats are in `polls.json`. No shared decisions, importer, or model files were modified.


## Root source recovery

The September11 Quantus original was recovered from the pollster HTML embedded public link and visually checked. It replaces August18 SurveyUSA in selected polls.json, leaving four most recent verified accessible waves: InsiderSep30, SurveyUSASep15, QuantusSep11, TIPPSep8. The older fallback is archived separately and is not ingested. Quantus uses leaned partyID with other pooled intoI, weighted table bases R276/D314/I130 and workingDEFF3. Earlier unrecovered-status notes in this report/inventory are superseded by this recovery.
