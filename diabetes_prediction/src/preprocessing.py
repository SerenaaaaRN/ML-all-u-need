from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

NUMERIC_COLS = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

def build_preprocessor():

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), NUMERIC_COLS),
        ],
        remainder='drop'
    )

    return preprocessor