from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from election_modeling.public import export_public_forecasts, export_public_race_history


if __name__ == "__main__":
    export_public_forecasts()
    export_public_race_history()
