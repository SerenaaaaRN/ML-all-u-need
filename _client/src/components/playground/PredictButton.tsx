import { cn } from '@/lib/cn';
import PlayIcon from '@hugeicons/react/PlayIcon';

const spinner = (
  <div className="absolute inset-0 flex translate-y-0 items-center justify-center">
    <div className="border-text-tertiary border-t-text-primary h-3.5 w-3.5 animate-spin rounded-full border-2" />
  </div>
);

export const PredictButton = ({ pending }: { pending: boolean }) => {
  return (
    <button
      type="submit"
      disabled={pending}
      className={cn(
        'group border-border-strong bg-surface-primary relative mt-4 flex w-full items-center justify-center gap-2 overflow-hidden rounded-sm border px-4 py-2.5 text-sm font-medium transition-all',
        pending
          ? 'cursor-not-allowed opacity-70'
          : 'hover:bg-surface-tertiary hover:border-text-primary text-text-primary'
      )}
    >
      <span
        className={cn(
          'flex items-center gap-2 transition-transform duration-300',
          pending ? 'invisible' : ''
        )}
      >
        <PlayIcon size={14} />
        Run Prediction
      </span>
      {pending && spinner}
    </button>
  );
};
