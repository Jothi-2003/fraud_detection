import requests

BASE_URL = "http://localhost:8000"

def predict_fraud(payload):
    response = requests.post(f"{BASE_URL}/fraud/predict", json=payload)
    return response.json()
