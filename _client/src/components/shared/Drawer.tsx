import { cn } from '@/lib/cn';
import Cancel01Icon from '@hugeicons/react/Cancel01Icon';
import { type ComponentPropsWithoutRef, useEffect, useRef } from 'react';

interface Props extends ComponentPropsWithoutRef<'div'> {
  isOpen: boolean;
  onClose: () => void;
}

export const Drawer = ({
  isOpen,
  onClose,
  className,
  children,
  ...props
}: Props) => {
  const onCloseRef = useRef(onClose);
  onCloseRef.current = onClose;

  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onCloseRef.current();
    };

    if (isOpen) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleEscape);
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.body.style.overflow = 'unset';
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex md:hidden"
      aria-modal="true"
      role="dialog"
    >
      <div
        className="bg-text-primary/50 fixed inset-0 backdrop-blur-sm transition-opacity"
        onClick={onClose}
        aria-hidden="true"
      />
      <div
        className={cn(
          'bg-surface-primary animate-fade-in-right relative flex h-full w-full max-w-sidebar-mobile flex-col overflow-y-auto shadow-xl',
          className
        )}
        {...props}
      >
        <button
          onClick={onClose}
          className="text-text-tertiary hover:text-text-primary absolute top-4 right-4 transition-colors"
          aria-label="Close drawer"
        >
          <Cancel01Icon size={24} />
        </button>
        {children}
      </div>
    </div>
  );
};
