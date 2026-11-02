"""Office boundaries and paired-race handling for reviewed governor data."""
import importlib.util
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ingest_senate_research import normalize_reviewed_row, replay


def governor():
    return {"poll_id": "paired-survey", "race_id": "fl_gov", "state": "Florida", "office": "governor",
            "pollster": "Example Polling", "publication_date": "2026-10-02", "field_date": "2026-10-01",
            "candidate_a": "Byron Donalds", "candidate_b": "David Jolly", "candidate_a_party": "republican",
            "candidate_b_party": "democratic", "crosstab_basis": "party_id", "subgroup_n_method": "reported_unweighted",
            "republican_a": .9, "republican_b": .05, "democratic_a": .03, "democratic_b": .9,
            "independent_a": .4, "independent_b": .45, "republican_n": 200, "democratic_n": 200,
            "independent_n": 200, "source_url": "https://example.org/table", "source_location": "Governor question",
            "evidence_excerpt": "All three party groups verified.", "sample_id": "one-sample"}


def test_governor_needs_explicit_office_and_cannot_enter_senate_research():
    kwargs = dict(source_path="research/example/polls.json", start="2026-10-01", end="2026-11-01")
    with pytest.raises(ValueError, match="Senate"):
        normalize_reviewed_row(governor(), {"reason": "verified"}, **kwargs)
    result = normalize_reviewed_row(governor(), {"reason": "verified"}, expected_office="governor", **kwargs)
    assert result["poll_id"] == "fl_gov--paired-survey"


def test_separate_senate_and_governor_questions_from_one_survey_are_distinct():
    kwargs = dict(source_path="research/example/polls.json", start="2026-10-01", end="2026-11-01")
    raw = governor()
    gov = normalize_reviewed_row(raw, {"reason": "verified"}, expected_office="governor", **kwargs)
    senate_raw = {**raw, "race_id": "fl_sen", "office": "senate", "candidate_a": "Ashley Moody", "candidate_b": "Angie Nixon"}
    sen = normalize_reviewed_row(senate_raw, {"reason": "verified"}, **kwargs)
    election, ledger = replay([gov, sen])
    assert election.races["fl_gov"].observation_count == 1
    assert election.races["fl_sen"].observation_count == 1
    assert len(ledger.seen_poll_ids) == 2
