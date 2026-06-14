export interface FeatureImportanceItem {
  feature: string;
  importance: number;
}

export interface PredictionResult {
  value: string | number;
  label: string;
  confidence?: number;
  featureImportance?: FeatureImportanceItem[];
}
