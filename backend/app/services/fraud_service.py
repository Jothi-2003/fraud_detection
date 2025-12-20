import numpy as np
from backend.app.core.model_loader import load_fraud_model

model = load_fraud_model()

def predict_fraud(data):
    features = np.array([[
        data.claim_amount,
        data.patient_age,
        data.length_of_stay_days,
        data.number_of_procedures,
        data.deductible_amount,
        data.copay_amount,
        data.previous_claims_patient,
        data.previous_claims_provider,
        data.provider_patient_distance_miles,
        data.claim_submitted_late,
        hash(data.admission_type) % 1000,
        hash(data.provider_type) % 1000
    ]])

    probability = model.predict_proba(features)[0][1]
    prediction = "Fraud" if probability > 0.5 else "Not Fraud"

    return probability, prediction
