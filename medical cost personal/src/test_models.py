import sys
import joblib
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
MODEL_PATH = Path("medical cost personal/models/LinearRegression.joblib")

try:
    pipeline = joblib.load(MODEL_PATH)
    print("Model berhasil di load\n")
except FileNotFoundError:
    print("File not found")
    exit()

# age,sex,bmi,children,smoker,region,charges
# 19,female,27.9,0,yes,southwest,16884.924
SAMPLE = {
    "Age": 19,
    "sex": 'female',
    "bmi": 27.9,
    "children": 0,
    "smoker": "yes",
    "region": "southwest"
}

def predict(raw: dict):
    df = pd.DataFrame([raw])
    pred = pipeline.predict(df)[0]
    return float(pred)

if __name__ == "__main__":
    result, conf = predict(SAMPLE)
    print(f"Prediksi Pengeluaran Medical Cost: {result:.2f}")