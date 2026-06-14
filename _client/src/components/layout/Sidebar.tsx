import { useSidebar } from '@/hooks/useSidebar';
import { cn } from '@/lib/cn';
import {
  cloneElement,
  isValidElement,
  type ComponentProps,
  type ReactElement,
} from 'react';

function Slot({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) {
  if (isValidElement(children)) {
    const childProps = children.props as Record<string, unknown>;
    return cloneElement(children as ReactElement<Record<string, unknown>>, {
      ...childProps,
      className: cn(childProps.className as string | undefined, className),
    });
  }
  return children;
}

/* ─── SIDEBAR ─── */

interface SidebarProps extends ComponentProps<'div'> {
  side?: 'left' | 'right';
  collapsible?: 'offcanvas' | 'icon' | 'none';
}

export function Sidebar({
  side = 'left',
  collapsible = 'icon',
  className,
  children,
  ...props
}: SidebarProps) {
  const { isMobile, state, openMobile, setOpenMobile } = useSidebar();

  if (collapsible === 'none') {
    return (
      <div
        data-slot="sidebar"
        className={cn(
          'w-sidebar bg-surface-secondary text-text-primary flex h-full flex-col',
          className
        )}
        {...props}
      >
        {children}
      </div>
    );
  }

  if (isMobile) {
    if (!openMobile) return null;
    return (
      <>
        <div
          className="bg-text-primary/50 fixed inset-0 z-50 backdrop-blur-sm md:hidden"
          onClick={() => setOpenMobile(false)}
          aria-hidden="true"
        />
        <div
          data-slot="sidebar"
          data-mobile="true"
          className={cn(
            'bg-surface-primary animate-fade-in-right fixed inset-y-0 z-50 flex w-[--width-sidebar-mobile] flex-col overflow-y-auto shadow-xl md:hidden',
            side === 'left' ? 'left-0' : 'right-0',
            className
          )}
          {...props}
        >
          <button
            onClick={() => setOpenMobile(false)}
            className={cn(
              'text-text-tertiary hover:text-text-primary absolute top-4 z-10 transition-colors',
              side === 'left' ? 'right-4' : 'left-4'
            )}
            aria-label="Close sidebar"
          >
            <span className="text-xl">&times;</span>
          </button>
          {children}
        </div>
      </>
    );
  }

  return (
    <div
      className="group peer text-text-primary hidden md:block"
      data-state={state}
      data-collapsible={state === 'collapsed' ? collapsible : ''}
      data-side={side}
      data-slot="sidebar"
    >
      {/* Gap element that adjusts main content margin when sidebar collapses/expands */}
      <div
        data-slot="sidebar-gap"
        className={cn(
          'w-sidebar relative bg-transparent transition-[width] duration-200 ease-linear',
          'group-data-[collapsible=offcanvas]:w-0',
          'group-data-[side=right]:rotate-180',
          'group-data-[collapsible=icon]:w-sidebar-icon'
        )}
      />
      <div
        data-slot="sidebar-container"
        className={cn(
          'w-sidebar fixed inset-y-0 z-10 hidden h-svh transition-[inset-inline,width] duration-200 ease-linear md:flex',
          side === 'left'
            ? 'group-data-[collapsible=offcanvas]:-start-sidebar start-0'
            : 'group-data-[collapsible=offcanvas]:-end-sidebar end-0',
          'group-data-[collapsible=icon]:w-sidebar-icon group-data-[side=left]:border-e group-data-[side=right]:border-s',
          className
        )}
        {...props}
      >
        <div
          data-sidebar="sidebar"
          data-slot="sidebar-inner"
          className="bg-surface-secondary flex h-full w-full flex-col"
        >
          {children}
        </div>
      </div>

      {/* SidebarRail — auto-rendered for icon/offcanvas collapsible */}
      {<SidebarRail />}
    </div>
  );
}

/* ─── COMPOUND COMPONENTS ─── */

export function SidebarHeader({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-header"
      data-sidebar="header"
      className={cn('flex flex-col gap-2 p-2', className)}
      {...props}
    />
  );
}

export function SidebarContent({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-content"
      data-sidebar="content"
      className={cn(
        'flex min-h-0 flex-1 flex-col gap-1 overflow-hidden group-data-[collapsible=icon]:overflow-hidden',
        className
      )}
      {...props}
    />
  );
}

export function SidebarFooter({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-footer"
      data-sidebar="footer"
      className={cn('flex flex-col gap-2 p-2', className)}
      {...props}
    />
  );
}

export function SidebarSeparator({
  className,
  ...props
}: ComponentProps<'hr'>) {
  return (
    <hr
      data-slot="sidebar-separator"
      data-sidebar="separator"
      className={cn('border-border-default mx-2 w-auto border-t', className)}
      {...props}
    />
  );
}

export function SidebarGroup({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-group"
      data-sidebar="group"
      className={cn(
        'relative flex w-full min-w-0 flex-col px-2 py-1',
        className
      )}
      {...props}
    />
  );
}

export function SidebarGroupLabel({
  className,
  ...props
}: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-group-label"
      data-sidebar="group-label"
      className={cn(
        'text-text-secondary flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium outline-hidden transition-[margin,opacity] duration-200 ease-linear [&>svg]:size-4 [&>svg]:shrink-0',
        'group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0',
        className
      )}
      {...props}
    />
  );
}

export function SidebarGroupContent({
  className,
  ...props
}: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-group-content"
      data-sidebar="group-content"
      className={cn('w-full text-sm', className)}
      {...props}
    />
  );
}

export function SidebarMenu({ className, ...props }: ComponentProps<'ul'>) {
  return (
    <ul
      data-slot="sidebar-menu"
      data-sidebar="menu"
      className={cn('flex w-full min-w-0 flex-col gap-1', className)}
      {...props}
    />
  );
}

export function SidebarMenuItem({ className, ...props }: ComponentProps<'li'>) {
  return (
    <li
      data-slot="sidebar-menu-item"
      data-sidebar="menu-item"
      className={cn('group/menu-item relative', className)}
      {...props}
    />
  );
}

export function SidebarMenuButton({
  asChild = false,
  variant = 'main',
  size = 'md',
  isActive = false,
  tooltip,
  className,
  children,
  ...props
}: ComponentProps<'button'> & {
  asChild?: boolean;
  variant?: 'main' | 'sub';
  size?: 'sm' | 'md';
  isActive?: boolean;
  tooltip?: string;
}) {
  const Comp = asChild ? Slot : 'button';
  const { isMobile, state } = useSidebar();

  const isCollapsed = state === 'collapsed';

  const button = (
    <Comp
      data-slot="sidebar-menu-button"
      data-sidebar="menu-button"
      data-active={isActive}
      className={cn(
        // Base
        'hover:bg-surface-tertiary hover:text-text-primary active:bg-surface-tertiary active:text-text-primary flex w-full items-center gap-2 overflow-hidden rounded-md px-2 outline-hidden focus-visible:ring-2 disabled:pointer-events-none disabled:opacity-50',
        'data-[active=true]:bg-surface-tertiary data-[active=true]:text-text-primary data-[active=true]:font-medium',
        '[&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0',

        // Variant: main
        variant === 'main' &&
          'peer/menu-button p-2 text-start text-sm transition-[width,height,padding] group-data-[collapsible=icon]:size-8! group-data-[collapsible=icon]:p-2!',

        // Variant: sub
        variant === 'sub' &&
          'text-text-secondary h-7 -translate-x-px group-data-[collapsible=icon]:hidden' +
            (size === 'sm' ? ' text-xs' : ' text-sm'),

        className
      )}
      {...props}
    >
      {children}
    </Comp>
  );

  if (variant === 'sub' || !tooltip) return button;

  return (
    <div className="relative">
      {button}
      <div
        className={cn(
          'bg-text-primary text-text-inverse pointer-events-none absolute start-full top-1/2 z-50 -translate-y-1/2 rounded-md px-2 py-1 text-xs opacity-0 shadow-sm transition-opacity',
          'group-data-[collapsible=icon]:ms-2 group-data-[collapsible=icon]:group-hover:opacity-100',
          !isCollapsed || isMobile ? 'hidden' : ''
        )}
        role="tooltip"
      >
        {tooltip}
      </div>
    </div>
  );
}

export function SidebarMenuSub({ className, ...props }: ComponentProps<'ul'>) {
  return (
    <ul
      data-slot="sidebar-menu-sub"
      data-sidebar="menu-sub"
      className={cn(
        'border-border-default mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-s px-2.5 py-0.5',
        'group-data-[collapsible=icon]:hidden',
        className
      )}
      {...props}
    />
  );
}

export function SidebarRail({ className, ...props }: ComponentProps<'button'>) {
  const { toggleSidebar } = useSidebar();

  return (
    <button
      data-sidebar="rail"
      data-slot="sidebar-rail"
      aria-label="Toggle Sidebar"
      tabIndex={-1}
      onClick={toggleSidebar}
      title="Toggle Sidebar"
      className={cn(
        'hover:after:bg-border-strong absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear group-data-[side=left]:-end-4 group-data-[side=right]:start-0 after:absolute after:inset-y-0 after:start-1/2 after:w-0.5 sm:flex',
        'group-data-[side=left]:cursor-w-resize group-data-[side=right]:cursor-e-resize',
        'group-data-[side=left][data-state=collapsed]:cursor-e-resize group-data-[side=right][data-state=collapsed]:cursor-w-resize',
        'hover:group-data-[collapsible=offcanvas]:bg-surface-tertiary group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:start-full',
        'group-data-[side=left][data-collapsible=offcanvas]:-end-2',
        'group-data-[side=right][data-collapsible=offcanvas]:-start-2',
        className
      )}
      {...props}
    />
  );
}

export function SidebarTrigger({
  className,
  onClick,
  children,
  ...props
}: ComponentProps<'button'>) {
  const { toggleSidebar, isMobile } = useSidebar();

  if (isMobile) return null;

  return (
    <button
      data-sidebar="trigger"
      data-slot="sidebar-trigger"
      className={cn(
        'text-text-tertiary hover:text-text-primary transition-colors',
        className
      )}
      onClick={(e) => {
        onClick?.(e);
        toggleSidebar();
      }}
      aria-label="Toggle Sidebar"
      {...props}
    >
      {children}
    </button>
  );
}

export function SidebarInset({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      data-slot="sidebar-inset"
      className={cn(
        'relative flex w-full flex-1 flex-col overflow-y-auto',
        className
      )}
      {...props}
    />
  );
}
