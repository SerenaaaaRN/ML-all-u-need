import { projects } from '@/data/projects';
import Brain01Icon from '@hugeicons/react/Brain01Icon';
import ChartHistogramIcon from '@hugeicons/react/ChartHistogramIcon';
import Home01Icon from '@hugeicons/react/Home01Icon';
import Layers01Icon from '@hugeicons/react/Layers01Icon';

export type NavItem = {
  title: string;
  url: string;
  icon?: typeof Home01Icon;
};

export type NavGroup = {
  id: string;
  title: string;
  icon?: typeof Home01Icon;
  items: NavItem[];
};

const { classificationProjects, regressionProjects, unsupervisedProjects } =
  (() => {
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

export const sidebarData = {
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
      items: classificationProjects.map((p) => ({
        title: p.name,
        url: `/project/${p.id}`,
      })),
    },
    {
      id: 'regression',
      title: 'Regression',
      icon: Brain01Icon,
      items: regressionProjects.map((p) => ({
        title: p.name,
        url: `/project/${p.id}`,
      })),
    },
    {
      id: 'unsupervised',
      title: 'Unsupervised',
      icon: ChartHistogramIcon,
      items: unsupervisedProjects.map((p) => ({
        title: p.name,
        url: `/project/${p.id}`,
      })),
    },
  ],
};
