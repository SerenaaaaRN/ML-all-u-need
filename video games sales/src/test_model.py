import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("video games sales/models/LinearRegression.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("File not found")

# Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
# 15961,Drone Tactics,DS,2007,Strategy,Success,0.01,0,0,0,0.02
SAMPLE = {
    "Platform": "Wii",
    "Year": 2006,
    "Genre": "Sports",
    "Publisher": "Nintendo",
    "NA_Sales": 41.49,
    "EU_Sales": 29.02,
    "JP_Sales": 3.77,
    "Other_Sales": 8.46,
    "Global_Sales": 82.74
}

def predict(raw: dict) -> float:
    df = pd.DataFrame([raw])
    pred = pipeline.predict(df)[0]

    return float(pred)


if __name__ == "__main__":
    result = predict(SAMPLE)
    print(f"Prediksi Penjualan Global: {result:.2f}")