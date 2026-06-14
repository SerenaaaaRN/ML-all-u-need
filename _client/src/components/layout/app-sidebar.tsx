import { useSidebar } from '@/hooks/useSidebar';
import SidebarLeftIcon from '@hugeicons/react/SidebarLeftIcon';
import SidebarRightIcon from '@hugeicons/react/SidebarRightIcon';
import { NavGroup } from './nav-group';
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuItem,
  SidebarSeparator,
  SidebarTrigger,
} from './sidebar';
import { sidebarData } from './sidebar-data';

export function AppSidebar() {
  const { state } = useSidebar();
  const isCollapsed = state === 'collapsed';

  return (
    <Sidebar collapsible="icon">
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <div className="flex items-center justify-between gap-3 p-2">
              {!isCollapsed && (
                <span className="text-text-primary font-serif text-lg font-semibold">
                  ML Showcase
                </span>
              )}
              <SidebarTrigger>
                {isCollapsed ? (
                  <SidebarRightIcon size={20} />
                ) : (
                  <SidebarLeftIcon size={20} />
                )}
              </SidebarTrigger>
            </div>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>

      <SidebarContent>
        {/* Main navigation */}
        {sidebarData.navGroups
          .filter((g) => g.id === 'main')
          .map((group) => (
            <NavGroup key={group.id} group={group} />
          ))}

        <SidebarSeparator />

        {/* Project groups */}
          {sidebarData.navGroups
            .filter((g) => g.id !== 'main')
            .map((group) => (
              <NavGroup key={group.id} group={group} />
            ))}
      </SidebarContent>

      <SidebarFooter>
        <div className="text-text-tertiary px-2 font-mono text-[10px] tracking-wider uppercase">
          {isCollapsed ? (
            <span className="block text-center">v1</span>
          ) : (
            <span>ML Gallery &middot; v1.0.0</span>
          )}
        </div>
      </SidebarFooter>
    </Sidebar>
  );
}
