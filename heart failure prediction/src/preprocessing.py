import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, StandardScaler, OneHotEncoder
from utils.cleaning import handle_whitespace 

CATEGORICAL_COLS = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
NUMERIC_ROBUST = ['FastingBS', 'Cholesterol']
NUMERIC_STANDARD = ['Age', 'RestingBP', 'MaxHR', 'Oldpeak']

def cleaning_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = handle_whitespace(df)
    if 'Cholesterol' in df.columns:
        df['Cholesterol'] = df['Cholesterol'].clip(32.6, 407.6)
    
    if 'RestingBP' in df.columns:
        df['RestingBP'] = df['RestingBP'].clip(90, 170)

    if 'Oldpeak' in df.columns:
        df['Oldpeak'] = df['Oldpeak'].clip(-2.2, 3.7)

    return df

def build_preprocessor()-> ColumnTransformer:
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num_robust', RobustScaler(), NUMERIC_ROBUST),
            ('num_standard', StandardScaler(), NUMERIC_STANDARD),
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False), CATEGORICAL_COLS),
        ],
        remainder='drop'
    )
    return preprocessor
