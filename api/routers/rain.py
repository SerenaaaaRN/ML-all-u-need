from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {0: "No Rain", 1: "Rain"}

class RainRequest(BaseModel):
    Location: str
    MinTemp: float
    MaxTemp: float
    Rainfall: float
    WindGustDir: str
    WindGustSpeed: int
    WindDir9am: str
    WindDir3pm: str
    WindSpeed9am: int
    WindSpeed3pm: int
    Humidity9am: int
    Humidity3pm: int
    Pressure9am: float
    Pressure3pm: float
    Temp9am: float
    Temp3pm: float
    RainToday: str

@router.post("/predict/rain", response_model=PredictResponse)
def predict_rain(body: RainRequest):
    model = MODELS.get("rain")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    X = pd.DataFrame([body.model_dump()])
    prediction = int(model.predict(X)[0])

    confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)[0]
        confidence = round(float(max(proba)) * 100, 1)

    feature_importance = None
    estimator = None
    if hasattr(model, "named_steps"):
        estimator = model.named_steps.get("model")
    else:
        estimator = model

    if estimator and hasattr(estimator, "feature_importances_"):
        importances = estimator.feature_importances_
        feature_names = X.columns
        try:
            if hasattr(model, "named_steps") and hasattr(model.named_steps["preprocessor"], "get_feature_names_out"):
                 feature_names = model.named_steps["preprocessor"].get_feature_names_out()
                 
            feature_importance = [
                {"feature": col, "importance": round(float(imp), 4)}
                for col, imp in sorted(
                    zip(feature_names, importances),
                    key=lambda x: x[1], reverse=True
                )
            ]
        except Exception:
            pass

    return PredictResponse(
        value=prediction,
        label=LABEL_MAP.get(prediction, str(prediction)),
        confidence=confidence,
        feature_importance=feature_importance,
    )
