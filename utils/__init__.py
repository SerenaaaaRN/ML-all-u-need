"""
DS-all-u-need — Utility functions for tabular data science pipelines.
"""

from .eda import (
    summary_stats,
    missing_report,
    correlation_matrix,
    class_balance,
    outlier_report,
)

from .cleaning import (
    drop_duplicates,
    fix_dtypes,
    handle_whitespace,
    drop_constant_columns,
)

from .transformer import (
    impute_median,
    impute_mode,
    remove_outliers_iqr,
    cap_outliers,
)

from .encoding import (
    one_hot_encode,
    label_encode,
    target_encode,
)

from .scaling import (
    standardize,
    robust_scale,
    log_transform,
)

from .visualization import (
    plot_distributions,
    plot_boxplot,
    plot_class_balance,
)

from .modeling import (
    compare_models,
    save_competition_result,
)

__all__ = [
    "summary_stats", "missing_report", "correlation_matrix", "class_balance", "outlier_report",
    "drop_duplicates", "fix_dtypes", "handle_whitespace", "drop_constant_columns",
    "impute_median", "impute_mode", "remove_outliers_iqr", "cap_outliers",
    "one_hot_encode", "label_encode", "target_encode",
    "standardize", "robust_scale", "log_transform",
    "plot_distributions", "plot_boxplot", "plot_class_balance",
    "compare_models", "save_competition_result",
]