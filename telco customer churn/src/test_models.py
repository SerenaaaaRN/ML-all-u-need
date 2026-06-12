import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("telco customer churn/models/LogisticReg.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")

# customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn
# 7590-VHVEG,Female,0,Yes,No,1,No,No phone service,DSL,No,Yes,No,No,No,No,Month-to-month,Yes,Electronic check,29.85,29.85,No
SAMPLE = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 1,
    "PhoneService": "No",
    "MultipleLines": "No phone service",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 29.85,
    "TotalCharges": "29.85",
}

def predict(raw: dict) -> dict:
    df = pd.DataFrame([raw])
    
    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0]

    return {
        "pred": int(pred),
        "confidence": float(max(proba)),
        "prob_churn": float(proba[1]),
        "prob_no_churn": float(proba[0]),
    }


if __name__ == "__main__":
    result = predict(SAMPLE)
    print(f"Level Confident Model: {result['confidence']:.1%}")
    print(f"\nDetail:")
    print(f"Probabilitas churn: {result['prob_churn']:.2%}")
    print(f"Probabilitas tidak churn: {result['prob_no_churn']:.2%}")
