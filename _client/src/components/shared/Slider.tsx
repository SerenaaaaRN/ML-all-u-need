import { cn } from '@/lib/cn';
import type { ChangeEvent, InputHTMLAttributes } from 'react';

interface SliderProps extends Omit<
  InputHTMLAttributes<HTMLInputElement>,
  'type'
> {
  /** Nilai saat ini (controlled) */
  value?: number;
  /** Callback saat nilai berubah */
  onValueChange?: (value: number) => void;
}

function Slider({
  className,
  defaultValue,
  value,
  min = 0,
  max = 100,
  step = 1,
  onValueChange,
  onChange,
  ...props
}: SliderProps) {
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const numValue = Number(e.target.value);
    onValueChange?.(numValue);
    onChange?.(e);
  };

  return (
    <input
      type="range"
      data-slot="slider"
      min={min}
      max={max}
      step={step}
      defaultValue={defaultValue}
      value={value}
      onChange={handleChange}
      className={cn(
        'bg-muted relative h-1.5 w-full cursor-pointer appearance-none rounded-full',
        '[&::-webkit-slider-thumb]:border-ring [&::-webkit-slider-thumb]:size-3 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:border [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:transition-[color,box-shadow]',
        '[&::-webkit-slider-thumb]:hover:ring-3 [&::-webkit-slider-thumb]:focus-visible:ring-3 [&::-webkit-slider-thumb]:focus-visible:outline-hidden [&::-webkit-slider-thumb]:active:ring-3',
        '[&::-moz-range-thumb]:border-ring [&::-moz-range-thumb]:size-3 [&::-moz-range-thumb]:appearance-none [&::-moz-range-thumb]:rounded-full [&::-moz-range-thumb]:border [&::-moz-range-thumb]:bg-white [&::-moz-range-thumb]:transition-[color,box-shadow]',
        'disabled:pointer-events-none disabled:opacity-50',
        className
      )}
      {...props}
    />
  );
}

export { Slider, type SliderProps };
