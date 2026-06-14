import { cn } from '@/lib/cn';
import { type ComponentPropsWithoutRef } from 'react';

interface Props extends ComponentPropsWithoutRef<'span'> {
  variant?: 'default' | 'category' | 'outline';
}

const baseClasses =
  'inline-flex items-center rounded-sm px-2 py-0.5 font-mono text-[10px] uppercase tracking-widest';

const variants = {
  default:
    'bg-surface-tertiary border border-border-default text-text-secondary',
  category: 'bg-transparent text-text-secondary font-bold tracking-widest',
  outline: 'bg-transparent border border-border-default text-text-secondary',
};

export const Badge = ({
  className,
  variant = 'default',
  children,
  ...props
}: Props) => {
  return (
    <span className={cn(baseClasses, variants[variant], className)} {...props}>
      {children}
    </span>
  );
};
