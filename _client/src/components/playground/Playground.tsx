import { ProjectEdaReport } from '@/components/eda/ProjectEdaReport';
import { PageHeader } from '@/components/layout/PageHeader';
import { InputForm } from '@/components/playground/InputForm';
import { ResultPanel } from '@/components/result/ResultPanel';
import { getEdaProjects } from '@/lib/api';
import { getProjectById } from '@/data/projects';
import type { PredictionResult } from '@/types/prediction';
import { useEffect, useState } from 'react';
import { Navigate, useParams } from 'react-router-dom';

export const Playground = () => {
  const { projectId } = useParams<{ projectId: string }>();
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [activeTab, setActiveTab] = useState<'playground' | 'eda'>('eda');
  const [edaProjects, setEdaProjects] = useState<string[]>([]);

  useEffect(() => {
    getEdaProjects().then(setEdaProjects).catch(() => {});
  }, []);

  if (!projectId) return <Navigate to="/" replace />;

  const project = getProjectById(projectId);

  if (!project) return <Navigate to="/" replace />;

  if (!project.isAvailable) {
    return (
      <div className="animate-fade-in">
        <PageHeader project={project} />
        <div className="border-border-strong bg-surface-secondary mt-12 rounded-sm border border-dashed p-12 text-center">
          <h2 className="text-text-secondary font-serif text-xl">
            Model Integration Pending
          </h2>
          <p className="text-text-tertiary mt-2">
            The frontend schema for this model is currently being finalized.
          </p>
        </div>
      </div>
    );
  }

  const hasEda = edaProjects.includes(project.id);

  return (
    <div className="animate-fade-in">
      <PageHeader project={project} />

      {/* Tabs Menu */}
      <div className="border-border-default mb-6 flex border-b font-mono text-xs tracking-wider uppercase">
        {hasEda && (
          <button
            onClick={() => setActiveTab('eda')}
            className={`-mb-0.5 border-b-2 px-4 py-2 transition-colors ${
              activeTab === 'eda'
                ? 'border-accent-burgundy text-text-primary font-medium'
                : 'text-text-tertiary hover:text-text-primary border-transparent'
            }`}
          >
            Dataset Insights (EDA)
          </button>
        )}
        <button
          onClick={() => setActiveTab('playground')}
          className={`-mb-0.5 border-b-2 px-4 py-2 transition-colors ${
            activeTab === 'playground'
              ? 'border-accent-burgundy text-text-primary font-medium'
              : 'text-text-tertiary hover:text-text-primary border-transparent'
          }`}
        >
          Model Playground
        </button>
      </div>

      {/* Playground Tab */}
      {activeTab === 'playground' && (
        <div className="animate-fade-in grid grid-cols-1 gap-6 lg:grid-cols-12 lg:gap-8">
          <div className="lg:col-span-5 xl:col-span-4">
            <InputForm project={project} onResult={setResult} />
          </div>

          <div className="lg:col-span-7 xl:col-span-8">
            <ResultPanel result={result} />
          </div>
        </div>
      )}

      {/* EDA Tab */}
      {activeTab === 'eda' && hasEda && (
        <div className="animate-fade-in">
          <ProjectEdaReport projectId={project.id} />
        </div>
      )}
    </div>
  );
};
