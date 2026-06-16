import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from sklearn.model_selection import train_test_split
from utils.modeling import save_competition_result
from preprocessing import build_preprocessor, cleaning
from training import run_competition

DATA_PATH = Path("medical cost personal/data/insurance.csv")
TARGET = 'charges'
MODEL_PATH = Path("medical cost personal/models")

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    df = cleaning(df)

    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    preprocessor = build_preprocessor()
    result_df, winner_name, trained = run_competition(
        X_train, X_test, y_train, y_test, preprocessor
    )

    MODEL_PATH.mkdir(parents=True, exist_ok=True)
    save_competition_result(result_df, MODEL_PATH / "results.csv", append=False)

    N_BEST = 3
    N_BEST = 3
    for i in range(min(N_BEST, len(result_df))):
        row = result_df.iloc[i]
        name = row["Model"]
        joblib.dump(trained[name], MODEL_PATH / f"{name}.joblib")
        print(f"  #{i+1}: {name} (R2 Score: {row['R2_Score']:.4f})")
    
    joblib.dump(trained[winner_name], f"api/models/med-cost.joblib")    #save to api
    winner_name = result_df.iloc[0]["Model"]
    print(f"\nWinner: {winner_name}")
