import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("diabetes_prediction/models/NaiveBayes.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")

# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
#6,148,72,35,0,33.6,0.627,50,1
SAMPLE = {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}

def predict(raw: dict) -> dict:
    df = pd.DataFrame([raw])
    
    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]

    return {
        "pred": int(pred),
        "confidence": float(max(proba)),
        "prob_no_diabetes": float(proba[0]),
        "prob_diabetes": float(proba[1]),
    }


if __name__ == "__main__":
    result = predict(SAMPLE)
    print(f"Level Confident Model: {result['confidence']:.1%}")
    print(f"\nDetail:")
    print(f"Probabilitas diabetes: {result['prob_diabetes']:.2%}")
    print(f"Probabilitas tidak diabetes: {result['prob_no_diabetes']:.2%}")