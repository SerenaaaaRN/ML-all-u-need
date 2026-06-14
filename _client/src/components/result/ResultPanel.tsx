import { FeatureImportance } from '@/components/result/FeatureImportance';
import { Card, CardContent } from '@/components/shared/Card';
import type { PredictionResult } from '@/types/prediction';
import ChartHistogramIcon from '@hugeicons/react/ChartHistogramIcon';
import { PredictionValue } from '@/components/result/PredictionValue';

interface Props {
  result: PredictionResult | null;
}

export const ResultPanel = ({ result }: Props) => {
  if (!result) {
    return (
      <Card className="items-center justify-center text-center opacity-70">
        <CardContent className="flex flex-col items-center py-12">
          <div className="bg-surface-tertiary text-text-tertiary mb-4 rounded-full p-4">
            <ChartHistogramIcon size={32} />
          </div>
          <p className="text-text-secondary font-serif text-lg">
            Awaiting Input
          </p>
          <p className="text-text-tertiary mt-2 max-w-xs font-sans text-sm">
            Fill out the features form and run prediction to see the model's
            output here.
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="animate-fade-in h-full">
      <CardContent>
        <PredictionValue
          label={result.label}
          value={result.value}
          confidence={result.confidence}
        />

        {result.featureImportance && (
          <div className="mt-auto">
            <FeatureImportance data={result.featureImportance} />
          </div>
        )}
      </CardContent>
    </Card>
  );
};