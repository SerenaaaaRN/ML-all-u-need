export type EdaInsightItem = {
  title: string;
  description: string;
};

export type EdaChartPoint = {
  name: string;
  value: number;
};

export type EdaTable = {
  headers: string[];
  rows: (string | number)[][];
  caption?: string;
};

export type EdaMetricItem = {
  label: string;
  value: string | number;
  description?: string;
};

export type EdaImage = {
  url: string;
  alt?: string;
  caption?: string;
};

export type EdaSection = {
  id: string;
  title: string;
  paragraphs: string[];
  blockquote?: string;
  blockquote_citation?: string;
  metrics?: EdaMetricItem[];
  table?: EdaTable;
  images?: EdaImage[];
};

export type EdaReportData = {
  title: string;
  subtitle: string;
  source: string;
  size: number;
  chart_title: string;
  chart_data: EdaChartPoint[];
  x_axis_label: string;
  y_axis_label: string;
  sections: EdaSection[];
};
