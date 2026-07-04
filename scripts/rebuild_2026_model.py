from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from election_modeling.cycles import create_2026_election_model
from election_modeling.ingestion import (
    IngestionLedger,
    PollIngestionPipeline,
    StructuredJSONSource,
)
from election_modeling.persistence import save_election_model
from election_modeling.public import export_public_forecasts, export_public_race_history


def main() -> None:
    feed_path = ROOT / "data" / "ingestion" / "2026_normalized_polls.json"
    ledger_path = ROOT / "data" / "ingestion" / "2026_seen_polls.json"
    snapshot_path = ROOT / "data" / "models" / "2026_election_model.json"
    public_path = ROOT / "docs" / "data" / "forecasts.json"

    election = create_2026_election_model()
    pipeline = PollIngestionPipeline(
        sources=(StructuredJSONSource(str(feed_path)),),
        ledger=IngestionLedger(path=ledger_path),
    )
    result = pipeline.run(election)
    if result.errors or result.unclassified_poll_ids or result.unknown_race_ids:
        raise SystemExit(
            "ingestion failed: "
            f"errors={result.errors}, "
            f"unclassified={result.unclassified_poll_ids}, "
            f"unknown_races={result.unknown_race_ids}"
        )

    save_election_model(election, snapshot_path)
    export_public_forecasts(snapshot_path=snapshot_path, output_path=public_path)
    export_public_race_history(feed_path=feed_path)
    print(f"applied={len(result.applied)} duplicates={len(result.duplicate_poll_ids)}")


if __name__ == "__main__":
    main()
