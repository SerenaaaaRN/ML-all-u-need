import { Badge } from '@/components/shared/Badge';
import { categories } from '@/data/categories';
import { formatMetric } from '@/lib/formatters';
import type { ProjectMeta } from '@/types/project';
import { Link } from 'react-router-dom';

interface Props {
  project: ProjectMeta;
}

export const PageHeader = ({ project }: Props) => {
  const categoryLabel = categories[project.category].label;
  const mainGroup = project.category.includes('classification')
    ? 'Classification'
    : project.category === 'regression'
      ? 'Regression'
      : 'Unsupervised';

  return (
    <header className="mb-8">
      <nav className="text-text-tertiary mb-4 flex flex-wrap items-center gap-2 font-mono text-[10px] tracking-widest uppercase">
        <Link to="/" className="hover:text-text-primary transition-colors">
          Home
        </Link>
        <span>/</span>
        <span>{mainGroup}</span>
        <span>/</span>
        <span className="text-accent-burgundy font-semibold">
          {project.name}
        </span>
      </nav>

      <div className="flex items-center gap-2">
        <span className="text-text-tertiary font-mono text-[10px] tracking-widest uppercase">
          {categoryLabel}
        </span>
        {!project.isAvailable && (
          <Badge
            variant="default"
            className="text-accent-amber border-accent-amber"
          >
            Coming Soon
          </Badge>
        )}
      </div>
      <h1 className="text-text-primary mt-1 font-serif text-2xl font-semibold md:text-3xl">
        {project.name}
      </h1>
      <p className="text-text-secondary mt-2 max-w-2xl font-sans text-sm leading-relaxed">
        {project.description}
      </p>

      <div className="mt-6 flex flex-wrap gap-4">
        <MetricChip
          label={project.metricName}
          value={formatMetric(project.metricValue, project.metricName)}
        />
        <MetricChip label="Model" value={project.bestModel} />
        <MetricChip
          label="Dataset"
          value={`${project.datasetSize.toLocaleString()} rows`}
        />
      </div>
    </header>
  );
};

const MetricChip = ({ label, value }: { label: string; value: string }) => {
  if (!value) return null;

  return (
    <div className="flex items-center gap-1.5 font-mono text-xs">
      <span className="text-text-secondary tracking-widest uppercase">
        {label}:
      </span>
      <span className="text-text-primary font-medium">{value}</span>
    </div>
  );
};
