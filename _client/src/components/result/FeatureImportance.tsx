import type { FeatureImportanceItem } from '@/types/prediction';
import {
  Bar,
  BarChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

interface Props {
  data: FeatureImportanceItem[];
}

export const FeatureImportance = ({ data }: Props) => {
  if (!data || data.length === 0) return null;

  const chartData = data
    .slice(0, 8)
    .map((item) => ({
      name:
        item.feature.length > 15
          ? item.feature.substring(0, 15) + '...'
          : item.feature,
      fullFeature: item.feature,
      value: item.importance * 100,
    }))
    .reverse();

  return (
    <div className="border-border-default mt-8 border-t pt-8">
      <h3 className="text-text-tertiary mb-6 font-mono text-[10px] tracking-widest uppercase">
        Feature Importance
      </h3>

      <div className="h-62.5 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={chartData}
            layout="vertical"
            margin={{ top: 0, right: 0, left: 0, bottom: 0 }}
          >
            <XAxis type="number" hide />
            <YAxis
              dataKey="name"
              type="category"
              axisLine={false}
              tickLine={false}
              tick={{
                fill: 'var(--color-text-secondary)',
                fontSize: 12,
                fontFamily: 'var(--font-mono)',
              }}
              width={120}
            />
            <Tooltip
              cursor={{ fill: 'var(--color-surface-tertiary)' }}
              content={({ active, payload }) => {
                if (active && payload && payload.length) {
                  const data = payload[0].payload;
                  return (
                    <div className="bg-surface-primary border-border-strong rounded-sm border p-2 shadow-sm">
                      <p className="text-text-primary text-sm font-medium">
                        {data.fullFeature}
                      </p>
                      <p className="text-text-secondary mt-1 font-mono text-xs">
                        Importance: {(data.value / 100).toFixed(4)}
                      </p>
                    </div>
                  );
                }
                return null;
              }}
            />
            <Bar
              dataKey="value"
              fill="var(--color-border-strong)"
              radius={[0, 2, 2, 0]}
              barSize={12}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
