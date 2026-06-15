import { cn } from '@/lib/cn';
import ArrowDown01Icon from '@hugeicons/react/ArrowDown01Icon';
import CheckmarkCircle01Icon from '@hugeicons/react/CheckmarkCircle01Icon';
import {
  createContext,
  use,
  useEffect,
  useRef,
  useState,
  type ButtonHTMLAttributes,
  type KeyboardEvent,
  type ReactNode,
  type RefObject,
} from 'react';

/* ─── Context ─── */
interface SelectContextValue {
  value: string;
  onValueChange: (value: string) => void;
  open: boolean;
  setOpen: (open: boolean) => void;
  triggerRef: RefObject<HTMLButtonElement | null>;
  contentRef: RefObject<HTMLDivElement | null>;
}

const SelectContext = createContext<SelectContextValue | null>(null);

function useSelectContext() {
  const ctx = use(SelectContext);
  if (!ctx) throw new Error('Select components must be used within <Select>');
  return ctx;
}

/* ─── Root ─── */
interface SelectProps {
  value?: string;
  defaultValue?: string;
  onValueChange?: (value: string) => void;
  children: ReactNode;
  name?: string;
}

function Select({
  value,
  defaultValue = '',
  onValueChange,
  children,
  name,
}: SelectProps) {
  const [internalValue, setInternalValue] = useState(defaultValue);
  const [open, setOpen] = useState(false);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  const selectedValue = value ?? internalValue;

  const handleValueChange = (newValue: string) => {
    if (value === undefined) setInternalValue(newValue);
    onValueChange?.(newValue);
    setOpen(false);
    triggerRef.current?.focus();
  };

  // Click outside handler
  useEffect(() => {
    if (!open) return;
    const handleClickOutside = (e: MouseEvent) => {
      if (
        triggerRef.current &&
        !triggerRef.current.contains(e.target as Node) &&
        contentRef.current &&
        !contentRef.current.contains(e.target as Node)
      ) {
        setOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [open]);

  return (
    <SelectContext.Provider
      value={{
        value: selectedValue,
        onValueChange: handleValueChange,
        open,
        setOpen,
        triggerRef,
        contentRef,
      }}
    >
      <div
        data-slot="select"
        className="relative inline-block w-full text-left"
      >
        {/* Hidden input untuk FormData compatibility */}
        {name ? (
          <input type="hidden" name={name} value={selectedValue} />
        ) : null}
        {children}
      </div>
    </SelectContext.Provider>
  );
}

/* ─── Trigger ─── */
function SelectTrigger({
  className,
  children,
  ...props
}: ButtonHTMLAttributes<HTMLButtonElement>) {
  const { open, setOpen, triggerRef } = useSelectContext();

  const handleKeyDown = (e: KeyboardEvent<HTMLButtonElement>) => {
    if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowDown') {
      e.preventDefault();
      setOpen(true);
    }
  };

  return (
    <button
      ref={triggerRef}
      type="button"
      aria-haspopup="listbox"
      aria-expanded={open}
      onClick={() => setOpen(!open)}
      onKeyDown={handleKeyDown}
      className={cn(
        'border-border-input bg-surface-input text-text-primary flex h-9 w-full items-center justify-between gap-1.5 rounded-sm border px-2.5 py-1.5 text-sm whitespace-nowrap transition-colors outline-none select-none',
        'focus:border-border-strong focus:ring-border-strong focus:ring-1',
        'disabled:cursor-not-allowed disabled:opacity-50',
        className
      )}
      {...props}
    >
      <span className="truncate">{children}</span>
      <ArrowDown01Icon
        size={16}
        className={cn(
          'text-text-tertiary shrink-0 transition-transform duration-200',
          open && 'rotate-180'
        )}
      />
    </button>
  );
}

/* ─── Value ─── */
function SelectValue({ placeholder }: { placeholder?: string }) {
  const { value } = useSelectContext();
  return value ? (
    <>{value}</>
  ) : (
    <span className="text-text-tertiary">{placeholder}</span>
  );
}

/* ─── Content ─── */
function SelectContent({
  className,
  children,
}: {
  className?: string;
  children: ReactNode;
}) {
  const { open, contentRef } = useSelectContext();
  if (!open) return null;

  return (
    <div
      ref={contentRef}
      role="listbox"
      className={cn(
        'border-border-default bg-surface-primary animate-in fade-in-0 zoom-in-95 absolute z-50 mt-1 max-h-60 w-full overflow-auto rounded-sm border p-1 shadow-md duration-100',
        className
      )}
    >
      {children}
    </div>
  );
}

/* ─── Item ─── */
function SelectItem({
  className,
  children,
  value,
  ...props
}: ButtonHTMLAttributes<HTMLButtonElement> & { value: string }) {
  const { value: selectedValue, onValueChange } = useSelectContext();
  const isSelected = selectedValue === value;

  const handleKeyDown = (e: KeyboardEvent<HTMLButtonElement>) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      onValueChange(value);
    }
  };

  return (
    <button
      type="button"
      role="option"
      aria-selected={isSelected}
      tabIndex={0}
      onClick={() => onValueChange(value)}
      onKeyDown={handleKeyDown}
      className={cn(
        'text-text-primary relative flex w-full cursor-pointer items-center gap-2 rounded-sm px-2 py-1.5 text-sm transition-colors outline-none select-none',
        'hover:bg-surface-tertiary focus:bg-surface-tertiary',
        className
      )}
      {...props}
    >
      <span className="flex size-4 shrink-0 items-center justify-center">
        {isSelected ? (
          <CheckmarkCircle01Icon size={14} className="text-accent-burgundy" />
        ) : null}
      </span>
      <span className="truncate">{children}</span>
    </button>
  );
}

export { Select, SelectContent, SelectItem, SelectTrigger, SelectValue };
