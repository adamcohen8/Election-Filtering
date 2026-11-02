"""Rolling comparisons share the chronological, canonical, deduplicated feed."""
import json
from pathlib import Path

import pytest

from election_modeling import RACES_2026_BY_ID, public_race_history_payload


def poll(index, *, race_id="me_sen", date=None, **extra):
    return {
        "poll_id": f"poll-{index}", "pollster": "Example",
        "field_date": date or f"2026-10-{index:02}", "race_id": race_id,
        "topline_a": .30 + index / 100, "topline_b": .60 - index / 100,
        # Sample size intentionally varies: each poll must still count equally.
        "topline_n": 100 * index, **extra,
    }


def history(tmp_path, rows, race_id="me_sen"):
    path = tmp_path / "polls.json"
    path.write_text(json.dumps({"polls": rows}))
    return next(r for r in public_race_history_payload(feed_path=path)["races"]
                if r["race_id"] == race_id)


@pytest.mark.parametrize("count, expected_a", [(1, .31), (3, .32), (7, .34), (9, .36)])
def test_equal_weight_latest_seven_with_early_windows(tmp_path, count, expected_a):
    result = history(tmp_path, [poll(i) for i in reversed(range(1, count + 1))])
    average = result["rolling_average"]
    assert result["rolling_average_window"] == 7
    assert len(result["rolling_average_points"]) == count
    assert average["poll_count"] == min(count, 7)
    assert average["poll_ids"] == [f"poll-{i}" for i in range(max(1, count - 6), count + 1)]
    assert average["candidate_a_share"] == pytest.approx(expected_a)
    assert average["candidate_b_share"] == pytest.approx(.9 - expected_a)
    assert average["margin"] == pytest.approx(2 * expected_a - .9)
    assert average["margin_percent"] == pytest.approx(100 * (2 * expected_a - .9))


def test_window_counts_polls_even_on_the_same_day(tmp_path):
    result = history(tmp_path, [poll(i, date="2026-10-01") for i in range(1, 10)])
    assert len(result["poll_points"]) == 9
    assert len(result["rolling_average_points"]) == 1
    assert result["rolling_average"]["candidate_a_share"] == .36
    assert result["rolling_average"]["poll_count"] == 7


def test_average_uses_canonical_electorate_adjusted_polls_and_deduplicates(tmp_path):
    original = {
        "poll_id": "original", "pollster": "Example", "race_id": "me_sen",
        "field_date": "2026-10-01", "candidate_a": "Troy Jackson", "candidate_b": "Susan Collins",
        "republican_a": .1, "republican_b": .9, "republican_n": 100,
        "democratic_a": .8, "democratic_b": .2, "democratic_n": 100,
        "independent_a": .5, "independent_b": .4, "independent_n": 100,
    }
    rows = [original, dict(original), dict(original, poll_id="mirror"),
            poll(2, pollster="Wedgewood Polls"), poll(3, race_id="fl_sen")]
    result = history(tmp_path, rows)
    average = result["rolling_average"]
    assert average["poll_count"] == 1
    assert average["candidate_a_share"] == round(.31*.9 + .28*.2 + .41*.4, 4)
    assert average["candidate_b_share"] == round(.31*.1 + .28*.8 + .41*.5, 4)


@pytest.mark.parametrize("race_id", ["me_sen", "pa_gov", "us_house_generic"])
def test_average_is_available_for_every_office(tmp_path, race_id):
    result = history(tmp_path, [poll(1, race_id=race_id)], race_id)
    assert result["rolling_average"]["poll_count"] == 1


def test_prior_only_races_have_no_average(tmp_path):
    result = history(tmp_path, [])
    assert result["rolling_average"] is None
    assert result["rolling_average_points"] == []


def test_saved_history_contains_current_rolling_averages_for_all_races():
    root = Path(__file__).resolve().parents[1]
    saved = json.loads((root / "docs/data/race-history.json").read_text())
    replayed = public_race_history_payload(feed_path=root / "data/ingestion/2026_normalized_polls.json")
    assert saved["races"] == replayed["races"]
    assert {race["race_id"] for race in saved["races"]} == set(RACES_2026_BY_ID)
    for race in saved["races"]:
        if not race["poll_points"]:
            assert race["rolling_average"] is None
            continue
        window = race["poll_points"][-7:]
        average = race["rolling_average"]
        assert average["poll_count"] == len(window)
        assert average["poll_ids"] == [point["poll_id"] for point in window]
        for key in ("candidate_a_share", "candidate_b_share"):
            assert average[key] == pytest.approx(sum(point[key] for point in window) / len(window), abs=.000051)
