from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {0: "No Click", 1: "Will Click"}

class AdClickRequest(BaseModel):
    Gender: str
    Age: int
    EstimatedSalary: int

@router.post("/predict/ad-click", response_model=PredictResponse)
def predict_ad_click(body: AdClickRequest):
    model = MODELS.get("ad-click")
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
