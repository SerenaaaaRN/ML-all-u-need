from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()

class MedicalCost(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

@router.post("/predict/med-cost", response_model=PredictResponse)
def predict_medical_cost(body: MedicalCost):

    model = MODELS.get("med-cost")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    X = pd.DataFrame([body.model_dump()])
    prediction = float(model.predict(X)[0])

    return PredictResponse(
        value=prediction,
        label=f"{prediction:.2f}",
        confidence=None,
        feature_importance=None,
    )
