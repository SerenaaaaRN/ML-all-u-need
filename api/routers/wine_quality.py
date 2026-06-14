from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {
    3: "Poor", 
    4: "Below Average", 
    5: "Average", 
    6: "Good", 
    7: "Very Good", 
    8: "Excellent"
}

class WineQualityRequest(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@router.post("/predict/wine-quality", response_model=PredictResponse)
def predict_wine_quality(body: WineQualityRequest):
    model = MODELS.get("wine-quality")
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
                {"feature": col.replace("num__", ""), "importance": round(float(imp), 4)}
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
