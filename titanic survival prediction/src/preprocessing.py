import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler, FunctionTransformer

NUMERIC_COLS = ['Age', 'SibSp', 'Parch', 'Fare']
CATEGORICAL_COLS = ['Sex', 'Embarked', 'Pclass', 'Title']
DROP_COLS = ['PassengerId', 'Ticket', 'Cabin']

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.drop(columns=DROP_COLS, inplace=True, errors='ignore')
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

    rare_titles = ['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
    df['Title'] = df['Title'].replace(rare_titles, 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')

    df.drop(columns=['Name'], inplace=True)

    medians = df.groupby(['Title', 'Pclass'])['Age'].transform('median')
    df['Age'] = df['Age'].fillna(medians)
    if df['Age'].isnull().any():
        df['Age'] = df['Age'].fillna(df['Age'].median())

    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['Pclass'] = df['Pclass'].astype(str)

    return df



def build_preprocessor() -> Pipeline:

    fe_step = FunctionTransformer(feature_engineering, validate=False)

    numeric_pipeline = RobustScaler()
    category_pipeline = make_pipeline(
        SimpleImputer(strategy='most_frequent'),
        OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    )

    column_transformer = ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, NUMERIC_COLS),
            ('cat', category_pipeline, CATEGORICAL_COLS),
        ],
        remainder='drop'
    )

    return Pipeline([
        ('feature_engineering', fe_step),
        ('column_transformer', column_transformer),
    ])