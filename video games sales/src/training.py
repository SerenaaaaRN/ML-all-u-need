from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from utils.modeling import compare_models

def get_models() -> dict:
    return {
        "LinearRegression": LinearRegression(),
        "ElasticNet": ElasticNet(), 
        "SVR": SVR(),
        "RandomForest": RandomForestRegressor(n_jobs=-1, random_state=42, n_estimators=300),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=300, random_state=42),
    }

def run_competition(X_train, X_test, y_train, y_test, preprocessor = None):
    models = get_models()

    result_df, trained = compare_models(
        models, X_train, y_train, X_test, y_test, preprocessor=preprocessor,
        sort_by='R2_Score'
    )

    best_idx = result_df.iloc[0]
    winner_name = best_idx['Model']

    print(f"\nWinner: {winner_name} (R2 Score: {best_idx['R2_Score']})")
    return result_df, winner_name, trained