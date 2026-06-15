from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {0: "Did Not Survive", 1: "Survived"}

RARE_TITLES = ['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']

def _feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(RARE_TITLES, 'Rare')
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    df.drop(columns=['Name'], inplace=True)
    medians = df.groupby(['Title', 'Pclass'])['Age'].transform('median')
    df['Age'] = df['Age'].fillna(medians)
    if df['Age'].isnull().any():
        df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0] if not df['Embarked'].mode().empty else 'S')
    df['Pclass'] = df['Pclass'].astype(str)
    return df


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

    X = _feature_engineering(pd.DataFrame([body.model_dump()]))
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
