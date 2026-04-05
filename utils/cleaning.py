"""
utils/cleaning.py — Data Cleaning utilities (Pre-split)
"""

import pandas as pd

def drop_duplicates(df: pd.DataFrame,
                    subset: list = None,
                    keep: str = "first") -> pd.DataFrame:
    """Hapus baris duplikat."""
    before = len(df)
    df = df.drop_duplicates(subset=subset, keep=keep).reset_index(drop=True)
    dropped = before - len(df)
    print(f"[drop_duplicates] Removed {dropped} duplicate rows ({before} -> {len(df)})")
    return df

def fix_dtypes(df: pd.DataFrame, exclude_cols: list = None) -> pd.DataFrame:
    """
    Auto-convert dtypes secara cerdas untuk tipe numerik dan kategori.
    Bisa mengecualikan kolom tertentu (misal: kolom tanggal).
    """
    df = df.copy()
    if exclude_cols is None:
        exclude_cols = []
        
    for col in df.columns:
        if col in exclude_cols:
            continue

        converted = pd.to_numeric(df[col], errors="coerce")
        if converted.notnull().sum() / len(df) > 0.9:
            if df[col].dtype == object:
                df[col] = converted
                print(f"[fix_dtypes] '{col}': object → numeric")
                continue

        if df[col].dtype == object and df[col].nunique() <= 20:
            df[col] = df[col].astype("category")
            print(f"[fix_dtypes] '{col}': object → category ({df[col].nunique()} unique values)")

    return df

def handle_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace dan normalisasi multiple spaces pada kolom objek."""
    df = df.copy()
    str_cols = df.select_dtypes(include=["object"]).columns
    for col in str_cols:
        df[col] = df[col].str.strip().str.replace(r"\s+", " ", regex=True)
    print(f"[handle_whitespace] Stripped whitespace on {len(str_cols)} columns")
    return df


def drop_constant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop kolom dengan variansi 0 (hanya memiliki 1 nilai unik)."""
    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    print(f"[drop_constant_columns] Dropping {len(constant_cols)} columns: {constant_cols}")
    return df.drop(columns=constant_cols)

