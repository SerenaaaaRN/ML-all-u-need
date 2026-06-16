import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from utils.cleaning import fix_dtypes, handle_whitespace, drop_duplicates

NUMERIC_COLS = ['age', 'bmi', 'children']
CAT_COLS = ['sex', 'smoker', 'region']

def cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = fix_dtypes(df)
    df = handle_whitespace(df)
    df = drop_duplicates(df)

    if 'bmi' in df.columns:
        df['bmi'] = df['bmi'].clip(13.7, 47.2)
    
    return df

def build_preprocessor() -> ColumnTransformer:
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', RobustScaler(), NUMERIC_COLS),
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False), CAT_COLS)
        ],
        remainder='drop'
    )
    return preprocessor
