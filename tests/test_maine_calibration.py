import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "calibration" / "2020_me_sen_party_id_crosstabs.json"
TURNOUT_FIT = ROOT / "data" / "calibration" / "2020_me_sen_turnout_weight_fit.json"


def test_maine_calibration_dataset_has_complete_party_crosstabs() -> None:
    payload = json.loads(DATASET.read_text())

    assert payload["metadata"]["candidate_a"] == "Susan Collins"
    assert payload["metadata"]["candidate_b"] == "Sara Gideon"
    assert len(payload["observations"]) >= 6

    for poll in payload["observations"]:
        assert set(poll["party_id_crosstab"]) == {
            "republican",
            "democratic",
            "independent",
        }
        assert 0 <= poll["topline"]["candidate_a"] <= 1
        assert 0 <= poll["topline"]["candidate_b"] <= 1
        assert poll["topline"]["candidate_a"] + poll["topline"]["candidate_b"] <= 1
        for cell in poll["party_id_crosstab"].values():
            assert 0 <= cell["candidate_a"] <= 1
            assert 0 <= cell["candidate_b"] <= 1
            assert cell["candidate_a"] + cell["candidate_b"] <= 1
            assert cell["sample_size"] > 0


def test_maine_turnout_fit_has_valid_balanced_weights() -> None:
    payload = json.loads(TURNOUT_FIT.read_text())
    weights = payload["equal_weight_fit"]["weights"]

    assert set(weights) == {"republican", "democratic", "independent"}
    assert abs(sum(weights.values()) - 1.0) < 1e-9
    assert all(0 <= value <= 1 for value in weights.values())
    assert payload["equal_weight_fit"]["poll_margin_rmse"] >= 0
