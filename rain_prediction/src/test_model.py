import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("rain_prediction/models/RandomForest.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")

SAMPLE = {
    "Location": "Sydney",
    "MinTemp": 18.5,
    "MaxTemp": 26.3,
    "Rainfall": 2.4,
    "WindGustDir": "NW",
    "WindGustSpeed": 44,
    "WindDir9am": "N",
    "WindDir3pm": "NW",
    "WindSpeed9am": 15,
    "WindSpeed3pm": 22,
    "Humidity9am": 78,
    "Humidity3pm": 100,
    "Pressure9am": 1019.2,
    "Pressure3pm": 1016.8,
    "Temp9am": 21.0,
    "Temp3pm": 25.1,
    "RainToday": "No",
}


def predict(raw: dict) -> dict:
    df = pd.DataFrame([raw])

    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]

    return {
        "prediction": int(pred),
        "label": "Hujan" if pred == 1 else "Tidak Hujan",
        "confidence": float(max(proba)),
        "prob_no_rain": float(proba[0]),
        "prob_rain": float(proba[1]),
    }


if __name__ == "__main__":
    result = predict(SAMPLE)
    print(f"{result['label']} ({result['confidence']:.1%})")
    print(f"\nDetail:")
    print(f"  Probabilitas Tidak Hujan: {result['prob_no_rain']:.2%}")
    print(f"  Probabilitas Hujan: {result['prob_rain']:.2%}")
