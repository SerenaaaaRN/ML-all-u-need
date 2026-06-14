import { FormField } from '@/components/playground/FormField';
import { PredictButton } from '@/components/playground/PredictButton';
import {
  Card,
  CardAction,
  CardContent,
  CardHeader,
  CardTitle,
} from '@/components/shared/Card';
import { predict } from '@/lib/api';
import { extractFeatures } from '@/lib/formatters';
import type { PredictionResult } from '@/types/prediction';
import type { ProjectMeta } from '@/types/project';
import { useActionState } from 'react';

interface Props {
  project: ProjectMeta;
  onResult: (result: PredictionResult | null) => void;
}

export const InputForm = ({ project, onResult }: Props) => {
  const [error, submitAction] = useActionState(
    async (_prevState: string | null, formData: FormData) => {
      try {
        onResult(null);

        const features = extractFeatures(formData, project.features);
        const result = await predict(project.id, features);

        onResult(result);
        return null;
      } catch (err: any) {
        return err.message || 'Failed to run prediction';
      }
    },
    null
  );

  return (
    <Card>
      <CardHeader>
        <CardTitle>Input Features</CardTitle>
        <CardAction>
          <span className="text-text-tertiary font-mono text-[10px] tracking-wider uppercase">
            {project.features.length} fields
          </span>
        </CardAction>
      </CardHeader>
      <CardContent>
        <form action={submitAction} className="flex flex-1 flex-col">
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            {project.features.map((field) => (
              <FormField key={field.key} field={field} />
            ))}
          </div>

          {error && (
            <div className="bg-accent-burgundy/10 border-accent-burgundy/20 text-accent-burgundy mt-4 rounded-sm border p-3 text-sm">
              {error}
            </div>
          )}

          <PredictButton />
        </form>
      </CardContent>
    </Card>
  );
};
