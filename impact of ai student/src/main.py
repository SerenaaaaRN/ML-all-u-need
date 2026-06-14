import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from sklearn.model_selection import train_test_split
from utils.modeling import save_competition_result
from preprocessing import build_preprocessor, handle_outlier
from training import run_competition

DATA_PATH = Path("impact of ai student/data/ai_student_impact_dataset.csv")
TARGET = 'Burnout_Risk_Level'
MODEL_PATH = Path("impact of ai student/models")

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)

    df = handle_outlier(df)

    target_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    y = df[TARGET].map(target_mapping)
    X = df.drop(columns=[TARGET])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    preprocessor = build_preprocessor()
    result_df, winner_name, trained = run_competition(X_train, X_test, y_train, y_test, preprocessor)

    MODEL_PATH.mkdir(parents=True, exist_ok=True)
    save_competition_result(result_df, MODEL_PATH / "results.csv")

    N_BEST = 3
    for i in range(min(N_BEST, len(result_df))):
        row = result_df.iloc[i]
        name = row["Model"]
        joblib.dump(trained[name], MODEL_PATH / f"{name}.joblib")
        print(f"  #{i+1}: {name} (Accuracy: {row['Accuracy']:.4f})")

    print(f"\nWinner: {winner_name}")

    



