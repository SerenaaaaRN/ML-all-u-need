from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()
LABEL_MAP = {0: "Low Burnout", 1: "Medium Burnout", 2: "High Burnout"}

class AIStudentRequest(BaseModel):
    Pre_Semester_GPA: float = Field(ge=0.0, le=4.0)
    Weekly_GenAI_Hours: float = Field(ge=0.0)
    Traditional_Study_Hours: float = Field(ge=0.0)
    Perceived_AI_Dependency: float = Field(ge=1.0, le=10.0)
    Anxiety_Level_During_Exams: float = Field(ge=1.0, le=10.0)
    Tool_Diversity: int = Field(ge=0)
    Paid_Subscription: int = Field(ge=0, le=1)
    Year_of_Study: str
    Prompt_Engineering_Skill: str
    Major_Category: str
    Primary_Use_Case: str
    Institutional_Policy: str

@router.post("/predict/ai-student", response_model=PredictResponse)
def predict_ai_student(body: AIStudentRequest):
    model = MODELS.get("ai-student")
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
