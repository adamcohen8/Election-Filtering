"""Review gates for new, source-backed Senate polling inputs."""
import copy
import importlib.util
from pathlib import Path

import pytest
import numpy as np

from election_modeling.ingestion import NormalizedPoll, canonical_poll
from election_modeling.public import public_race_history_payload

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("senate_research", ROOT / "scripts/ingest_senate_research.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def row():
    return {
        "poll_id": "example", "race_id": "mn_sen", "state": "Minnesota", "office": "senate",
        "pollster": "Example", "field_start": "2026-09-27", "field_date": "2026-09-30",
        "publication_date": "2026-10-01", "crosstab_basis": "party_id",
        "candidate_a": "Michele Tafoya", "candidate_b": "Peggy Flanagan",
        "candidate_a_party": "republican", "candidate_b_party": "democratic",
        "source_url": "https://example.org/poll.pdf", "source_location": "p. 1",
        "evidence_excerpt": "Party ID, candidate support and bases.",
        "subgroup_n_method": "reported_weighted", "reported_total_n": 600,
        "republican_a": .85, "republican_b": .1, "republican_n": 200.9,
        "democratic_a": .1, "democratic_b": .85, "democratic_n": 200.1,
        "independent_a": .4, "independent_b": .45, "independent_n": 199.0,
    }


def normalized(raw=None, review=None):
    return module.normalize_reviewed_row(raw or row(), review or {"reason": "verified primary table"},
        source_path="research/example/polls.json", start="2026-10-01", end="2026-11-01")


def test_october_first_release_can_have_september_fieldwork_and_preserves_source_bases():
    raw = row()
    result = normalized(raw)
    assert raw == row()
    assert result["field_date"] == "2026-09-30"
    assert result["publication_date"] == "2026-10-01"
    assert result["republican_n"] == 200
    assert result["source_subgroup_bases"]["republican"] == 200.9
    assert result["model_base_method"] == "reported_weighted"
    assert result["design_effect"] == 2.0


@pytest.mark.parametrize("publication", ["2026-09-30", "2026-11-02", None])
def test_unverified_or_outside_publication_is_rejected(publication):
    raw = row()
    raw["publication_date"] = publication
    with pytest.raises(ValueError, match="publication date"):
        normalized(raw)


def test_older_poll_requires_both_race_policy_and_record_authorization():
    raw = row()
    raw["publication_date"] = "2026-09-30"
    kwargs = dict(source_path="research/example/polls.json", start="2026-10-01", end="2026-11-01")
    with pytest.raises(ValueError, match="outside requested window"):
        module.normalize_reviewed_row(raw, {"reason": "reviewed", "backfill_authorized": True}, **kwargs)
    with pytest.raises(ValueError, match="outside requested window"):
        module.normalize_reviewed_row(raw, {"reason": "reviewed"}, backfill_allowed=True, **kwargs)
    result = module.normalize_reviewed_row(raw, {"reason": "reviewed", "backfill_authorized": True},
        backfill_allowed=True, **kwargs)
    assert result["backfill_original_cutoff"] == "2026-10-01"


def test_backfill_preserves_baseline_and_stops_at_target():
    baseline = {"poll_id": "old", "race_id": "mn_sen", "research_record_sha256": "original"}
    added = {"poll_id": "new", "race_id": "mn_sen", "backfill_original_cutoff": "2026-10-01"}
    policy = {"baseline_source_hashes": {"old": "original"}, "baseline_counts": {"mn_sen": 1},
              "target_races": {"mn_sen": 1}, "target_count": 2}
    module.validate_backfill_selection([baseline, added], policy)
    with pytest.raises(ValueError, match="preserve every baseline"):
        module.validate_backfill_selection([added], policy)
    with pytest.raises(ValueError, match="changed a baseline"):
        module.validate_backfill_selection([{**baseline, "research_record_sha256": "changed"}, added], policy)
    with pytest.raises(ValueError, match="exceeds"):
        module.validate_backfill_selection([baseline, added, {**added, "poll_id": "third"}], policy)
    with pytest.raises(ValueError, match="not an authorized"):
        module.validate_backfill_selection([baseline, {**added, "race_id": "tx_sen"}], policy)


def test_authorized_backfill_accepts_bounded_older_publication_but_not_future():
    raw = row()
    raw["publication_date"] = None
    review = {"reason": "reviewed", "backfill_authorized": True,
              "publication_date_bounds": ["2026-09-30", "2026-09-30"]}
    kwargs = dict(source_path="research/example/polls.json", start="2026-10-01", end="2026-11-01")
    result = module.normalize_reviewed_row(raw, review, backfill_allowed=True, **kwargs)
    assert result["backfill_original_cutoff"] == "2026-10-01"
    with pytest.raises(ValueError, match="publication date"):
        module.normalize_reviewed_row(raw, review, **kwargs)
    raw["publication_date"] = "2026-11-02"
    with pytest.raises(ValueError, match="outside requested window"):
        module.normalize_reviewed_row(raw, review, backfill_allowed=True, **kwargs)


@pytest.mark.parametrize("basis", ["modeled_party_id", "ideology", None])
def test_proxies_are_not_silently_substituted_for_party_id(basis):
    raw = row()
    raw["crosstab_basis"] = basis
    with pytest.raises(ValueError, match="actual party-ID"):
        normalized(raw)


def test_missing_counts_need_a_published_bound_and_never_become_reported_counts():
    raw = row()
    raw["subgroup_n_method"] = "missing"
    for p in module.PARTIES:
        raw[f"{p}_n"] = None
    with pytest.raises(ValueError, match="denominator"):
        normalized(raw)
    result = normalized(raw, {"reason": "published suppression rule", "precision": {
        "method": "suppression_lower_bound", "minimum_n": 100,
        "evidence": "Publisher suppresses all subgroups with n < 100.",
    }})
    assert result["republican_n"] == 100
    assert result["source_subgroup_bases"]["republican"] is None
    assert result["model_base_method"] == "suppression_lower_bound"
    assert result["design_effect"] == 3.0


def test_censored_support_is_not_converted_to_zero():
    raw = row()
    raw["democratic_a"] = None
    raw["democratic_a_interval"] = [0, .01]
    with pytest.raises(ValueError, match="censored"):
        normalized(raw)


def test_contradictory_candidates_fail_replay_before_snapshot_writes():
    raw = row()
    raw["candidate_a"] = "Wrong Candidate"
    with pytest.raises(ValueError):
        module.replay([normalized(raw)])


def test_duplicate_survey_measurement_fails_replay():
    first = normalized()
    second = copy.deepcopy(first)
    second["poll_id"] = "mirror"
    with pytest.raises(ValueError, match="duplicate measurements"):
        module.replay([first, second])


def fixed_precision():
    return {"method": "assumed_covariance", "cell_sd": .05,
            "within_group_correlation": -.5,
            "evidence": "User authorized missing-count sources; explicitly assumed 5pp cell SD."}


def test_authorized_proxy_stays_labeled_and_does_not_invent_counts():
    raw = row()
    raw["crosstab_basis"] = "modeled_party_id"
    raw["subgroup_n_method"] = "missing"
    for party in module.PARTIES:
        raw[party + "_n"] = None
    review = {"reason": "user authorized proxy", "allow_proxy": True, "precision": fixed_precision()}
    result = normalized(raw, review)
    assert result["crosstab_basis"] == "modeled_party_id"
    assert result["proxy_inclusion_authorized"] is True
    assert all(result[p + "_n"] is None for p in module.PARTIES)
    poll = NormalizedPoll.from_mapping(result)
    assert poll.crosstab.subgroup_sample_sizes == {}
    observation = poll.crosstab.to_observation(design_effect=99)
    np.testing.assert_allclose(observation.covariance, result["crosstab_covariance"])
    election, _ = module.replay([result])
    assert election.races["mn_sen"].observation_count == 1


def test_censored_cell_explicit_midpoint_preserves_interval_and_adds_uncertainty():
    raw = row()
    raw["democratic_a"] = None
    raw["democratic_a_censored"] = {"lower_exclusive": 0, "upper_exclusive": .01}
    result = normalized(raw, {"reason": "explicit interval approximation", "precision": fixed_precision(),
        "interval_midpoints": {"democratic_a": {"lower": 0, "upper": .01}}})
    assert result["democratic_a"] == .005
    assert result["source_support_values"]["democratic_a"] is None
    assert result["support_approximations"]["democratic_a"]["source_interval"] == [0, .01]
    assert result["crosstab_covariance"][2][2] == pytest.approx(.05**2 + .005**2)
    bad_review = {"reason": "wrong interval", "precision": fixed_precision(),
        "interval_midpoints": {"democratic_a": {"lower": 0, "upper": .02}}}
    with pytest.raises(ValueError, match="published interval"):
        normalized(raw, bad_review)


def test_direct_covariance_reorders_when_candidate_labels_reverse():
    raw = row()
    for p in module.PARTIES:
        raw[p + "_n"] = 200
    matrix = np.diag([.001, .002, .003, .004, .005, .006])
    raw["crosstab_covariance"] = matrix.tolist()
    raw["candidate_a"], raw["candidate_b"] = raw["candidate_b"], raw["candidate_a"]
    raw["candidate_a_party"], raw["candidate_b_party"] = "democratic", "republican"
    parsed = NormalizedPoll.from_mapping(raw)
    canonical = canonical_poll(parsed, "mn_sen")
    np.testing.assert_allclose(np.diag(canonical.crosstab.measurement_covariance), [.002, .001, .004, .003, .006, .005])
    assert canonical.crosstab.values["independent"] == (.45, .4)


def test_missing_count_history_uses_null_instead_of_zero(tmp_path):
    raw = row()
    raw["subgroup_n_method"] = "missing"
    for p in module.PARTIES:
        raw[p + "_n"] = None
    result = normalized(raw, {"reason": "missing counts", "precision": fixed_precision()})
    path = tmp_path / "polls.json"
    module.write_json(path, {"polls": [result]})
    history = public_race_history_payload(feed_path=path)
    mn = next(r for r in history["races"] if r["race_id"] == "mn_sen")
    assert len(mn["poll_points"]) == 1
    assert mn["poll_points"][0]["sample_size"] is None


def test_direct_covariance_rejects_materially_invalid_error_matrix():
    raw = row()
    for p in module.PARTIES:
        raw[p + "_n"] = 200
    raw["crosstab_covariance"] = (-np.eye(6)).tolist()
    with pytest.raises(ValueError, match="positive semidefinite"):
        NormalizedPoll.from_mapping(raw)
