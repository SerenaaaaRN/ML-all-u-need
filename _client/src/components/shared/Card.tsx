import { cn } from '@/lib/cn';
import type { ComponentProps } from 'react';

function Card({
  className,
  size = 'default',
  ...props
}: ComponentProps<'div'> & { size?: 'default' | 'sm' }) {
  return (
    <div
      data-slot="card"
      data-size={size}
      className={cn(
        'group/card border-border-default bg-surface-secondary flex flex-col overflow-hidden rounded-sm border shadow-sm',
        'p-6 md:p-8',
        'data-[size=sm]:p-4 md:data-[size=sm]:p-5',
        'has-data-[slot=card-footer]:pb-0 has-data-[slot=card-header]:pt-0',
        'has-[>img:first-child]:pt-0',
        className
      )}
      {...props}
    />
  );
}

function CardHeader({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="card-header"
      className={cn(
        'grid auto-rows-min items-start gap-1',
        'pt-6 pb-4 md:pt-8 md:pb-4',
        'group-data-[size=sm]/card:pt-4 group-data-[size=sm]/card:pb-3 md:group-data-[size=sm]/card:pt-5 md:group-data-[size=sm]/card:pb-3',
        'has-data-[slot=card-action]:grid-cols-[1fr_auto]',
        className
      )}
      {...props}
    />
  );
}

function CardTitle({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="card-title"
      className={cn(
        'text-text-primary font-serif text-xl font-medium',
        'group-data-[size=sm]/card:text-lg',
        className
      )}
      {...props}
    />
  );
}

function CardDescription({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="card-description"
      className={cn('text-text-secondary text-sm', className)}
      {...props}
    />
  );
}

function CardAction({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="card-action"
      className={cn(
        'col-start-2 row-span-2 row-start-1 self-start justify-self-end',
        className
      )}
      {...props}
    />
  );
}

function CardContent({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="card-content"
      className={cn('flex-1', className)}
      {...props}
    />
  );
}

function CardFooter({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="card-footer"
      className={cn(
        'border-border-default bg-surface-tertiary/50 flex items-center rounded-b-sm border-t',
        'py-6 md:py-8',
        'group-data-[size=sm]/card:py-4 md:group-data-[size=sm]/card:py-5',
        className
      )}
      {...props}
    />
  );
}

export {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
};
