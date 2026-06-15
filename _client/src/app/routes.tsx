import { AppShell } from '@/components/layout/AppShell';
import { ProjectPage } from '@/components/ProjectPage';
import { WelcomeScreen } from '@/components/WelcomeScreen';
import { createBrowserRouter } from 'react-router-dom';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <AppShell />,
    children: [
      {
        index: true,
        element: <WelcomeScreen />,
      },
      {
        path: 'project/:projectId',
        element: <ProjectPage />,
      },
    ],
  },
]);
