import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "models"

PROJECTS = [
    "ad-click", "diabetes", "ai-student", "rain",
    "telco-churn", "titanic", "video-games", "wine-quality",
    "med-cost", "heart-fail",
]


def load_all_models() -> dict:
    loaded = {}
    for pid in PROJECTS:
        path = BASE / f"{pid}.joblib"
        if not path.exists():
            print(f"Model not found: {path}")
            continue
        try:
            loaded[pid] = joblib.load(path)
            print(f"Loaded: {pid}")
        except Exception as e:
            print(f"Error loading {pid}: {e}")

    return loaded
