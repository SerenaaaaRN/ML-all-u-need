import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, RobustScaler, OneHotEncoder
from utils.cleaning import handle_whitespace, drop_duplicates

NUMERIC_COLS = [
    'Pre_Semester_GPA', 'Weekly_GenAI_Hours', 'Traditional_Study_Hours', 
    'Perceived_AI_Dependency', 'Anxiety_Level_During_Exams', 'Tool_Diversity'
]
BINARY_COLS = ['Paid_Subscription']
ORDINAL_COLS = ['Year_of_Study', 'Prompt_Engineering_Skill']
ORDINAL_CATEGORIES = [
    ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate'], 
    ['Beginner', 'Intermediate', 'Advanced']                   
]

NOMINAL_COLS = ['Major_Category', 'Primary_Use_Case', 'Institutional_Policy']

def handle_outlier(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  

    df.drop(columns=['Student_ID'], inplace=True)
    df['Paid_Subscription'] = df['Paid_Subscription'].astype(int)

    df = handle_whitespace(df)
    df = drop_duplicates(df)

    leakage_cols = ['Post_Semester_GPA', 'Skill_Retention_Score']
    df.drop(columns=[col for col in leakage_cols if col in df.columns], inplace=True, errors='ignore')

    if 'Weekly_GenAI_Hours' in df.columns:
        df['Weekly_GenAI_Hours'] = df['Weekly_GenAI_Hours'].clip(lower=0)
    if 'Traditional_Study_Hours' in df.columns:
        df['Traditional_Study_Hours'] = df['Traditional_Study_Hours'].clip(lower=0)

    if 'Pre_Semester_GPA' in df.columns:
        df['Pre_Semester_GPA'] = df['Pre_Semester_GPA'].clip(lower=0.0, upper=4.0)

    if 'Perceived_AI_Dependency' in df.columns:
        df['Perceived_AI_Dependency'] = df['Perceived_AI_Dependency'].clip(lower=1, upper=10)
    if 'Anxiety_Level_During_Exams' in df.columns:
        df['Anxiety_Level_During_Exams'] = df['Anxiety_Level_During_Exams'].clip(lower=1, upper=10)
    
    return df


def build_preprocessor() -> ColumnTransformer:

    numeric_pipeline = make_pipeline(
        SimpleImputer(strategy='median'),
        RobustScaler()
    )

    binary_pipeline = make_pipeline(
        SimpleImputer(strategy='most_frequent'),
    )

    ordinal_pipeline = make_pipeline(
        SimpleImputer(strategy='most_frequent'),
        OrdinalEncoder(
            categories=ORDINAL_CATEGORIES,
            handle_unknown='use_encoded_value',
            unknown_value=-1
        )
    )

    ohe_pipeline = make_pipeline(
        SimpleImputer(strategy='most_frequent'),
        OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False)
    )


    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, NUMERIC_COLS),
            ('cat', binary_pipeline, BINARY_COLS),
            ('ord', ordinal_pipeline, ORDINAL_COLS),
            ('ohe', ohe_pipeline, NOMINAL_COLS),
        ],
        remainder='drop'
    )

    return preprocessor