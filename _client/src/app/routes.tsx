import { AppShell } from '@/components/layout/AppShell';
import { Playground } from '@/components/playground/Playground';
import { WelcomeScreen } from '@/components/welcome/WelcomeScreen';
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
        element: <Playground />,
      },
    ],
  },
]);
