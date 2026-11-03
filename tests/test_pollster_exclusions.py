"""User exclusions apply to every office and cannot leak into public history."""
import json
from pathlib import Path

import pytest

from election_modeling.cycles import create_2026_election_model
from election_modeling.ingestion import (
    NormalizedPoll, PollIngestionPipeline, StaticPollSource, apply_poll,
    user_pollster_exclusion_reason,
)
from election_modeling.public import public_race_history_payload

ROOT = Path(__file__).resolve().parents[1]


def poll_row(race="us_house_generic", name="AtlasIntel", identifier="excluded"):
    row = dict(poll_id=identifier, pollster=name, field_date="2026-11-01", race_id=race)
    for party in ("republican", "democratic", "independent"):
        row.update({party + "_a": .6, party + "_b": .35, party + "_n": 200})
    return row


@pytest.mark.parametrize("name", ["AtlasIntel", "Atlas Intel", "ATLAS INTEL",
                                "AtlasIntel/PollsterGraph", "Bloomberg / AtlasIntel"])
def test_atlas_aliases_and_joint_labels_are_excluded(name):
    assert "user request" in user_pollster_exclusion_reason(name)


@pytest.mark.parametrize("name", ["Emerson College Polling", "Rasmussen Reports", "Atlas Intelligence"])
def test_unrelated_pollsters_remain_allowed(name):
    assert user_pollster_exclusion_reason(name) is None


@pytest.mark.parametrize("race", ["tx_sen", "tx_gov", "us_house_generic"])
def test_pipeline_and_direct_application_reject_excluded_pollster_without_updates(race):
    election = create_2026_election_model()
    poll = NormalizedPoll.from_mapping(poll_row(race))
    pipeline = PollIngestionPipeline(sources=(StaticPollSource([poll]),))
    result = pipeline.run(election)
    assert not result.applied and len(result.errors) == 1
    assert "excluded from all models by user request" in result.errors[0]
    assert not pipeline.ledger.seen_poll_ids and not pipeline.ledger.measurement_keys
    assert election.races[race].observation_count == 0
    with pytest.raises(ValueError, match="excluded from all models"):
        apply_poll(poll, election.races[race])
    assert election.races[race].observation_count == 0


def test_history_ignores_atlas_even_in_a_contaminated_feed(tmp_path):
    kept = poll_row(name="Allowed Polling", identifier="kept")
    path = tmp_path / "polls.json"
    path.write_text(json.dumps({"polls": [poll_row(), kept]}))
    history = public_race_history_payload(feed_path=path)
    generic = next(r for r in history["races"] if r["race_id"] == "us_house_generic")
    assert [p["poll_id"] for p in generic["poll_points"]] == ["kept"]
    assert generic["rolling_average"]["poll_ids"] == ["kept"]


def test_current_feed_contains_no_user_excluded_pollsters():
    rows = json.loads((ROOT / "data/ingestion/2026_normalized_polls.json").read_text())["polls"]
    assert not [r["poll_id"] for r in rows if user_pollster_exclusion_reason(r["pollster"])]
