import joblib
from backend.app.core.config import MODEL_PATH

def load_fraud_model():
    return joblib.load(MODEL_PATH)