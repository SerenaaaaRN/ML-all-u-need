"""
utils/encoding.py — Categorical Encoding utilities (Post-split)
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def one_hot_encode(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list, 
                   drop_first: bool = False, prefix_sep: str = "_") -> tuple:
    """One-Hot Encoding aman menggunakan reindexing dummy columns milik X_train."""
    X_train_enc = pd.get_dummies(X_train, columns=cols, drop_first=drop_first, prefix_sep=prefix_sep, dtype=int)
    X_test_enc = pd.get_dummies(X_test, columns=cols, drop_first=drop_first, prefix_sep=prefix_sep, dtype=int)
    
    X_test_enc = X_test_enc.reindex(columns=X_train_enc.columns, fill_value=0)
    
    print(f"[one_hot_encode] Encoded {len(cols)} columns.")
    return X_train_enc, X_test_enc


def label_encode(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list) -> tuple:
    """Label encoding dengan penanganan kategori baru di X_test."""
    X_train, X_test = X_train.copy(), X_test.copy()
    encoders = {}
    
    for col in cols:
        le = LabelEncoder()
        X_train[col] = le.fit_transform(X_train[col].astype(str))
        
        # Mengatasi nilai baru di X_test yang tidak ada di X_train
        X_test[col] = X_test[col].astype(str).map(lambda s: le.transform([s])[0] if s in le.classes_ else -1)
        encoders[col] = le
        print(f"[label_encode] '{col}' successfully encoded.")
        
    return X_train, X_test, encoders


def target_encode(X_train: pd.DataFrame, X_test: pd.DataFrame, cols: list, 
                  y_train: pd.Series, smoothing: float = 1.0) -> tuple:
    """Target Encoding menggunakan statistik y_train dengan formula smoothing."""
    X_train, X_test = X_train.copy(), X_test.copy()
    global_mean = y_train.mean()
    
    # Gabung sementara dengan target untuk menghitung statistik grup
    temp_train = X_train.copy()
    temp_train["_target"] = y_train

    for col in cols:
        stats = temp_train.groupby(col)["_target"].agg(["mean", "count"])
        smoothed = (stats["count"] * stats["mean"] + smoothing * global_mean) / (stats["count"] + smoothing)
        
        X_train[col] = X_train[col].map(smoothed).fillna(global_mean)
        X_test[col] = X_test[col].map(smoothed).fillna(global_mean)
        print(f"[target_encode] '{col}' encoded safely using train targets.")

    return X_train, X_test

