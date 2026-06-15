import {
  ReportBlockquote,
  ReportChartContainer,
  ReportContainer,
  ReportHeader,
  ReportImage,
  ReportMetricGrid,
  ReportParagraph,
  ReportSection,
  ReportTable,
} from '@/components/eda/ReportComponents';
import { getEdaReport } from '@/lib/api';
import type { EdaReportData } from '@/types/eda';
import { useEffect, useMemo, useState, useTransition } from 'react';
import {
  Bar,
  BarChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

interface ProjectEdaReportProps {
  projectId: string;
}

export const ProjectEdaReport = ({ projectId }: ProjectEdaReportProps) => {
  const [report, setReport] = useState<EdaReportData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  useEffect(() => {
    let ignore = false;
    startTransition(async () => {
      try {
        setError(null);
        const data = await getEdaReport(projectId);
        if (!ignore) setReport(data);
      } catch (err: any) {
        if (!ignore) setError(err.message || 'Failed to load report.');
      }
    });
    return () => {
      ignore = true;
    };
  }, [projectId]);

  const tocSections = useMemo(
    () =>
      report ? report.sections.map((s) => ({ id: s.id, label: s.title })) : [],
    [report]
  );

  const handleRetry = () => {
    startTransition(async () => {
      try {
        setError(null);
        const data = await getEdaReport(projectId);
        setReport(data);
      } catch (err: any) {
        setError(err.message || 'Failed to load report.');
      }
    });
  };

  if (isPending && !report) {
    return (
      <div className="text-text-tertiary py-12 text-center font-mono text-xs">
        Loading dataset outline and analysis...
      </div>
    );
  }

  if (error || !report) {
    return (
      <div className="text-accent-burgundy py-12 text-center font-mono text-xs">
        <p>{error || 'No report available for this dataset.'}</p>
        <button
          onClick={handleRetry}
          disabled={isPending}
          className="border-accent-burgundy hover:bg-accent-burgundy/10 mt-4 rounded-sm border px-4 py-2 font-mono text-[11px] tracking-wider uppercase transition-colors disabled:opacity-50"
        >
          {isPending ? 'Loading...' : 'Retry'}
        </button>
      </div>
    );
  }

  return (
    <ReportContainer sections={tocSections}>
      <ReportHeader
        title={report.title}
        subtitle={report.subtitle}
        source={report.source}
        size={report.size}
      />

      {report.sections.map((section, idx) => (
        <ReportSection key={section.id} id={section.id} title={section.title}>
          {section.paragraphs.map((p, pIdx) => (
            <ReportParagraph key={pIdx}>{p}</ReportParagraph>
          ))}

          {/* Render Images if present */}
          {section.images?.map((img, imgIdx) => (
            <ReportImage
              key={imgIdx}
              src={img.url}
              alt={img.alt}
              caption={img.caption}
            />
          ))}

          {/* Render Metrics Grid if present */}
          {section.metrics?.length ? (
            <ReportMetricGrid metrics={section.metrics} />
          ) : null}

          {/* Render Chart right after section 2 (idx === 1) */}
          {idx === 1 && (
            <ReportChartContainer
              title={report.chart_title}
              caption={`1.1 — ${report.chart_title}`}
            >
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={report.chart_data}
                  margin={{ top: 0, right: 0, left: -20, bottom: 0 }}
                >
                  <XAxis
                    dataKey="name"
                    axisLine={{ stroke: 'var(--color-border-default)' }}
                    tickLine={false}
                    tick={{
                      fill: 'var(--color-text-secondary)',
                      fontSize: 10,
                      fontFamily: 'var(--font-mono)',
                    }}
                  />
                  <YAxis
                    axisLine={{ stroke: 'var(--color-border-default)' }}
                    tickLine={false}
                    tick={{
                      fill: 'var(--color-text-secondary)',
                      fontSize: 10,
                      fontFamily: 'var(--font-mono)',
                    }}
                  />
                  <Tooltip
                    cursor={{ fill: 'var(--color-surface-tertiary)' }}
                    content={({ active, payload }) => {
                      if (active && payload && payload.length) {
                        const cell = payload[0].payload;
                        return (
                          <div className="bg-surface-primary border-border-strong rounded-sm border p-2 font-mono text-xs shadow-sm">
                            <p className="text-text-primary font-bold">
                              {cell.name}
                            </p>
                            <p className="text-text-secondary mt-1">
                              {report.y_axis_label}: {cell.value}%
                            </p>
                          </div>
                        );
                      }
                      return null;
                    }}
                  />
                  <Bar
                    dataKey="value"
                    fill="var(--color-accent-burgundy)"
                    radius={[2, 2, 0, 0]}
                    barSize={32}
                  />
                </BarChart>
              </ResponsiveContainer>
            </ReportChartContainer>
          )}

          {/* Render Table if present */}
          {section.table ? (
            <ReportTable
              headers={section.table.headers}
              rows={section.table.rows}
              caption={section.table.caption}
            />
          ) : null}

          {/* Render Blockquote if present */}
          {section.blockquote ? (
            <ReportBlockquote citation={section.blockquote_citation}>
              {section.blockquote}
            </ReportBlockquote>
          ) : null}
        </ReportSection>
      ))}
    </ReportContainer>
  );
};
