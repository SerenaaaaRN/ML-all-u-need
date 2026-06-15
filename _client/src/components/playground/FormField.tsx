import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/shared/Select';
import { Slider } from '@/components/shared/Slider';
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
        {field.unit ? (
          <span className="text-text-tertiary font-mono text-[9px] uppercase">
            {field.unit}
          </span>
        ) : null}
      </div>

      {field.type === 'number' ? (
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
      ) : null}

      {field.type === 'slider' ? (
        <div className="flex items-center gap-3">
          <Slider
            id={field.key}
            name={field.key}
            defaultValue={field.defaultValue}
            min={field.min}
            max={field.max}
            step={field.step}
            className="bg-border-default accent-accent-burgundy h-1"
            required
            onValueChange={(value) => {
              if (outputRef.current) {
                outputRef.current.textContent = String(value);
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
      ) : null}

      {field.type === 'select' && field.options ? (
        <Select name={field.key} defaultValue={String(field.defaultValue)}>
          <SelectTrigger id={field.key} className={cn(inputBase)}>
            <SelectValue placeholder="Pilih..." />
          </SelectTrigger>
          <SelectContent>
            {field.options.map((opt) => (
              <SelectItem key={String(opt.value)} value={String(opt.value)}>
                {opt.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      ) : null}

      {field.hint ? (
        <p className="text-text-tertiary text-[10px]">{field.hint}</p>
      ) : null}
    </div>
  );
};
