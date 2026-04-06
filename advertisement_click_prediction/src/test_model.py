import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("advertisement_click_prediction/models/best_model.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")

SAMPLE = {
    "Gender": "Female",
    "Age": 32,
    "EstimatedSalary": 150000,
}

def predict(raw: dict) -> dict:
    df = pd.DataFrame([raw])
    
    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]

    return {
        "pred": int(pred),
        "confidence": float(max(proba)),
        "prob_no_click": float(proba[0]),
        "prob_click": float(proba[1]),
    }


if __name__ == "__main__":
    result = predict(SAMPLE)
    print(f"Level Confident Model: {result['confidence']:.1%}")
    print(f"\nDetail:")
    print(f"Probabilitas tidak click iklan: {result['prob_no_click']:.2%}")
    print(f"Probabilitas click iklan: {result['prob_click']:.2%}")