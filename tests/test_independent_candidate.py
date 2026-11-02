"""Independent opponents keep their own affiliation throughout the pipeline."""
import numpy as np
import pytest
from dataclasses import replace

from election_modeling import NormalizedPoll, create_2026_election_model
from election_modeling.ingestion import canonical_poll, apply_poll
from election_modeling.public import public_forecast_payload


def test_independent_candidate_orientation_and_public_affiliation():
    source = {
        "poll_id": "ne-orientation", "pollster": "Example", "field_date": "2026-10-30",
        "race_id": "ne_sen", "state": "Nebraska", "office": "senate",
        "candidate_a": "Dan Osborn", "candidate_a_party": "independent",
        "candidate_b": "Pete Ricketts", "candidate_b_party": "republican",
        "republican_a": .40, "republican_b": .55, "republican_n": 200,
        "democratic_a": .90, "democratic_b": .05, "democratic_n": 200,
        "independent_a": .70, "independent_b": .25, "independent_n": 200,
        "crosstab_covariance": np.diag([.001, .002, .003, .004, .005, .006]).tolist(),
    }
    poll = canonical_poll(NormalizedPoll.from_mapping(source), "ne_sen")
    assert poll.candidate_a == "Pete Ricketts" and poll.candidate_b == "Dan Osborn"
    assert poll.candidate_b_party == "independent"
    assert poll.crosstab.values["independent"] == (.25, .70)
    np.testing.assert_allclose(np.diag(poll.crosstab.measurement_covariance), [.002, .001, .004, .003, .006, .005])
    election = create_2026_election_model()
    apply_poll(poll, election.races["ne_sen"])
    result = next(r for r in public_forecast_payload(election)["races"] if r["race_id"] == "ne_sen")
    assert result["candidate_b_party"] == "Independent"
    assert result["candidate_b_name"] == "Dan Osborn"
    assert result["leader"] == "independent"
    assert "independent" in result["status"]
    assert "democratic" not in result["nominee_sources"]
    with pytest.raises(ValueError, match="explicit candidate A/B"):
        canonical_poll(replace(poll, party_named_crosstabs=True), "ne_sen")
    source["candidate_a_party"] = "democratic"
    with pytest.raises(ValueError, match="disagree"):
        canonical_poll(NormalizedPoll.from_mapping(source), "ne_sen")


def test_nebraska_user_selected_electorate():
    electorate = create_2026_election_model().races["ne_sen"].electorate
    assert (electorate.republican, electorate.democratic, electorate.independent) == (.57, .24, .19)
    assert electorate.share_standard_deviation == .01
