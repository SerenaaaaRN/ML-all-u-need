from pydantic import BaseModel
from typing import Union

class FeatureImportanceItem(BaseModel):
    feature: str
    importance: float

class PredictResponse(BaseModel):
    value: Union[str, float]
    label: str
    confidence: float | None = None
    feature_importance: list[FeatureImportanceItem] | None = None
