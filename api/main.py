from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.model_loader import load_all_models
from schemas.predict import EdaResponse
from services.eda_data import EDA_REPORTS

MODELS: dict = {}

app = FastAPI(title="ML Classic Showcase API", version="1.0.0")

@app.on_event("startup")
async def startup():
    MODELS.update(load_all_models())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/api/eda")
def list_eda_projects():
    return list(EDA_REPORTS.keys())

@app.get("/api/eda/{project_id}", response_model=EdaResponse)
def get_eda_report(project_id: str):
    if project_id not in EDA_REPORTS:
        raise HTTPException(status_code=404, detail="EDA report not found")
    return EDA_REPORTS[project_id]

from routers import (
    ad_click, diabetes, ai_student, rain, 
    telco_churn, titanic, video_games, wine_quality,
    medical_cost, heart_failure
)

app.include_router(ad_click.router, prefix="/api")
app.include_router(diabetes.router, prefix="/api")
app.include_router(ai_student.router, prefix="/api")
app.include_router(rain.router, prefix="/api")
app.include_router(telco_churn.router, prefix="/api")
app.include_router(titanic.router, prefix="/api")
app.include_router(video_games.router, prefix="/api")
app.include_router(wine_quality.router, prefix="/api")
app.include_router(medical_cost.router, prefix="/api")
app.include_router(heart_failure.router, prefix="/api")
