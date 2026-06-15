import { Badge } from '@/components/shared/Badge';
import {
  Card,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/shared/Card';
import { categories } from '@/data/categories';
import { projects } from '@/data/projects';
import { cn } from '@/lib/cn';
import { formatMetric } from '@/lib/formatters';
import { Link } from 'react-router-dom';

export const WelcomeScreen = () => {
  return (
    <div className="animate-fade-in mx-auto max-w-5xl">
      <header className="mb-12">
        <nav className="text-text-tertiary mb-4 flex items-center gap-2 font-mono text-[10px] tracking-widest uppercase">
          <span className="text-text-primary font-medium">Home</span>
          <span>/</span>
          <span>Welcome</span>
        </nav>
        <h1 className="text-text-primary font-serif text-3xl font-semibold md:text-4xl">
          ML Classic Showcase
        </h1>
        <p className="text-text-secondary mt-4 max-w-3xl font-sans leading-relaxed">
          A portfolio of classic machine learning problems, demonstrated through
          interactive web applications. Each project showcases a complete
          end-to-end pipeline from data preprocessing to model deployment.
        </p>
      </header>

      <div className="grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4">
        {projects.map((project) => {
          const category = categories[project.category];

          return (
            <Link
              key={project.id}
              to={`/project/${project.id}`}
              className="group flex h-full flex-col outline-none"
            >
              <Card className="hover:border-border-strong hover:bg-surface-tertiary focus:border-border-strong focus:ring-border-strong h-full overflow-hidden p-0 transition-colors focus:ring-1 sm:p-0 md:p-0 lg:p-0">
                {project.imageUrl ? (
                  <div className="border-border-default bg-surface-tertiary aspect-4/3 w-full shrink-0 overflow-hidden border-b sm:aspect-3/2">
                    <img
                      src={project.imageUrl}
                      alt={project.name}
                      className="h-full w-full object-cover"
                    />
                  </div>
                ) : null}
                <CardHeader className="flex flex-1 flex-col gap-0 p-4">
                  <Badge
                    variant="category"
                    className={cn(
                      category.textColor,
                      'mb-2 self-start text-[8px] lg:mb-3 lg:text-xs'
                    )}
                  >
                    {category.label}
                  </Badge>
                  <CardTitle
                    className={cn(
                      'mb-2 text-sm leading-snug sm:text-base lg:text-xl',
                      'group-hover:text-accent-burgundy transition-colors'
                    )}
                  >
                    {project.name}
                  </CardTitle>
                  <CardDescription
                    className={cn(
                      'mb-4 line-clamp-2 hidden flex-1 text-xs sm:block lg:line-clamp-3 lg:text-sm'
                    )}
                  >
                    {project.description}
                  </CardDescription>
                  <div className="flex-1 sm:hidden" />
                </CardHeader>
                <CardFooter
                  className={cn(
                    'mt-auto flex-col items-stretch gap-1.5 border-t bg-transparent',
                    'px-4 py-3 font-mono text-[8px] tracking-widest uppercase',
                    'sm:px-5 sm:py-3 sm:text-[9px]',
                    'md:px-6 md:py-3',
                    'lg:text-[10px]',
                    'xl:flex-row xl:items-center xl:gap-2'
                  )}
                >
                  <span className="w-full truncate xl:w-auto xl:max-w-[55%]">
                    {project.bestModel}
                  </span>
                  <span className="text-text-primary whitespace-nowrap">
                    {formatMetric(project.metricValue, project.metricName)}{' '}
                    {project.metricName}
                  </span>
                </CardFooter>
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
};
