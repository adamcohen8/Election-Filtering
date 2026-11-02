# InsiderAdvantage Senate survey recovery

Seven in-window race-waves have complete Republican, Democratic and independent candidate-support columns: Ohio (released October 1), Kansas (October 11 and 15), Maine and Texas (October 15), Michigan (October 23), and Florida (October 30). The original images are preserved in `sources/`, and each record in `polls.json` identifies its release and separate table post or image. The remaining six identified in-window waves lack a recovered full party table and remain in the inventory, not the model dataset.

All recovered tables label their subgroup simply “Party”; the source does not establish whether it is self-identification, voter-file registration, or a model. Column counts are displayed but not labeled weighted or unweighted. The release says surveys are weighted for political affiliation. These distinctions remain unknown; all records are marked `needs_review`. The party group numbers are not fabricated subgroup counts. The ballot question is combined vote or leaning except Florida, which asks for whom respondents would vote. This is a distinction between ballot questions, not a party-leaner classification.

| State / field end | Republican candidate support / Democrat candidate support in R, D, I groups | Displayed group bases R / D / I |
|---|---|---|
| Ohio Sep 29 | 86.6 / 6.8; 0.5 / 96.2; 24.2 / 42.3 | 480 / 336 / 384 |
| Kansas Oct 10 | 82.5 / 12.7; 3.1 / 92.2; 29.1 / 62.4 | 540 / 300 / 360 |
| Kansas Oct 14 | 84.0 / 11.5; 1.0 / 95.4; 31.9 / 58.4 | 540 / 300 / 360 |
| Maine Oct 14 | 92.5 / 5.1; 4.9 / 92.4; 47.0 / 46.4 | 384 / 420 / 396 |
| Texas Oct 14 | 86.5 / 10.7; 4.9 / 94.1; 44.3 / 48.5 | 473 / 378 / 349 |
| Michigan Oct 22 | 96.8 / 1.8; 4.5 / 91.2; 37.3 / 47.3 | 408 / 420 / 372 |
| Florida Oct 29 | 87.3 / 7.5; 8.6 / 85.8; 39.1 / 44.0 | 468 / 372 / 360 |

The Ohio September-field survey was released October 1, and is eligible by publication date; the image was separately published on the pollster's [October 1 tab post](https://insideradvantage.com/ohio-top-line-tabs/). Kansas October 9–10 image was posted [October 11](https://x.com/InsiderPolling/status/2109439147522007169); October 13–14 images for [Kansas](https://x.com/InsiderPolling/status/2111096445063528539), [Maine](https://x.com/InsiderPolling/status/2111096704267399329), and [Texas](https://x.com/InsiderPolling/status/2111096358233129297) were separately posted October 16. Michigan October 21–22 was posted [October 25](https://x.com/InsiderPolling/status/2114368835449233863). The Florida original image was located in a [public mirror of the pollster’s X feed](https://www.sotwe.com/InsiderPolling?lang=en) and published after the October 30 release; exact post URL/date not independently resolved. X itself returned 403, but public mirror metadata identified the pollster’s image URLs, and original pbs.twimg.com images were downloaded and inspected. The known Kansas, Maine, and Texas individual posts each exposed one image; this does not establish that other separate posts do not exist.

The pollster’s website and X releases were searched for Alaska and Michigan October 9–10; Iowa and Ohio October 21–22; and Minnesota and Ohio October 29–30. The pollster explicitly says the earlier Alaska and Michigan tabs are on X and says the later tabs would appear there. Those individual images were not recovered, not proven absent. Alaska’s available 50–48 result is ranked choice, so do not substitute it for a first-choice crosstab. Minnesota and Ohio final releases dated November 1 are included as unresolved inventory entries. The pollster's WordPress public posts and media archive for October 1–November 1 were searched; links to source release pages are in `inventory.json`.

A Minnesota September 28–29 wave was first published September 30 and its table merely reposted October 3. It is excluded under the explicit publication cutoff even though the repost displays complete cells. No raw topline-only observation is included in `polls.json`.
