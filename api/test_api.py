import pytest
from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance. 
# We use a with block to trigger the lifespan events (startup/shutdown) so that models are loaded.
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_ad_click_prediction(client: TestClient):
    payload = {
        "Gender": "Female",
        "Age": 32,
        "EstimatedSalary": 150000
    }
    response = client.post("/api/predict/ad-click", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data
    assert "label" in data

def test_diabetes_prediction(client: TestClient):
    payload = {
        "Pregnancies": 6,
        "Glucose": 148,
        "BloodPressure": 72,
        "SkinThickness": 35,
        "Insulin": 0,
        "BMI": 33.6,
        "DiabetesPedigreeFunction": 0.627,
        "Age": 50
    }
    response = client.post("/api/predict/diabetes", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data
    assert "label" in data

def test_ai_student_prediction(client: TestClient):
    payload = {
        "Pre_Semester_GPA": 3.5,
        "Weekly_GenAI_Hours": 5,
        "Traditional_Study_Hours": 15,
        "Perceived_AI_Dependency": 5,
        "Anxiety_Level_During_Exams": 6,
        "Tool_Diversity": 3,
        "Paid_Subscription": 0,
        "Year_of_Study": "Junior",
        "Prompt_Engineering_Skill": "Intermediate",
        "Major_Category": "Engineering",
        "Primary_Use_Case": "Research",
        "Institutional_Policy": "Allowed"
    }
    response = client.post("/api/predict/ai-student", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data

def test_rain_prediction(client: TestClient):
    payload = {
        "Location": "Sydney",
        "MinTemp": 18.5,
        "MaxTemp": 26.3,
        "Rainfall": 2.4,
        "WindGustDir": "NW",
        "WindGustSpeed": 44,
        "WindDir9am": "N",
        "WindDir3pm": "NW",
        "WindSpeed9am": 15,
        "WindSpeed3pm": 22,
        "Humidity9am": 78,
        "Humidity3pm": 100,
        "Pressure9am": 1019.2,
        "Pressure3pm": 1016.8,
        "Temp9am": 21.0,
        "Temp3pm": 25.1,
        "RainToday": "No"
    }
    response = client.post("/api/predict/rain", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data

def test_telco_churn_prediction(client: TestClient):
    payload = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "No",
        "MultipleLines": "No phone service",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85,
        "TotalCharges": "29.85"
    }
    response = client.post("/api/predict/telco-churn", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data

def test_titanic_prediction(client: TestClient):
    payload = {
        "Pclass": 3,
        "Name": "Braund, Mr. Owen Harris",
        "Sex": "male",
        "Age": 22.0,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S"
    }
    response = client.post("/api/predict/titanic", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data

def test_video_games_prediction(client: TestClient):
    payload = {
        "Platform": "Wii",
        "Year": 2006,
        "Genre": "Sports",
        "Publisher": "Nintendo",
        "NA_Sales": 41.49,
        "EU_Sales": 29.02,
        "JP_Sales": 3.77,
        "Other_Sales": 8.46,
        "Global_Sales": 82.74
    }
    response = client.post("/api/predict/video-games", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data

def test_wine_quality_prediction(client: TestClient):
    payload = {
        "fixed_acidity": 7.4,
        "volatile_acidity": 0.70,
        "citric_acid": 0.00,
        "residual_sugar": 1.9,
        "chlorides": 0.076,
        "free_sulfur_dioxide": 11.0,
        "total_sulfur_dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4
    }
    response = client.post("/api/predict/wine-quality", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "value" in data

def test_eda_report(client: TestClient):
    response = client.get("/api/eda/titanic")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "RMS Titanic Survival Demographics Study"
    assert len(data["sections"]) > 0
    assert "chart_data" in data

    response = client.get("/api/eda/invalid-project")
    assert response.status_code == 404
