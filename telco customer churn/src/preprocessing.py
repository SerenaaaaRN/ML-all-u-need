from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

NUMERIC_COLS = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']
BINARY_COLS = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
MULTI_COLS = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
              'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']

def build_preprocessor() -> ColumnTransformer:

    numeric_cols = Pipeline([
        ('imputer', SimpleImputer(strategy='median'))
    ])

    binary_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ordinal', OrdinalEncoder())
    ])

    ohe_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(drop='first', sparse_output=False))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_cols, NUMERIC_COLS),
            ('bin', binary_pipeline, BINARY_COLS),
            ('mul', ohe_pipeline, MULTI_COLS),
        ],
        remainder='drop'
    )
    return preprocessor
