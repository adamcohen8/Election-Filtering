"""State-vector definitions for party-ID support models."""

from __future__ import annotations

from typing import Literal

PartyID = Literal["republican", "democratic", "independent"]

PARTY_IDS: tuple[PartyID, ...] = ("republican", "democratic", "independent")

STATE_NAMES: tuple[str, ...] = (
    "republican_candidate_a",
    "republican_candidate_b",
    "democratic_candidate_a",
    "democratic_candidate_b",
    "independent_candidate_a",
    "independent_candidate_b",
)

STATE_INDEX: dict[str, int] = {name: index for index, name in enumerate(STATE_NAMES)}

PARTY_STATE_SLICES: dict[PartyID, tuple[int, int]] = {
    "republican": (0, 1),
    "democratic": (2, 3),
    "independent": (4, 5),
}
