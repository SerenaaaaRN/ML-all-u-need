"""
utils/modeling.py — Utility training dan evaluasi model (reusable).
"""
import os
import pandas as pd
import numpy as np
from time import time
from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score, 
    r2_score, mean_squared_error, mean_absolute_error
)

def compare_models(models: dict,
                   X_train: pd.DataFrame, y_train: pd.Series,
                   X_test: pd.DataFrame, y_test: pd.Series,
                   sort_by: str = None,
                   preprocessor=None) -> tuple[pd.DataFrame, dict]:
    trained = {}
    rows = []
    
    # deteksi problem berdasarkan target
    is_regression = pd.api.types.is_numeric_dtype(y_train) and y_train.nunique() > 10
    
    for name, m in models.items():
        t0 = time()

        if preprocessor is not None:
            from sklearn.pipeline import Pipeline
            m = Pipeline([("preprocessor", preprocessor), ("model", m)])

        m.fit(X_train, y_train)
        y_pred = m.predict(X_test)

        trained[name] = m
        print(f"  {name: <20} ({time()-t0:.1f}s)")

        row = {"Model": name, "Time(s)": round(time() - t0, 1)}
        
        if is_regression:
            row["R2_Score"] = r2_score(y_test, y_pred)
            row["RMSE"] = np.sqrt(mean_squared_error(y_test, y_pred))
            row["MAE"] = mean_absolute_error(y_test, y_pred)
        else:
            row["Accuracy"] = accuracy_score(y_test, y_pred)
            row["F1_weighted"] = f1_score(y_test, y_pred, average='weighted')
            try:
                y_proba = m.predict_proba(X_test)
                if y_test.nunique() == 2:
                    row["ROC_AUC"] = roc_auc_score(y_test, y_proba[:, 1])
                else:
                    row["ROC_AUC"] = roc_auc_score(y_test, y_proba, multi_class='ovr')
            except:
                row["ROC_AUC"] = None
                
        rows.append(row)

    df = pd.DataFrame(rows).sort_values(sort_by, ascending=False).reset_index(drop=True)
    return df, trained

def save_competition_result(result_df: pd.DataFrame,
                            filepath: str,
                            append: bool = True) -> None:
    
    
    df = result_df.copy()
    if append and os.path.isfile(filepath):
        existing = pd.read_csv(filepath)
        df = pd.concat([existing, df], ignore_index=True)
    df.to_csv(filepath, index=False)
    print(f"Results saved to {filepath} ({len(result_df)} rows)")

