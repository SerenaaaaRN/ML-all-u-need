import { SidebarInset } from '@/components/layout/Sidebar';
import { SidebarProvider, useSidebar } from '@/hooks/useSidebar';
import { AppSidebar } from '@/components/layout/AppSidebar';
import Menu01Icon from '@hugeicons/react/Menu01Icon';
import { Link, Outlet } from 'react-router-dom';

const logoLink = (
  <Link
    to="/"
    className="text-text-primary ml-5 font-serif text-xl font-semibold outline-none"
  >
    ML Showcase
  </Link>
);

function MobileHeader() {
  const { setOpenMobile } = useSidebar();

  return (
    <header className="border-border-default bg-surface-primary flex h-20 shrink-0 items-center border-b px-6 md:hidden">
      <button
        onClick={() => setOpenMobile(true)}
        className="text-text-secondary hover:text-text-primary outline-none"
        aria-label="Open menu"
      >
        <Menu01Icon size={26} />
      </button>
      {logoLink}
    </header>
  );
}

export const AppShell = () => {
  return (
    <SidebarProvider>
      <div className="bg-surface-primary flex h-screen overflow-hidden">
        <AppSidebar />

        <SidebarInset>
          <MobileHeader />

          <div className="p-6 md:p-8 lg:p-12">
            <Outlet />
          </div>
        </SidebarInset>
      </div>
    </SidebarProvider>
  );
};
