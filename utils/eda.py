import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def summary_stats(df: pd.DataFrame):
    """
    Print dan return ringkasan statistik dasar dataframe.

    Returns
    -------
    dict berisi shape, dtypes, describe
    """
    print("=" * 60)
    print(f"SHAPE        : {df.shape[0]} rows × {df.shape[1]} columns")
    print("=" * 60)

    print("\n── DTYPES ──")
    dtype_df = pd.DataFrame({
        "dtype":   df.dtypes,
        "nunique": df.nunique(),
        "sample":  df.iloc[0] if len(df) > 0 else pd.Series(dtype=object),
    })
    print(dtype_df.to_string())


def missing_report(df: pd.DataFrame):
    """
    Laporan persentase missing value per kolom.

    Returns
    -------
    pd.DataFrame diurutkan dari % missing tertinggi
    """
    total   = df.isnull().sum()
    pct     = total / len(df) * 100
    report  = pd.DataFrame({
        "missing_count": total,
        "missing_pct":   pct.round(2),
        "dtype":         df.dtypes,
    }).sort_values("missing_pct", ascending=False)

    report = report[report["missing_count"] > 0]

    print("=" * 50)
    print(f"MISSING VALUE REPORT  (total kolom: {df.shape[1]})")
    print("=" * 50)
    if report.empty:
        print("✓ Tidak ada missing values.")
    else:
        print(report.to_string())

def correlation_matrix(df: pd.DataFrame,
                       method: str = "pearson",
                       figsize: tuple = (12, 9)):
    """
    Heatmap korelasi antar kolom numerik.

    Parameters
    ----------
    method  : 'pearson' | 'spearman' | 'kendall'
    figsize : ukuran figure

    Returns
    -------
    pd.DataFrame correlation matrix
    """
    num_df = df.select_dtypes(include=[np.number])
    corr   = num_df.corr(method=method)

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".2f",
        cmap="coolwarm", center=0,
        linewidths=0.5, ax=ax,
        annot_kws={"size": 8},
    )
    ax.set_title(f"Correlation Matrix ({method.capitalize()})", fontsize=13)
    plt.tight_layout()
    plt.show()


def class_balance(df: pd.DataFrame, target: str):
    """
    Cek distribusi / imbalance pada kolom target.

    Returns
    -------
    pd.DataFrame dengan count dan persentase per kelas
    """
    counts = df[target].value_counts()
    pct    = df[target].value_counts(normalize=True) * 100
    report = pd.DataFrame({"count": counts, "pct": pct.round(2)})

    print("=" * 40)
    print(f"CLASS BALANCE — '{target}'")
    print("=" * 40)
    print(report.to_string())

    ratio = counts.max() / counts.min() if counts.min() > 0 else float("inf")
    print(f"\nImbalance ratio (max/min): {ratio:.2f}x")
    if ratio > 3:
        print("⚠  Dataset tampak imbalanced (ratio > 3).")
    else:
        print("✓  Dataset relatif balanced.")


def outlier_report(df: pd.DataFrame,
                   method: str = "iqr",
                   z_thresh: float = 3.0):
    """
    Flag kolom numerik yang mengandung outlier.

    Parameters
    ----------
    method   : 'iqr' atau 'zscore'
    z_thresh : threshold z-score (default 3.0)

    Returns
    -------
    pd.DataFrame ringkasan outlier per kolom
    """
    num_cols = df.select_dtypes(include=[np.number]).columns
    records  = []

    for col in num_cols:
        series = df[col].dropna()

        if method == "iqr":
            q1, q3 = series.quantile([0.25, 0.75])
            iqr    = q3 - q1
            lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
            n_out  = ((series < lower) | (series > upper)).sum()
        else:  # zscore
            z      = np.abs(stats.zscore(series))
            n_out  = (z > z_thresh).sum()
            lower = upper = None

        records.append({
            "column":        col,
            "n_outliers":    n_out,
            "pct_outliers":  round(n_out / len(series) * 100, 2),
            "has_outlier":   n_out > 0,
            "lower_bound":   round(lower, 4) if lower is not None else None,
            "upper_bound":   round(upper, 4) if upper is not None else None,
        })

    report = pd.DataFrame(records).sort_values("n_outliers", ascending=False)

    print("=" * 55)
    print(f"OUTLIER REPORT  (method={method})")
    print("=" * 55)
    print(report[report["has_outlier"]].to_string(index=False))
    print(f"\nKolom dengan outlier: "
          f"{report['has_outlier'].sum()} / {len(report)}")
