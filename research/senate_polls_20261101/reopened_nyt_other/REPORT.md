# New York Times / Siena source-access review

Archive sanitation (2026-11-01): the Google Maps API key embedded in `sources/siena-oct03.html` and `sources/siena-oct28.html` was replaced with `REDACTED_GOOGLE_API_KEY`. The poll text and links are retained. Original and sanitized SHA-256 hashes are recorded in `../source-redactions.json`.

No complete party-by-candidate tables were recovered for Texas or Ohio (October 3) or Florida or Minnesota (October 28). `polls.json` contains no rows, so none is proposed for ingestion. All four requested state-specific crosstab links on Siena’s official releases point to NYT interactive HTML, not Siena-hosted PDFs. The web reader returned non-retryable errors for each; a previously encountered browser site-safety gate was respected. No screenshots, rendered page images, authentication workarounds or bypasses were used.

Siena’s official original release HTML files are preserved under `sources/` and provide release dates, candidate names, state-level toplines and links to the relevant tables, but no party-conditional six-cell vote tables. Independent web searches for Siena-hosted files and candidate/party breakdowns did not establish equivalent complete source tables. A separately published October 13 ReconMR/Siena Texas poll is a different survey and should not be substituted for the October 3 Times/Siena wave.

The four direct table URLs and their access status appear in inventory.json. Any future ingestion requires a permitted readable version of each original table and verification of party definitions, candidate ballot question, field dates and subgroup counts where available.
