from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {0: "No Diabetes", 1: "Diabetes"}

class DiabetesRequest(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@router.post("/predict/diabetes", response_model=PredictResponse)
def predict_diabetes(body: DiabetesRequest):
    model = MODELS.get("diabetes")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    X = pd.DataFrame([body.model_dump()])
    prediction = int(model.predict(X)[0])

    confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)[0]
        confidence = round(float(max(proba)) * 100, 1)

    return PredictResponse(
        value=prediction,
        label=LABEL_MAP.get(prediction, str(prediction)),
        confidence=confidence,
        feature_importance=None,
    )
