import sys
import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent

PROJECT_FOLDER_MAP = {
    "ad-click":     "advertisement_click_prediction",
    "diabetes":     "diabetes_prediction",
    "ai-student":   "impact of ai student",
    "rain":         "rain_prediction",
    "telco-churn":  "telco customer churn",
    "titanic":      "titanic survival prediction",
    "video-games":  "video games sales",
    "wine-quality": "wine_quality_classification",
}

def load_all_models() -> dict:
    loaded = {}
    for project_id, folder_name in PROJECT_FOLDER_MAP.items():
        model_dir = BASE / folder_name / "models"
        pkl_files = list(model_dir.glob("*.joblib"))
        if not pkl_files:
            print(f"No .joblib found for {project_id}")
            continue
        
        if project_id == "ad-click": best_name = "NaiveBayes"
        elif project_id == "diabetes": best_name = "NaiveBayes"
        elif project_id == "ai-student": best_name = "HistGradientBoosting"
        elif project_id == "rain": best_name = "RandomForest"
        elif project_id == "telco-churn": best_name = "LogisticReg"
        elif project_id == "titanic": best_name = "RandomForest"
        elif project_id == "video-games": best_name = "LinearRegression"
        elif project_id == "wine-quality": best_name = "RandomForest"
        else: best_name = "best"
        
        best = next((f for f in pkl_files if best_name.lower() in f.name.lower()), pkl_files[0])
        
        src_path = str(model_dir.parent / "src")
        sys.path.insert(0, src_path)
        try:
            loaded[project_id] = joblib.load(best)
            print(f"Loaded: {project_id} <- {best.name}")
        except Exception as e:
            print(f"Error loading {project_id}: {e}")
        finally:
            if src_path in sys.path:
                sys.path.remove(src_path)
                
    return loaded
