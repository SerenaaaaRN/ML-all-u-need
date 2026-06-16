import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OneHotEncoder

NUMERIC_COLS = ['Age', 'SibSp', 'Parch', 'Fare']
CATEGORICAL_COLS = ['Sex', 'Embarked', 'Pclass']
DROP_COLS = ['PassengerId', 'Name', 'Ticket', 'Cabin']

def build_preprocessor() -> ColumnTransformer:

    numeric_pipeline = make_pipeline(
        SimpleImputer(strategy='median'),
        RobustScaler()
    )
    category_pipeline = make_pipeline(
        SimpleImputer(strategy='most_frequent'),
        OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    )

    return ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, NUMERIC_COLS),
            ('cat', category_pipeline, CATEGORICAL_COLS),
        ],
        remainder='drop'
    )
