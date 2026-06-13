import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OneHotEncoder, OrdinalEncoder, FunctionTransformer
from sklearn.preprocessing import TargetEncoder

NUMERIC_COLS = ['MinTemp', 'MaxTemp', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm',
                'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm']
WIND_COLS = ['WindGustDir', 'WindDir9am', 'WindDir3pm']

def build_preprocessor():
    # numerik biasa
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])

    # rainfall
    rain_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('log', FunctionTransformer(np.log1p)),
        ('scaler', RobustScaler())
    ])

    # location
    loc_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('target_enc', TargetEncoder(smooth='auto'))
    ])

    # mata angin
    wind_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # rain today
    binary_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ordinal', OrdinalEncoder())
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, NUMERIC_COLS),
            ('rain', rain_pipeline, ['Rainfall']),
            ('loc', loc_pipeline, ['Location']),
            ('wind', wind_pipeline, WIND_COLS),
            ('binary', binary_pipeline, ['RainToday'])
        ],
        remainder='drop'
    )

    return preprocessor