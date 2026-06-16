from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from utils.modeling import compare_models

MODELS = {
    "LogisticReg": LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42),
    "RandomForest": RandomForestClassifier(n_jobs=-1, random_state=42),
    "GradientBoosting": GradientBoostingClassifier(random_state=42),
    "DecisionTree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(random_state=42, probability=True),
}

def run_competition(X_train, X_test, y_train, y_test, preprocessor=None):

    results_df, trained = compare_models(
        MODELS, X_train, y_train, X_test, y_test,
        sort_by='Accuracy', preprocessor=preprocessor
    )

    best_idx = results_df.iloc[0]
    winner_name = best_idx["Model"]
    
    print(f"\nWinner: {winner_name} (Accuracy: {best_idx['Accuracy']:.4f})")
    return results_df, winner_name, trained