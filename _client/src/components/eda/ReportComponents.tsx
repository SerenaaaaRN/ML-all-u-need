import { type ReactNode } from 'react';

interface ReportContainerProps {
  sections: { id: string; label: string }[];
  children: ReactNode;
}

export const ReportContainer = ({
  sections,
  children,
}: ReportContainerProps) => {
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <div className="grid grid-cols-1 gap-8 lg:grid-cols-12">
      {/* Sticky Table of Contents Sidebar */}
      <aside className="border-border-default hidden self-start border-r pr-6 lg:sticky lg:top-8 lg:col-span-3 lg:block">
        <h4 className="text-text-primary mb-4 font-serif text-xs font-semibold tracking-wider uppercase">
          Report Outline
        </h4>
        <nav className="flex flex-col gap-3 font-mono text-[11px] tracking-wider uppercase">
          {sections.map((section) => (
            <button
              key={section.id}
              onClick={() => scrollToSection(section.id)}
              className="text-text-secondary hover:text-accent-burgundy text-left transition-colors focus:outline-none"
            >
              • {section.label}
            </button>
          ))}
        </nav>
      </aside>

      {/* Main Report Content */}
      <article className="max-w-3xl space-y-8 pb-16 lg:col-span-9">
        {children}
      </article>
    </div>
  );
};

interface ReportHeaderProps {
  title: string;
  subtitle: string;
  source: string;
  size: number;
}

export const ReportHeader = ({
  title,
  subtitle,
  source,
  size,
}: ReportHeaderProps) => {
  return (
    <header className="border-text-primary mb-8 border-b-2 pb-6">
      <span className="text-accent-burgundy font-mono text-[10px] font-semibold tracking-widest uppercase">
        Exploratory Data Analysis Report
      </span>
      <h1 className="text-text-primary mt-2 font-serif text-3xl font-semibold">
        {title}
      </h1>
      <p className="text-text-secondary mt-1 font-sans text-sm leading-relaxed">
        {subtitle}
      </p>
      <div className="text-text-tertiary mt-4 flex flex-wrap gap-x-6 gap-y-2 font-mono text-[10px] tracking-wider uppercase">
        <span>
          Source: <strong className="text-text-secondary">{source}</strong>
        </span>
        <span>
          Observations:{' '}
          <strong className="text-text-secondary">
            {size.toLocaleString()} rows
          </strong>
        </span>
      </div>
    </header>
  );
};

interface ReportSectionProps {
  id: string;
  title: string;
  children: ReactNode;
}

export const ReportSection = ({ id, title, children }: ReportSectionProps) => {
  return (
    <section id={id} className="scroll-mt-6 space-y-4">
      <h2 className="text-text-primary border-border-default border-b pb-2 font-serif text-xl font-semibold">
        {title}
      </h2>
      <div className="space-y-4">{children}</div>
    </section>
  );
};

export const ReportParagraph = ({ children }: { children: ReactNode }) => {
  return (
    <p className="text-text-secondary text-justify font-sans text-sm leading-relaxed">
      {children}
    </p>
  );
};

export const ReportBlockquote = ({
  children,
  citation,
}: {
  children: ReactNode;
  citation?: string;
}) => {
  return (
    <div className="border-accent-burgundy bg-surface-tertiary/40 my-6 rounded-sm border-l-4 px-6 py-4">
      <p className="text-text-primary font-serif text-sm leading-relaxed italic">
        "{children}"
      </p>
      {citation ? (
        <span className="text-text-secondary mt-2 block text-right font-mono text-[10px] tracking-wider uppercase">
          — {citation}
        </span>
      ) : null}
    </div>
  );
};

interface ReportTableProps {
  headers: string[];
  rows: (string | number)[][];
  caption?: string;
}

export const ReportTable = ({ headers, rows, caption }: ReportTableProps) => {
  return (
    <div className="my-6 space-y-2">
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-left font-sans text-xs">
          {/* LaTeX Booktabs style borders */}
          <thead>
            <tr className="border-text-primary text-text-secondary border-t-2 border-b font-mono text-[10px] tracking-wider uppercase">
              {headers.map((h, i) => (
                <th
                  key={i}
                  className="px-3 py-2 font-semibold first:pl-0 last:pr-0"
                >
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, rowIndex) => (
              <tr
                key={rowIndex}
                className="border-border-default hover:bg-surface-tertiary/20 border-b"
              >
                {row.map((val, cellIndex) => {
                  const isNum = typeof val === 'number';
                  return (
                    <td
                      key={cellIndex}
                      className={`text-text-primary px-3 py-2 first:pl-0 last:pr-0 ${
                        isNum ? 'font-mono' : 'font-sans'
                      }`}
                    >
                      {val}
                    </td>
                  );
                })}
              </tr>
            ))}
            {/* Bottom thick rule */}
            <tr className="border-text-primary border-t-2">
              <td colSpan={headers.length}></td>
            </tr>
          </tbody>
        </table>
      </div>
      {caption ? (
        <p className="text-text-secondary text-center font-serif text-[11px] italic">
          Table {caption}
        </p>
      ) : null}
    </div>
  );
};

interface ReportChartContainerProps {
  title: string;
  caption?: string;
  children: ReactNode;
}

export const ReportChartContainer = ({
  title,
  caption,
  children,
}: ReportChartContainerProps) => {
  return (
    <div className="bg-surface-secondary border-border-default my-6 flex flex-col items-center rounded-sm border p-6">
      <h4 className="text-text-primary mb-1 self-start font-serif text-sm font-semibold">
        {title}
      </h4>
      <span className="text-text-tertiary mb-6 self-start font-mono text-[9px] tracking-widest uppercase">
        Figure visualization
      </span>
      <div className="h-60 w-full">{children}</div>
      {caption ? (
        <p className="text-text-secondary mt-4 text-center font-serif text-[11px] italic">
          Figure {caption}
        </p>
      ) : null}
    </div>
  );
};

interface ReportImageProps {
  src: string;
  alt?: string;
  caption?: string;
}

export const ReportImage = ({ src, alt, caption }: ReportImageProps) => {
  return (
    <div className="border-border-default my-6 flex flex-col items-center rounded-sm border bg-transparent p-2">
      <img
        src={src}
        alt={alt ?? ''}
        className="h-auto max-h-96 w-full rounded object-contain"
        loading="lazy"
      />
      {caption ? (
        <p className="text-text-secondary mt-2 text-center font-serif text-[11px] italic">
          {caption}
        </p>
      ) : null}
    </div>
  );
};

interface ReportMetricGridProps {
  metrics: { label: string; value: string | number; description?: string }[];
}

export const ReportMetricGrid = ({ metrics }: ReportMetricGridProps) => {
  return (
    <div className="my-6 grid grid-cols-2 gap-4 md:grid-cols-4">
      {metrics.map((metric, i) => (
        <div
          key={i}
          className="bg-surface-secondary border-border-default flex flex-col justify-between rounded-sm border p-4"
        >
          <span className="text-text-secondary font-mono text-[9px] tracking-wider uppercase">
            {metric.label}
          </span>
          <span className="text-text-primary mt-2 font-mono text-xl font-bold">
            {metric.value}
          </span>
          {metric.description ? (
            <span className="text-text-tertiary mt-1 font-sans text-[10px]">
              {metric.description}
            </span>
          ) : null}
        </div>
      ))}
    </div>
  );
};
