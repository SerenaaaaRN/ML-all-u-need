from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from utils.modeling import compare_models

def get_models() -> dict:
    return {
        "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
        "NaiveBayes":         GaussianNB(),
        "DecisionTree":       DecisionTreeClassifier(random_state=42),
        "KNN":                KNeighborsClassifier(),
        "SVM":                SVC(random_state=42, probability=True),
        "RandomForest":       RandomForestClassifier(n_jobs=-1, random_state=42, n_estimators=300),
    }

def run_competition(X_train, X_test, y_train, y_test, preprocessor=None):
    models = get_models()
    results_df, trained = compare_models(
        models, X_train, y_train, X_test, y_test,
        sort_by="Accuracy", preprocessor=preprocessor
    )

    best_idx = results_df.iloc[0]
    winner_name = best_idx["Model"]
    
    print(f"\nWinner: {winner_name} (Accuracy: {best_idx['Accuracy']:.4f})")

    return results_df, winner_name, trained

