# Senate poll research assignment

User explicitly requests one GPT-6.1 Terra high subagent per modeled Senate race to find all available polls published since October 1, 2026 inclusive, with R/I/D candidate-support crosstabs, and add qualifying polls to the Senate models. The user confirmed the cutoff is PUBLICATION DATE, even if fieldwork ended in September. Current client date is November 1, 2026, America/Denver. Do not include later releases or substitute another year.

You own only `research/senate_polls_20261101/<race_id>/`. Work from `/Users/adamcohen/Documents/ChatGPT/Election Filtering`. Do not modify source code, other races, central data/models, or git metadata. Do not spawn more agents. Root will verify and ingest all records centrally. Preserve existing dirty work. Do not read or retrieve the excluded GitHub data directories. New research evidence and poll data are expressly authorized by this request.

## Research requirements

- Search widely across current polling aggregators and original pollster releases to enumerate the race's releases between 2026-10-01 and 2026-11-01 inclusive. Follow through to primary reports/crosstab PDFs where available. Aggregator toplines alone do not establish crosstabs.
- Candidate-support percentages CONDITIONAL ON Republican, Democratic, and Independent voter groups are required. Party ID is preferred; party registration is allowed only as a fallback when that poll has no usable party-ID table. Do not use ideology as party ID. Distinguish leaned-party ID from unleaned party ID. In registration tables, explain exactly how unaffiliated/other/no-party-preference is mapped to Independent; do not silently drop categories.
- Record ALL discovered releases in a candidate inventory, with a reason for any exclusion (no crosstabs, missing group, wrong date, inaccessible table, different candidate matchup, source unreliability, duplicate wave, etc.). Never fabricate values, quotes, sample sizes, dates, or source claims. Explicitly exclude Wedgewood, a disclosed fabricated pollster already blocked by this repository.
- Capture BOTH publication date and field start/end dates. Primary field-end date is the model's observation date. When a date is unverified, retain that uncertainty and do not pretend eligibility is established.
- Extract R and D candidate support within each R/D/I group, in fractions 0..1, with other/undecided residual allowed. Prefer all-candidate general-election first-choice ballot tests. Record question/round; do not mix first-choice and ranked-choice final-round or alternate hypothetical questions from one survey as independent observations. Prefer LV over RV for overlapping populations from the same survey and keep only one version of a wave.
- Capture subgroup bases: exact unweighted n preferred; exact reported weighted n must be labeled. If only total N and party-composition percentages are provided, retain those source values and a clearly labeled derived estimate (`floor(N * fraction)`) separately; do not call it a reported n. If no defensible denominator is available, preserve the crosstabs but mark the record `needs_denominator` for root review. Never assign arbitrary subgroup n.
- Preserve precise source URLs and PDF page/table/question references, short relevant excerpts or extracted table text, and any downloaded original file under your race folder. Do not bypass paywalls or access controls. Use web browsing and the PDF skill when local PDF inspection is needed. If a source cannot be read, report that limitation and continue other sources.
- Keep source text and provenance sufficient for root to independently check every accepted row. Do not describe search snippets as a full PDF read.

## Deliverables

Create `inventory.json`, `polls.json`, and `REPORT.md` in your race directory. You may add `sources/` and extracted text files.

`inventory.json`: list each discovered release with pollster, sponsor, publication_date, field_start, field_end, original_url, table_url, status, reason, and any alternate dates/duplicate relationships. Include search_queries and aggregator_urls in a top-level object so search coverage is auditable.

`polls.json`: top-level `{"race_id":"...","polls":[...]}`. Each row must preserve (null if not established):

```
{
  "poll_id": "stable-readable-wave-id",
  "race_id": "xx_sen",
  "state": "Full state name",
  "office": "senate",
  "pollster": "Original pollster",
  "sponsor": "Sponsor or null",
  "publication_date": "2026-10-DD",
  "field_start": "2026-...",
  "field_date": "field END YYYY-MM-DD",
  "population": "LV or RV or adults",
  "candidate_a": "Republican candidate name",
  "candidate_b": "Democratic candidate name",
  "candidate_a_party": "republican",
  "candidate_b_party": "democratic",
  "crosstab_basis": "party_id or party_registration",
  "party_question": "Exact wording or concise sourced description",
  "ballot_question_stage": "general-election first choice, etc.",
  "republican_a": 0.0,
  "republican_b": 0.0,
  "democratic_a": 0.0,
  "democratic_b": 0.0,
  "independent_a": 0.0,
  "independent_b": 0.0,
  "republican_n": 0,
  "democratic_n": 0,
  "independent_n": 0,
  "subgroup_n_method": "reported_unweighted/reported_weighted/derived_total_x_share/missing",
  "reported_total_n": 0,
  "reported_party_composition": {"republican":0.0,"democratic":0.0,"independent":0.0},
  "sample_id": "shared-wave-id; same survey always same ID",
  "source_url": "Primary crosstab URL",
  "release_url": "Primary release URL",
  "source_location": "PDF page and question/table label",
  "evidence_path": "path relative to repo root, or null",
  "evidence_excerpt": "Short table transcription with column/row labels",
  "ingestion_status": "ready/needs_denominator/needs_review",
  "notes": "Anything affecting comparability or reliability"
}
```

The zeros above are examples of schema, NOT data to copy. Use null for missing values. If a source has both ID and registration, use ID once and record why registration was not separately counted. Root's parser tolerates extra metadata. Shares within a group must sum to <= 1; preserve genuine rounding discrepancies for root review instead of silently renormalizing.

REPORT.md should state search coverage, count and identity of qualifying releases, excluded/inaccessible sources, denominator issues, and source-backed candidate-name conflicts if any. Completion means a thorough supported search, not an assertion that the open internet can be exhaustively proven complete. Send root early material findings and finish with concrete file paths and counts.
