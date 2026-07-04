import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "calibration" / "2020_me_sen_party_id_crosstabs.json"


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
        for cell in poll["party_id_crosstab"].values():
            assert 0 <= cell["candidate_a"] <= 1
            assert 0 <= cell["candidate_b"] <= 1
            assert cell["candidate_a"] + cell["candidate_b"] <= 1
            assert cell["sample_size"] > 0
