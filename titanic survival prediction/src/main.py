import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from sklearn.model_selection import train_test_split
from utils.modeling import save_competition_result
from preprocessing import feature_engineering, build_preprocessor
from training import run_competition


DATA_PATH = Path("titanic survival prediction/data/Titanic-Dataset.csv")
TARGET = 'Survived'
MODEL_PATH = Path("titanic survival prediction/models")

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)

    df = feature_engineering(df)

    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = build_preprocessor()

    result_df, winner_name, trained_models = run_competition(
        X_train, X_test, y_train, y_test, preprocessor
    )

    MODEL_PATH.mkdir(parents=True, exist_ok=True)
    save_competition_result(result_df, MODEL_PATH / "results.csv")

    for i in range(min(3, len(result_df))):
        row = result_df.iloc[i]
        name = row["Model"]
        joblib.dump(trained_models[name], MODEL_PATH / f"{name}.joblib")
        print(f"  #{i+1}: {name} (Accuracy: {row['Accuracy']:.4f})")

    print(f"\nFinal winner {winner_name}")
