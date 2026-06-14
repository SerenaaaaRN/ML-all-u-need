from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {0: "Did Not Survive", 1: "Survived"}

class TitanicRequest(BaseModel):
    Pclass: int
    Name: str
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

@router.post("/predict/titanic", response_model=PredictResponse)
def predict_titanic(body: TitanicRequest):
    model = MODELS.get("titanic")
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
            if hasattr(model, "named_steps") and hasattr(model.named_steps["column_transformer"], "get_feature_names_out"):
                 feature_names = model.named_steps["column_transformer"].get_feature_names_out()
                 
            feature_importance = [
                {"feature": col.replace("cat__", "").replace("num__", ""), "importance": round(float(imp), 4)}
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
