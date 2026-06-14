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
import { useEffect, useReducer } from 'react';
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

type FetchState = {
  data: EdaReportData | null;
  loading: boolean;
  error: string | null;
};

function fetchReducer(
  _state: FetchState,
  action:
    | { type: 'fetch' }
    | { type: 'success'; data: EdaReportData }
    | { type: 'error'; error: string }
): FetchState {
  switch (action.type) {
    case 'fetch':
      return { data: null, loading: true, error: null };
    case 'success':
      return { data: action.data, loading: false, error: null };
    case 'error':
      return { data: null, loading: false, error: action.error };
  }
}

export const ProjectEdaReport = ({ projectId }: ProjectEdaReportProps) => {
  const [{ data: report, loading, error }, dispatch] = useReducer(
    fetchReducer,
    { data: null, loading: true, error: null }
  );

  useEffect(() => {
    let active = true;
    dispatch({ type: 'fetch' });

    getEdaReport(projectId)
      .then((data) => {
        if (active) dispatch({ type: 'success', data });
      })
      .catch((err) => {
        if (active)
          dispatch({
            type: 'error',
            error: err.message || 'Failed to load report.',
          });
      });

    return () => {
      active = false;
    };
  }, [projectId]);

  if (loading) {
    return (
      <div className="text-text-tertiary py-12 text-center font-mono text-xs">
        Loading dataset outline and analysis...
      </div>
    );
  }

  if (error || !report) {
    return (
      <div className="text-accent-burgundy py-12 text-center font-mono text-xs">
        {error || 'No report available for this dataset.'}
      </div>
    );
  }

  // Map sections for Table of Contents outline
  const tocSections = report.sections.map((s) => ({
    id: s.id,
    label: s.title,
  }));

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
          {section.metrics && section.metrics.length > 0 && (
            <ReportMetricGrid metrics={section.metrics} />
          )}

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
          {section.table && (
            <ReportTable
              headers={section.table.headers}
              rows={section.table.rows}
              caption={section.table.caption}
            />
          )}

          {/* Render Blockquote if present */}
          {section.blockquote && (
            <ReportBlockquote citation={section.blockquote_citation}>
              {section.blockquote}
            </ReportBlockquote>
          )}
        </ReportSection>
      ))}
    </ReportContainer>
  );
};
