import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from utils.cleaning import handle_whitespace, fix_dtypes, drop_duplicates
from utils.modeling import save_competition_result
from sklearn.model_selection import train_test_split
from preprocessing import build_preprocessor
from training import run_competition

DATA_PATH = Path("rain_prediction/data/weatherAUS.csv")
TARGET = 'RainTomorrow'
MODEL_PATH = Path("rain_prediction/models")

def clean_data():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(columns=["Sunshine","Evaporation","Cloud3pm","Cloud9am","Date"], errors="ignore")
    df = df.dropna(subset=[TARGET]).reset_index(drop=True)
    df = handle_whitespace(df)
    df = fix_dtypes(df, ["Date"])
    df = drop_duplicates(df)
    return df

if __name__ == "__main__":
    df = clean_data()

    X = df.drop(columns=[TARGET])
    y = df[TARGET].astype(str).map({"No": 0, "Yes": 1})
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = build_preprocessor()
    result_df, _, trained = run_competition(X_train, X_test, y_train, y_test, preprocessor)
    save_competition_result(result_df, MODEL_PATH / "results.csv")

    MODEL_PATH.mkdir(parents=True, exist_ok=True)

    # print 3 model terbaik
    N_BEST = 3
    for i in range(min(N_BEST, len(result_df))):
        row = result_df.iloc[i]
        name = row["Model"]
        joblib.dump(trained[name], MODEL_PATH / f"{name}.joblib")
        print(f"  #{i+1}: {name} (Accuracy: {row['Accuracy']:.4f})")

    winner_name = result_df.iloc[0]["Model"]
    print(f"\nWinner: {winner_name}")
