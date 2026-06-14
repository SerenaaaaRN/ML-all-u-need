export interface Category {
  label: string;
  color: string;
  textColor: string;
}

export const categories: Record<string, Category> = {
  'binary-classification': {
    label: 'Binary Classification',
    color: 'bg-tag-classification',
    textColor: 'text-tag-classification',
  },
  'multiclass-classification': {
    label: 'Multiclass Classification',
    color: 'bg-tag-multiclass',
    textColor: 'text-tag-multiclass',
  },
  regression: {
    label: 'Regression',
    color: 'bg-tag-regression',
    textColor: 'text-tag-regression',
  },
};
