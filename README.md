# ML-all-u-need

My personal project for machine learning and data exploration — a monorepo of classification and regression experiments built with Python. Each project follows the same pipeline: load data, explore, preprocess, compare models, evaluate.

## Tech Stack

Python • scikit-learn • pandas • numpy • matplotlib • seaborn • joblib • Jupyter Notebook

## Projects

| Project | Type | Best Model |
|---|---|---|
| [Ad Click Prediction](advertisement_click_prediction/) | Binary Classification | NaiveBayes (Acc 92%) |
| [Diabetes Prediction](diabetes_prediction/) | Binary Classification | NaiveBayes (Acc 77%) |
| [Impact of AI Student](impact%20of%20ai%20student/) | Multiclass Classification | HistGradientBoosting (Acc 53%) |
| [Rain Prediction](rain_prediction/) | Binary Classification | RandomForest (Acc 85%) |
| [Telco Customer Churn](telco%20customer%20churn/) | Binary Classification | LogisticReg (Acc 79%) |
| [Titanic Survival Prediction](titanic%20survival%20prediction/) | Binary Classification | KNN (Acc 83%) |
| [Video Games Sales](video%20games%20sales/) | Regression | GradientBoosting (R2 0.85) |
| [Medical Cost Personal](medical%20cost%20personal/) | Regression | GradientBoosting (R2 0.89) |
| [Heart Failure Prediction](heart%20failure%20prediction/) | Binary Classification | GradientBoosting (Acc 88%) |
| [Wine Quality Classification](wine_quality_classification/) | Multiclass Classification | RandomForest (Acc 65%) |

## Structure

```
<project>/
├── data/              # Raw dataset
├── models/            # Trained models + results.csv
├── notebook/          # EDA notebooks
├── src/
│   ├── preprocessing.py   # Preprocessing pipeline
│   ├── training.py        # Model definitions + competition
│   ├── main.py            # Entry point
│   └── test_model.py      # Predict with sample data
└── README.md

utils/                 # Shared utilities
├── cleaning.py, eda.py, encoding.py
├── modeling.py, scaling.py, transformer.py
├── validation.py, visualization.py
└── __init__.py
```

## Quick Start

```bash
pip install scikit-learn pandas numpy matplotlib seaborn joblib

python advertisement_click_prediction/src/main.py
```

## Note

This is a personal practice repository. Model performance reflects experimental results, not production benchmarks.
