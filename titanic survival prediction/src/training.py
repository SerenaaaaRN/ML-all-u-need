from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from utils.modeling import compare_models

def get_models() -> dict:
    return {
        "LogisticReg":        LogisticRegression(random_state=12345, max_iter=1000),
        "NaiveBayes":         GaussianNB(),
        "DecisionTree":       DecisionTreeClassifier(random_state=42),
        "KNN":                KNeighborsClassifier(),
        "RandomForest":       RandomForestClassifier(n_jobs=-1, random_state=42, n_estimators=200),
    }

def run_competition(X_train, X_test, y_train, y_test, preprocessor=None):
    models = get_models()

    result_df, trained = compare_models(
        models, X_train, y_train, X_test, y_test,
        sort_by="Accuracy", preprocessor=preprocessor
    )

    best_idx = result_df.iloc[0]
    winner_name = best_idx["Model"]
    print(f"\nWinner: {winner_name} (Accuracy: {best_idx['Accuracy']:.4f})")

    return result_df, winner_name, trained