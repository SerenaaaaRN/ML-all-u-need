import { useSidebar } from '@/hooks/useSidebar';
import ArrowDown01Icon from '@hugeicons/react/ArrowDown01Icon';
import ArrowRight01Icon from '@hugeicons/react/ArrowRight01Icon';
import type { FunctionComponent } from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
} from './Sidebar';

type NavItem = {
  title: string;
  url: string;
  icon?: FunctionComponent<{ size?: number }>;
};

type NavGroupType = {
  id: string;
  title: string;
  icon?: FunctionComponent<{ size?: number }>;
  items: NavItem[];
};

interface Props {
  group: NavGroupType;
}

export function NavGroup({ group }: Props) {
  const [open, setOpen] = useState(true);
  const { isMobile, setOpenMobile, state } = useSidebar();
  const isCollapsed = state === 'collapsed';

  if (!group.items.length) {
    return (
      <SidebarGroup>
        {group.title && <SidebarGroupLabel>{group.title}</SidebarGroupLabel>}
        <SidebarGroupContent>
          <SidebarMenu>
            <SidebarMenuItem>
              <SidebarMenuButton
                disabled
                className="text-text-tertiary cursor-default hover:bg-transparent"
              >
                <span className="font-mono text-xs tracking-wider uppercase">
                  {isCollapsed ? '...' : 'Coming Soon'}
                </span>
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    );
  }

  const titleRow = group.title ? (
    <button
      onClick={() => setOpen((v) => !v)}
      className="hover:text-text-primary flex w-full items-center justify-between text-start transition-colors"
    >
      <SidebarGroupLabel>
        <div className="flex items-center gap-2">
          {group.icon && <group.icon size={18} />}
          <span>{group.title}</span>
        </div>
      </SidebarGroupLabel>
      {!isCollapsed ? (
        <div className="text-text-tertiary pr-2">
          {open ? (
            <ArrowDown01Icon size={14} />
          ) : (
            <ArrowRight01Icon size={14} />
          )}
        </div>
      ) : null}
    </button>
  ) : null;

  /* Main items (no group title — e.g. Home) */
  if (!group.title) {
    return (
      <SidebarGroup>
        <SidebarGroupContent>
          <SidebarMenu>
            {group.items.map((item) => (
              <SidebarMenuItem key={item.url}>
                <NavLink
                  to={item.url}
                  end
                  onClick={() => isMobile && setOpenMobile(false)}
                >
                  {({ isActive }) => (
                    <SidebarMenuButton
                      asChild
                      isActive={isActive}
                      tooltip={isCollapsed ? item.title : undefined}
                    >
                      <span className="flex items-center gap-3">
                        {item.icon && <item.icon size={18} />}
                        <span>{item.title}</span>
                      </span>
                    </SidebarMenuButton>
                  )}
                </NavLink>
              </SidebarMenuItem>
            ))}
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    );
  }

  /* Project groups with collapsible sub-menu */
  return (
    <SidebarGroup>
      {titleRow}

      {open ? (
        <SidebarGroupContent>
          <SidebarMenuSub>
            {group.items.map((item) => (
              <li key={item.url} className="group/menu-sub-item relative">
                <NavLink
                  to={item.url}
                  end
                  onClick={() => isMobile && setOpenMobile(false)}
                >
                  {({ isActive }) => (
                    <SidebarMenuButton
                      asChild
                      variant="sub"
                      isActive={isActive}
                    >
                      <span className="truncate text-sm">{item.title}</span>
                    </SidebarMenuButton>
                  )}
                </NavLink>
              </li>
            ))}
          </SidebarMenuSub>
        </SidebarGroupContent>
      ) : null}
    </SidebarGroup>
  );
}
