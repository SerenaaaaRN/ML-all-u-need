import { projects } from '@/data/projects';
import { useSidebar } from '@/hooks/useSidebar';
import Brain01Icon from '@hugeicons/react/Brain01Icon';
import ChartHistogramIcon from '@hugeicons/react/ChartHistogramIcon';
import Home01Icon from '@hugeicons/react/Home01Icon';
import Layers01Icon from '@hugeicons/react/Layers01Icon';
import SidebarLeftIcon from '@hugeicons/react/SidebarLeftIcon';
import SidebarRightIcon from '@hugeicons/react/SidebarRightIcon';
import { NavGroup } from './NavGroup';
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuItem,
  SidebarSeparator,
  SidebarTrigger,
} from './Sidebar';

const categorizedProjects = (() => {
  const c: typeof projects = [];
  const r: typeof projects = [];
  const u: typeof projects = [];
  for (const p of projects) {
    if (p.category.includes('classification')) c.push(p);
    else if (p.category === 'regression') r.push(p);
    else if ((p.category as string) === 'unsupervised') u.push(p);
  }
  return {
    classificationProjects: c,
    regressionProjects: r,
    unsupervisedProjects: u,
  };
})();

const sidebarData = {
  navGroups: [
    {
      id: 'main',
      title: '',
      items: [{ title: 'Home / Welcome', url: '/', icon: Home01Icon }],
    },
    {
      id: 'classification',
      title: 'Classification',
      icon: Layers01Icon,
      items: categorizedProjects.classificationProjects.map((p) => ({
        title: p.name,
        url: `/project/${p.id}`,
      })),
    },
    {
      id: 'regression',
      title: 'Regression',
      icon: Brain01Icon,
      items: categorizedProjects.regressionProjects.map((p) => ({
        title: p.name,
        url: `/project/${p.id}`,
      })),
    },
    {
      id: 'unsupervised',
      title: 'Unsupervised',
      icon: ChartHistogramIcon,
      items: categorizedProjects.unsupervisedProjects.map((p) => ({
        title: p.name,
        url: `/project/${p.id}`,
      })),
    },
  ],
};

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
        {sidebarData.navGroups
          .filter((g) => g.id === 'main')
          .map((group) => (
            <NavGroup key={group.id} group={group} />
          ))}

        <SidebarSeparator />

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
