import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OneHotEncoder, FunctionTransformer
from sklearn.preprocessing import TargetEncoder

NUMERIC_COLS = ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
TARGET_COL = 'Global_Sales'

HIGH_CARD_COLS = ['Publisher']
LOW_CARD_COLS = ['Platform', 'Genre']

def build_preprocessor():
    # pipeline untuk sales dan year
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('log', FunctionTransformer(np.log1p)),
        ('scaler', RobustScaler())
    ])

    # pipeline untuk publisher, target encoder dipilih karna publisher banyak unik
    pub_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('target_enc', TargetEncoder(smooth='auto'))
    ])

    # pipeline untuk genre
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])


    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, NUMERIC_COLS),
            ('pub', pub_pipeline, HIGH_CARD_COLS),
            ('cat', cat_pipeline, LOW_CARD_COLS)
        ],
        remainder='drop'
    )

    return preprocessor