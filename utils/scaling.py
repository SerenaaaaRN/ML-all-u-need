"""
utils/scaling.py — Feature Scaling & Transformation utilities (Post-split)
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler

def standardize(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Standarisasi fitur (Z-score Normalization) menggunakan parameter X_train."""
    X_train, X_test = X_train.copy(), X_test.copy()
    scaler = StandardScaler()
    X_train[cols] = scaler.fit_transform(X_train[cols])
    X_test[cols] = scaler.transform(X_test[cols])
    print(f"[standardize] Standardized {len(cols)} columns.")
    return X_train, X_test, scaler


def robust_scale(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Robust Scaling (Median & IQR) berbasis parameter X_train."""
    X_train, X_test = X_train.copy(), X_test.copy()
    scaler = RobustScaler()
    X_train[cols] = scaler.fit_transform(X_train[cols])
    X_test[cols] = scaler.transform(X_test[cols])
    print(f"[robust_scale] Robust-scaled {len(cols)} columns.")
    return X_train, X_test, scaler


def log_transform(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list, shift: float = 1.0) -> tuple:
    """Transformasi Log untuk mereduksi kecondongan distribusi kanan (Right-skewed)."""
    X_train, X_test = X_train.copy(), X_test.copy()
    for col in cols:
        min_val = X_train[col].min()
        s = shift
        if min_val <= 0:
            s = abs(min_val) + shift
        X_train[col] = np.log(X_train[col] + s)
        X_test[col] = np.log(X_test[col] + s)
        print(f"[log_transform] Applied log(x + {s:.4f}) to '{col}'")
    return X_train, X_test

