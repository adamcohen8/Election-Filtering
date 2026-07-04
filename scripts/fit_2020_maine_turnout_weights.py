from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from election_modeling.states import PARTY_IDS


CROSSTAB_PATH = ROOT / "data" / "calibration" / "2020_me_sen_party_id_crosstabs.json"
KALMAN_PATH = ROOT / "data" / "calibration" / "2020_me_sen_kalman.json"
OUTPUT_PATH = ROOT / "data" / "calibration" / "2020_me_sen_turnout_weight_fit.json"


def _party_margins(record: dict[str, Any]) -> np.ndarray:
    crosstab = record["party_id_crosstab"]
    return np.asarray(
        [
            float(crosstab[party_id]["candidate_a"])
            - float(crosstab[party_id]["candidate_b"])
            for party_id in PARTY_IDS
        ],
        dtype=float,
    )


def _target_margin(record: dict[str, Any]) -> float:
    topline = record["topline"]
    return float(topline["candidate_a"]) - float(topline["candidate_b"])


def _party_sample_weights(record: dict[str, Any]) -> np.ndarray:
    crosstab = record["party_id_crosstab"]
    sample_sizes = np.asarray(
        [float(crosstab[party_id]["sample_size"]) for party_id in PARTY_IDS],
        dtype=float,
    )
    return sample_sizes / float(np.sum(sample_sizes))


def _final_state_margins(kalman: dict[str, Any]) -> np.ndarray:
    final = kalman["final_state"]
    return np.asarray(
        [
            final["republican_candidate_a"]["mean"]
            - final["republican_candidate_b"]["mean"],
            final["democratic_candidate_a"]["mean"]
            - final["democratic_candidate_b"]["mean"],
            final["independent_candidate_a"]["mean"]
            - final["independent_candidate_b"]["mean"],
        ],
        dtype=float,
    )


def _weights_grid(step: float) -> np.ndarray:
    if step <= 0 or step > 1:
        raise ValueError("step must be greater than 0 and at most 1.")
    scale = round(1.0 / step)
    if not np.isclose(scale * step, 1.0):
        raise ValueError("step must divide 1.0 evenly.")

    weights: list[tuple[float, float, float]] = []
    for republican_units in range(scale + 1):
        for democratic_units in range(scale - republican_units + 1):
            independent_units = scale - republican_units - democratic_units
            weights.append(
                (
                    republican_units / scale,
                    democratic_units / scale,
                    independent_units / scale,
                )
            )
    return np.asarray(weights, dtype=float)


def _score_grid(
    *,
    weights: np.ndarray,
    poll_party_margins: np.ndarray,
    poll_target_margins: np.ndarray,
    final_party_margins: np.ndarray,
    actual_margin: float,
    final_weight: float,
    poll_weight: float,
    poll_ids: list[str],
) -> dict[str, Any]:
    poll_margins = weights @ poll_party_margins.T
    poll_errors = poll_margins - poll_target_margins
    poll_mse = np.mean(poll_errors * poll_errors, axis=1)

    final_margins = weights @ final_party_margins
    final_errors = final_margins - actual_margin
    objective = final_weight * final_errors * final_errors + poll_weight * poll_mse

    # Use the secondary key to avoid arbitrary final-only or poll-only ties.
    secondary = poll_mse if final_weight > 0 else final_errors * final_errors
    best_index = int(np.lexsort((secondary, objective))[0])
    selected_weights = weights[best_index]
    selected_poll_margins = poll_margins[best_index]
    selected_poll_errors = poll_errors[best_index]

    return {
        "objective": float(objective[best_index]),
        "final_weight": final_weight,
        "poll_weight": poll_weight,
        "weights": {
            "republican": float(selected_weights[0]),
            "democratic": float(selected_weights[1]),
            "independent": float(selected_weights[2]),
        },
        "final_margin": float(final_margins[best_index]),
        "actual_margin": float(actual_margin),
        "final_margin_error": float(final_errors[best_index]),
        "poll_margin_rmse": float(np.sqrt(poll_mse[best_index])),
        "poll_margin_mean": float(np.mean(selected_poll_margins)),
        "target_poll_margin_mean": float(np.mean(poll_target_margins)),
        "poll_margin_mean_error": float(
            np.mean(selected_poll_margins) - np.mean(poll_target_margins)
        ),
        "poll_margin_std": float(np.std(selected_poll_margins)),
        "target_poll_margin_std": float(np.std(poll_target_margins)),
        "poll_margin_std_error": float(
            np.std(selected_poll_margins) - np.std(poll_target_margins)
        ),
        "polls": [
            {
                "poll_id": poll_id,
                "modeled_margin": float(modeled),
                "target_margin": float(target),
                "error": float(error),
            }
            for poll_id, modeled, target, error in zip(
                poll_ids,
                selected_poll_margins,
                poll_target_margins,
                selected_poll_errors,
            )
        ],
    }


def fit_turnout_weights(step: float = 0.001) -> dict[str, Any]:
    crosstabs = json.loads(CROSSTAB_PATH.read_text())
    kalman = json.loads(KALMAN_PATH.read_text())

    observations = sorted(crosstabs["observations"], key=lambda row: row["field_end"])
    poll_ids = [record["poll_id"] for record in observations]
    poll_party_margins = np.asarray([_party_margins(record) for record in observations])
    poll_target_margins = np.asarray([_target_margin(record) for record in observations])
    poll_sample_weights = np.asarray([_party_sample_weights(record) for record in observations])
    final_party_margins = _final_state_margins(kalman)
    actual = crosstabs["actual_result"]
    actual_margin = float(actual["candidate_a_share"]) - float(actual["candidate_b_share"])
    weights = _weights_grid(step)

    frontier_weights = (0.0, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0, 100.0)
    frontier = [
        _score_grid(
            weights=weights,
            poll_party_margins=poll_party_margins,
            poll_target_margins=poll_target_margins,
            final_party_margins=final_party_margins,
            actual_margin=actual_margin,
            final_weight=final_weight,
            poll_weight=1.0,
            poll_ids=poll_ids,
        )
        for final_weight in frontier_weights
    ]

    result = {
        "metadata": {
            "race_id": crosstabs["metadata"]["race_id"],
            "candidate_a": crosstabs["metadata"]["candidate_a"],
            "candidate_b": crosstabs["metadata"]["candidate_b"],
            "method": "simplex grid search over R/D/I weights",
            "step": step,
            "objective": (
                "final_weight * squared final margin error "
                "+ poll_weight * mean squared poll margin error"
            ),
            "note": "Margins are candidate_a minus candidate_b, so positive margins favor Collins.",
        },
        "actual_margin": actual_margin,
        "final_party_margins": {
            "republican": float(final_party_margins[0]),
            "democratic": float(final_party_margins[1]),
            "independent": float(final_party_margins[2]),
        },
        "target_poll_margin_distribution": {
            "mean": float(np.mean(poll_target_margins)),
            "standard_deviation": float(np.std(poll_target_margins)),
            "minimum": float(np.min(poll_target_margins)),
            "maximum": float(np.max(poll_target_margins)),
        },
        "average_poll_sample_composition": {
            "republican": float(np.mean(poll_sample_weights[:, 0])),
            "democratic": float(np.mean(poll_sample_weights[:, 1])),
            "independent": float(np.mean(poll_sample_weights[:, 2])),
        },
        "equal_weight_fit": next(
            row for row in frontier if row["final_weight"] == 1.0
        ),
        "poll_only_fit": frontier[0],
        "strong_final_fit": next(row for row in frontier if row["final_weight"] == 10.0),
        "frontier": frontier,
    }
    OUTPUT_PATH.write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> None:
    result = fit_turnout_weights()
    fit = result["equal_weight_fit"]
    weights = fit["weights"]
    print(f"wrote={OUTPUT_PATH}")
    print(
        "equal-weight objective weights: "
        f"R={weights['republican']:.3f} "
        f"D={weights['democratic']:.3f} "
        f"I={weights['independent']:.3f}"
    )
    print(
        "equal-weight objective errors: "
        f"final={fit['final_margin_error']:+.3f} "
        f"poll_rmse={fit['poll_margin_rmse']:.3f}"
    )


if __name__ == "__main__":
    main()
