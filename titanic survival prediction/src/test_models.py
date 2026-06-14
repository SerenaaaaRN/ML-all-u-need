import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("titanic survival prediction/models/RandomForest.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")
    exit()

SAMPLE_RAW = {
    "Pclass": 2,
    "Name": "Serena, Mr. RIllah",
    "Sex": "male",
    "Age": 22,
    "SibSp": 0,
    "Parch": 0,
    "Fare": 13,
    "Embarked": "S",
}

def predict(raw_data: dict) -> dict:
    df = pd.DataFrame([raw_data])
    
    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]
    
    return {
        "pred": int(pred),
        "confidence": float(max(proba)),
        "prob_survived": float(proba[1]),
    }

if __name__ == "__main__":
    result = predict(SAMPLE_RAW)
    status = "SURVIVED 🟢" if result['pred'] == 1 else "DIED 🔴"
    print(f"Prediction: {status}")
    print(f"Confidence: {result['confidence']:.1%}")