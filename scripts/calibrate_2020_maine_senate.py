from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from election_modeling.polls import PollObservation
from election_modeling.races import Electorate, RaceModel
from election_modeling.states import PARTY_IDS, STATE_NAMES


INPUT_PATH = ROOT / "data" / "calibration" / "2020_me_sen_party_id_crosstabs.json"
OUTPUT_PATH = ROOT / "data" / "calibration" / "2020_me_sen_kalman.json"


def _observation(record: dict[str, Any]) -> PollObservation:
    crosstab = record["party_id_crosstab"]
    values = {
        party_id: (
            float(crosstab[party_id]["candidate_a"]),
            float(crosstab[party_id]["candidate_b"]),
        )
        for party_id in PARTY_IDS
    }
    sample_sizes = {
        party_id: int(crosstab[party_id]["sample_size"])
        for party_id in PARTY_IDS
    }
    return PollObservation.from_party_id_shares(
        values=values,
        subgroup_sample_sizes=sample_sizes,
        pollster=record["pollster"],
        field_date=record["field_end"],
    )


def _state_payload(model: RaceModel) -> dict[str, dict[str, float]]:
    state = model.filter.state
    return {
        name: {
            "mean": float(state.mean[index]),
            "standard_error": float(state.covariance[index, index] ** 0.5),
        }
        for index, name in enumerate(STATE_NAMES)
    }


def run_calibration() -> dict[str, Any]:
    payload = json.loads(INPUT_PATH.read_text())
    observations = sorted(payload["observations"], key=lambda row: row["field_end"])
    model = RaceModel.default(
        electorate=Electorate(
            republican=1.0 / 3.0,
            democratic=1.0 / 3.0,
            independent=1.0 / 3.0,
        )
    )

    history = []
    for record in observations:
        model.update(_observation(record))
        history.append(
            {
                "poll_id": record["poll_id"],
                "pollster": record["pollster"],
                "field_end": record["field_end"],
                "measurement": record["measurement"],
                "state": _state_payload(model),
            }
        )

    result = {
        "metadata": payload["metadata"],
        "actual_result": payload["actual_result"],
        "filter_settings": {
            "initial_mean": [0.86, 0.10, 0.08, 0.88, 0.46, 0.46],
            "initial_variance": 0.04,
            "process_variance": 0.00005,
            "electorate": {
                "republican": 1.0 / 3.0,
                "democratic": 1.0 / 3.0,
                "independent": 1.0 / 3.0,
            },
            "note": "Electorate is neutral because this run estimates party-ID support states, not a final topline.",
        },
        "polls_applied": [
            {
                "poll_id": record["poll_id"],
                "pollster": record["pollster"],
                "field_start": record["field_start"],
                "field_end": record["field_end"],
                "measurement": record["measurement"],
                "source_url": record["source_url"],
            }
            for record in observations
        ],
        "final_state": _state_payload(model),
        "history": history,
        "searched_not_applied": payload["searched_not_applied"],
    }
    OUTPUT_PATH.write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> None:
    result = run_calibration()
    final = result["final_state"]
    print(f"wrote={OUTPUT_PATH}")
    for party in PARTY_IDS:
        a_key = f"{party}_candidate_a"
        b_key = f"{party}_candidate_b"
        print(
            f"{party}: "
            f"Collins={final[a_key]['mean']:.3f} "
            f"Gideon={final[b_key]['mean']:.3f}"
        )


if __name__ == "__main__":
    main()
