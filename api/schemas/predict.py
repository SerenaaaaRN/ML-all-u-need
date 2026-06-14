from pydantic import BaseModel
from typing import Union, List

class FeatureImportanceItem(BaseModel):
    feature: str
    importance: float

class PredictResponse(BaseModel):
    value: Union[str, float]
    label: str
    confidence: float | None = None
    feature_importance: list[FeatureImportanceItem] | None = None

class EdaInsightItem(BaseModel):
    title: str
    description: str

class EdaChartPoint(BaseModel):
    name: str
    value: float

class EdaTable(BaseModel):
    headers: List[str]
    rows: List[List[Union[str, float]]]
    caption: str | None = None

class EdaMetricItem(BaseModel):
    label: str
    value: Union[str, float]
    description: str | None = None

class EdaImage(BaseModel):
    url: str
    alt: str | None = None
    caption: str | None = None

class EdaSection(BaseModel):
    id: str
    title: str
    paragraphs: List[str]
    blockquote: str | None = None
    blockquote_citation: str | None = None
    metrics: List[EdaMetricItem] | None = None
    table: EdaTable | None = None
    images: List[EdaImage] | None = None

class EdaResponse(BaseModel):
    title: str
    subtitle: str
    source: str
    size: int
    chart_title: str
    chart_data: List[EdaChartPoint]
    x_axis_label: str
    y_axis_label: str
    sections: List[EdaSection]
