from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.predict import PredictResponse
import pandas as pd
from main import MODELS

router = APIRouter()

class VideoGamesRequest(BaseModel):
    Platform: str
    Year: int
    Genre: str
    Publisher: str
    NA_Sales: float
    EU_Sales: float
    JP_Sales: float
    Other_Sales: float
    Global_Sales: float

@router.post("/predict/video-games", response_model=PredictResponse)
def predict_video_games(body: VideoGamesRequest):
    model = MODELS.get("video-games")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    X = pd.DataFrame([body.model_dump()])
    prediction = float(model.predict(X)[0])

    return PredictResponse(
        value=prediction,
        label=f"{prediction:.2f} Million Units",
        confidence=None,
        feature_importance=None,
    )
