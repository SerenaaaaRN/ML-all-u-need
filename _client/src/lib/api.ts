import type { ApiError } from '@/types/api';
import type { EdaReportData } from '@/types/eda';
import type { PredictionResult } from '@/types/prediction';

const API_BASE = import.meta.env.VITE_API_URL || '';

export const predict = async (
  projectId: string,
  features: Record<string, number | string>
): Promise<PredictionResult> => {
  const res = await fetch(`${API_BASE}/api/predict/${projectId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(features),
  });

  if (!res.ok) {
    const err: ApiError = await res
      .json()
      .catch(() => ({ detail: 'Unknown error' }));
    throw new Error(err.detail);
  }

  const data = await res.json();

  return {
    ...data,
    featureImportance: data.feature_importance,
  };
};

export const getEdaProjects = async (): Promise<string[]> => {
  const res = await fetch(`${API_BASE}/api/eda`);

  if (!res.ok) {
    throw new Error('Failed to fetch EDA project list.');
  }

  return res.json();
};

export const getEdaReport = async (
  projectId: string
): Promise<EdaReportData> => {
  const res = await fetch(`${API_BASE}/api/eda/${projectId}`);

  if (!res.ok) {
    throw new Error('Failed to fetch EDA report.');
  }

  return res.json();
};
