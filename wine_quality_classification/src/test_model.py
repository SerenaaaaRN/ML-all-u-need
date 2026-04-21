import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("wine_quality_classification/models/RandomForest.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")

sample_data = {
    "fixed_acidity": [11.2],
    "volatile_acidity": [0.28],
    "citric_acid": [0.56],
    "residual_sugar": [1.9],
    "chlorides": [0.075],
    "free_sulfur_dioxide": [17.0],
    "total_sulfur_dioxide": [60.0],
    "density": [0.9980],
    "pH": [3.16],
    "sulphates": [0.58],
    "alcohol": [9.8],
}


def predict(raw: dict) -> dict:
    df = pd.DataFrame([raw])

    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]
    proba_map = {f"quality_{c}": p for c, p in zip(pipeline.classes_, proba)}

    return {
        "pred": int(pred),
        "confidence": float(max(proba)),
        "probabilities": proba_map,
    }


if __name__ == "__main__":
    result = predict(sample_data)
    print(f"\nPrediksi Kualitas Wine: {result['pred']} ({result['confidence']:.1%})")
    print("Probabilitas per kelas:")
    for k, v in sorted(result['probabilities'].items()):
        print(f"  {k}: {v:.2%}")
