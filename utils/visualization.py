"""
visualization.py — Data Visualization utilities
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set_theme(style="whitegrid", palette="muted")

def plot_distributions(df: pd.DataFrame,
                           cols: list = None
                           ):
    """
    Grid subplot untuk banyak kolom sekaligus menggunakan Seaborn:
    - 'numeric'     : Mengambil semua kolom angka & membuat sns.histplot
    - 'categorical' : Mengambil semua kolom kategori & membuat sns.countplot
    """
    target_cols = cols or df.columns.tolist()

    if not target_cols:
        print("[plot_all_distributions] Tidak ada kolom yang ditemukan.")
        return
    
    sample_col = target_cols[0]
    is_numeric = np.issubdtype(df[sample_col].dtype, np.number)
    
    n_cols = 3
    n_rows = int(np.ceil(len(target_cols) / n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 4 * n_rows))
    axes = np.array(axes).flatten()

    for i, col in enumerate(target_cols):
        if col not in df.columns:
            print(f"[Warning] Kolom '{col}' tidak ditemukan di DataFrame. Dilewati.")
            continue

        if is_numeric:
            sns.histplot(data=df, x=col, color="steelblue", kde=True, 
                         alpha=0.6, edgecolor="white", linewidth=1.2, ax=axes[i])
            
            mean_val = df[col].mean()
            median_val = df[col].median()
            
            axes[i].axvline(mean_val, color="crimson", linestyle="--", linewidth=1.5, label=f"Mean: {mean_val:.2f}")
            axes[i].axvline(median_val, color="darkorange", linestyle=":", linewidth=2, label=f"Median: {median_val:.2f}")
            
            axes[i].legend(fontsize=8, loc="upper right")
            axes[i].set_ylabel("Frekuensi")
            
        else:
            order = df[col].value_counts().index
            sns.countplot(data=df, x=col, order=order, color="seagreen", ax=axes[i])
            axes[i].tick_params(axis='x', rotation=30)
            axes[i].set_ylabel("Jumlah")

        axes[i].set_title(col, fontsize=11, fontweight='bold')
    
    # Handle axes kosong jika jumlah kolom tidak pas kelipatan 3
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    main_title = "Analisis Distribusi Numerik" if is_numeric else "Analisis Distribusi Kategorikal"
    plt.suptitle(main_title, fontsize=15, y=1.02, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_boxplot(df: pd.DataFrame,
                 cols: str,
                 orient: str = "v",
                 figsize: tuple = (8, 4)):
    """
    Boxplot untuk visualisasi outlier banyak kolom.
    orient: 'v' (vertical) | 'h' (horizontal).
    """

    if cols is None:
        target_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    else:
        target_cols = [c for c in cols if c in df.columns and np.issubdtype(df[c].dtype, np.number)]
                       
    if not target_cols:
        print("[plot_boxplot] Tidak ada kolom numerik yang valid untuk ditampilkan.")
        return
    
    n_cols = 3
    n_rows = int(np.ceil(len(target_cols) / n_cols))
    figsize = (5 * n_cols, 5 * n_rows) if orient == "v" else (6 * n_cols, 3.5 * n_rows)
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = np.array(axes).flatten()
    
    for i, col in enumerate(target_cols):
        if orient == "h":
            sns.boxplot(data=df, x=col, ax=axes[i], 
                        flierprops={"markerfacecolor": "crimson", "marker": "o", "markersize": 5})
            axes[i].set_xlabel(col, fontsize=10)
        else:
            sns.boxplot(data=df, y=col, ax=axes[i],
                        flierprops={"markerfacecolor": "crimson", "marker": "o", "markersize": 5})
            axes[i].set_ylabel(col, fontsize=10)
            
        axes[i].set_title(f"Boxplot — {col}", fontsize=11, fontweight='bold')
        axes[i].grid(axis='both', linestyle=':', alpha=0.6)

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.suptitle("Analisis Outlier Menggunakan Boxplot", fontsize=15, y=1.02, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_class_balance(df: pd.DataFrame,
                       target: str,
                       figsize: tuple = (10, 5)):
    """
    Bar chart distribusi target (count + persentase)
    """
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

    df_sorted = df[target].value_counts().sort_index()
    counts_idx = df_sorted.index
    counts_vals = df_sorted.values
    pcts_vals = (df_sorted / df_sorted.sum()) * 100

    max_count = max(counts_vals)

    sns.barplot(x=counts_idx, y=counts_vals,
                hue=counts_idx, palette="viridis", legend=False, ax=ax1)
    ax1.set_title(f"Count — {target}", fontsize=12, pad=10)
    ax1.set_xlabel(target, fontsize=10)
    ax1.set_ylabel("Count", fontsize=10)
    ax1.set_ylim(0, max_count * 1.15) 
    
    for p in ax1.patches:
        height = p.get_height()
        if height > 0:
            ax1.annotate(f'{int(height)}',
                         (p.get_x() + p.get_width() / 2., height),
                         ha='center', va='bottom', 
                         xytext=(0, 5), textcoords='offset points', fontsize=10)

    sns.barplot(x=counts_idx, y=pcts_vals,
                hue=counts_idx, palette="viridis", legend=False, ax=ax2)
    ax2.set_title(f"Percentage — {target}", fontsize=12, pad=10)
    ax2.set_xlabel(target, fontsize=10)
    ax2.set_ylabel("%", fontsize=10)
    ax2.set_ylim(0, max(pcts_vals) * 1.15)

    for p in ax2.patches:
        height = p.get_height()
        if height > 0:
            ax2.annotate(f'{height:.1f}%',
                         (p.get_x() + p.get_width() / 2., height),
                         ha='center', va='bottom', 
                         xytext=(0, 5), textcoords='offset points', fontsize=10)

    plt.suptitle(f"Class Balance — '{target}'", fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()


