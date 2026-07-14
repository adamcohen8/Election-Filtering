import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FEED = ROOT / "data" / "ingestion" / "2026_normalized_polls.json"


def test_2026_normalized_poll_feed_is_crosstab_only() -> None:
    rows = json.loads(FEED.read_text())["polls"]
    required = {
        "republican_a",
        "republican_b",
        "republican_n",
        "democratic_a",
        "democratic_b",
        "democratic_n",
        "independent_a",
        "independent_b",
        "independent_n",
    }

    topline_only = [
        row["poll_id"]
        for row in rows
        if required - row.keys()
    ]
    topline_named = [
        row["poll_id"]
        for row in rows
        if row["poll_id"].endswith("_topline")
    ]

    assert topline_only == []
    assert topline_named == []
