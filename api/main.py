from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.model_loader import load_all_models

MODELS: dict = {}

app = FastAPI(title="ML Classic Showcase API", version="1.0.0")

@app.on_event("startup")
async def startup():
    MODELS.update(load_all_models())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

from routers import (
    ad_click, diabetes, ai_student, rain, 
    telco_churn, titanic, video_games, wine_quality
)

app.include_router(ad_click.router, prefix="/api")
app.include_router(diabetes.router, prefix="/api")
app.include_router(ai_student.router, prefix="/api")
app.include_router(rain.router, prefix="/api")
app.include_router(telco_churn.router, prefix="/api")
app.include_router(titanic.router, prefix="/api")
app.include_router(video_games.router, prefix="/api")
app.include_router(wine_quality.router, prefix="/api")
