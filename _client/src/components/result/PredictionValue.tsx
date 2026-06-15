import { cn } from '@/lib/cn';
import ChartHistogramIcon from '@hugeicons/react/ChartHistogramIcon';

interface Props {
  label: string;
  value: string | number;
  confidence?: number;
}

export const PredictionValue = ({ label, value, confidence }: Props) => {
  return (
    <div>
      <div className="mb-5 flex items-center gap-2">
        <ChartHistogramIcon size={14} className="text-text-tertiary" />
        <span className="text-text-tertiary font-mono text-[10px] tracking-widest uppercase">
          Prediction Result
        </span>
      </div>

      <div className="bg-surface-secondary border-border-default rounded-sm border p-5">
        <div className="flex flex-wrap items-end justify-between gap-4">
          <div className="min-w-0">
            <div className="text-text-tertiary mb-1 font-mono text-[10px] tracking-wider uppercase">
              Predicted Class
            </div>
            <div className="text-text-primary font-serif text-3xl wrap-break-word md:text-4xl">
              {label}
            </div>
          </div>

          {confidence !== undefined ? (
            <div className="text-right">
              <div className="text-text-tertiary mb-1 font-mono text-[10px] tracking-wider uppercase">
                Confidence
              </div>
              <div
                className={cn(
                  'font-serif text-2xl md:text-3xl',
                  confidence > 80
                    ? 'text-accent-forest'
                    : confidence > 60
                      ? 'text-accent-amber'
                      : 'text-accent-muted-red'
                )}
              >
                {confidence}%
              </div>
            </div>
          ) : null}
        </div>

        {confidence !== undefined ? (
          <div className="mt-4">
            <div className="bg-border-default h-2 w-full overflow-hidden rounded-full">
              <div
                className={cn(
                  'h-full rounded-full transition-all duration-1000 ease-out',
                  confidence > 80
                    ? 'bg-accent-forest'
                    : confidence > 60
                      ? 'bg-accent-amber'
                      : 'bg-accent-muted-red'
                )}
                style={{ width: `${confidence}%` }}
              />
            </div>
          </div>
        ) : null}

        <div className="text-text-tertiary mt-3 font-mono text-[11px]">
          Raw value: {value}
        </div>
      </div>
    </div>
  );
};
