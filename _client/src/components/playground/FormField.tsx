import { cn } from '@/lib/cn';
import type { FeatureSchema } from '@/types/project';
import { useRef } from 'react';

interface Props {
  field: FeatureSchema;
}

const inputBase =
  'w-full rounded-sm border border-border-input bg-surface-input px-2.5 py-1.5 text-sm text-text-primary focus:border-border-strong focus:outline-none focus:ring-1 focus:ring-border-strong';

export const FormField = ({ field }: Props) => {
  const outputRef = useRef<HTMLOutputElement>(null);

  return (
    <div className="space-y-1.5">
      <div className="flex items-center justify-between">
        <label
          htmlFor={field.key}
          className="text-text-secondary text-xs font-medium"
        >
          {field.label}
        </label>
        {field.unit && (
          <span className="text-text-tertiary font-mono text-[9px] uppercase">
            {field.unit}
          </span>
        )}
      </div>

      {field.type === 'number' && (
        <input
          type="number"
          id={field.key}
          name={field.key}
          defaultValue={field.defaultValue}
          min={field.min}
          max={field.max}
          step={field.step}
          className={inputBase}
          required
        />
      )}

      {field.type === 'slider' && (
        <div className="flex items-center gap-3">
          <input
            type="range"
            id={field.key}
            name={field.key}
            defaultValue={field.defaultValue}
            min={field.min}
            max={field.max}
            step={field.step}
            className="bg-border-default accent-accent-burgundy h-1 w-full appearance-none rounded-full"
            required
            onChange={() => {
              if (outputRef.current) {
                outputRef.current.textContent = (
                  document.getElementById(field.key) as HTMLInputElement
                )?.value;
              }
            }}
          />
          <output
            ref={outputRef}
            id={`${field.key}-output`}
            className="text-text-primary w-10 shrink-0 text-right font-mono text-xs"
          >
            {field.defaultValue}
          </output>
        </div>
      )}

      {field.type === 'select' && field.options && (
        <select
          id={field.key}
          name={field.key}
          defaultValue={field.defaultValue}
          className={cn(inputBase, 'appearance-none')}
          required
        >
          {field.options.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      )}

      {field.hint && (
        <p className="text-text-tertiary text-[10px]">{field.hint}</p>
      )}
    </div>
  );
};
