"""
utils/transformer.py — Missing Values and Outliers Handling (Post-split)
"""

import pandas as pd

def impute_median(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Isi missing value menggunakan median dari X_train."""
    X_train, X_test = X_train.copy(), X_test.copy()
    for col in cols:
        fill_val = X_train[col].median()
        X_train[col] = X_train[col].fillna(fill_val)
        X_test[col] = X_test[col].fillna(fill_val)
        print(f"[impute_median] '{col}': Imputed using train median = {fill_val:.4f}")
    return X_train, X_test


def impute_mode(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Isi missing value menggunakan mode dari X_train."""
    X_train, X_test = X_train.copy(), X_test.copy()
    for col in cols:
        fill_val = X_train[col].mode()[0]
        X_train[col] = X_train[col].fillna(fill_val)
        X_test[col] = X_test[col].fillna(fill_val)
        print(f"[impute_mode] '{col}': Imputed using train mode = {fill_val}")
    return X_train, X_test

def remove_outliers_iqr(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Hapus baris outlier berdasarkan batas IQR dari X_train."""
    X_train, X_test = X_train.copy(), X_test.copy()
    before_train, before_test = len(X_train), len(X_test)
    
    for col in cols:
        q1, q3 = X_train[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        X_train = X_train[(X_train[col] >= lower_bound) & (X_train[col] <= upper_bound)]
        X_test = X_test[(X_test[col] >= lower_bound) & (X_test[col] <= upper_bound)]
        
    print(f"[remove_outliers_iqr] Train row reduction: {before_train} → {len(X_train)}")
    print(f"[remove_outliers_iqr] Test row reduction: {before_test} → {len(X_test)}")
    return X_train.reset_index(drop=True), X_test.reset_index(drop=True)


def cap_outliers(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Winsorizing: Clip nilai ekstrem berdasarkan batas IQR (Q1-1.5*IQR, Q3+1.5*IQR) dari X_train."""
    X_train, X_test = X_train.copy(), X_test.copy()
    for col in cols:
        Q1 = X_train[col].quantile(0.25)
        Q3 = X_train[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        X_train[col] = X_train[col].clip(lower=lower, upper=upper)
        X_test[col] = X_test[col].clip(lower=lower, upper=upper)
        print(f"[cap_outliers] '{col}': Clipped to IQR bounds [{lower:.4f}, {upper:.4f}]")
    return X_train, X_test


