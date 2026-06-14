export type ProjectCategory =
  | 'binary-classification'
  | 'multiclass-classification'
  | 'regression';

export type FeatureType = 'number' | 'slider' | 'select';

export interface FeatureSchema {
  key: string;
  label: string;
  type: FeatureType;
  min?: number;
  max?: number;
  step?: number;
  options?: { label: string; value: string | number }[];
  defaultValue: number | string;
  unit?: string;
  hint?: string;
}

export interface ProjectMeta {
  id: string;
  name: string;
  description: string;
  imageUrl?: string;
  category: ProjectCategory;
  bestModel: string;
  metricName: string;
  metricValue: number;
  datasetSource: string;
  datasetSize: number;
  features: FeatureSchema[];
  isAvailable: boolean;
  notebookPath: string;
}
