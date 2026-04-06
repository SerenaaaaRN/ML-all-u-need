from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUMERIC_COLS = ['Age','EstimatedSalary']
CATEGORY_COL = ['Gender']

def build_preprocessor():
    preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), NUMERIC_COLS),
        ('cat', OneHotEncoder(drop='first'), CATEGORY_COL)
    ])
    return preprocessor
    