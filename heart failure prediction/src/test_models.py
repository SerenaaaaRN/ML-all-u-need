import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("heart failure prediction/models/KNN.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")
    exit()

# Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope,HeartDisease
# 40,M,ATA,140,289,0,Normal,172,N,0,Up,0
SAMPLE = {
    "Age": 49,
    "Sex": "F",
    "ChestPainType": "NAP",
    "RestingBP": 160,
    "Cholesterol": 180,
    "FastingBS": 0,
    "RestingECG": "Normal",
    "MaxHR": 156,
    "ExerciseAngina": "N",
    "Oldpeak": 1,
    "ST_Slope": "Flat"
}

def predict(raw: dict) -> dict:
    df = pd.DataFrame([raw])
    
    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]

    return {
        "pred": int(pred),
        "confidence": float(max(proba)),
        "prob_yes": float(proba[1]),
        "prob_no": float(proba[0]),
    }


if __name__ == "__main__":
    result = predict(SAMPLE)
    print(f"Level Confident Model: {result['confidence']:.1%}")
    print(f"\nDetail:")
    print(f"Probabilitas Yes: {result['prob_yes']:.2%}")
    print(f"Probabilitas No: {result['prob_no']:.2%}")
