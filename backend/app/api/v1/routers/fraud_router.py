from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Make sure these paths match your project structure
from backend.app.schemas.fraud_schema import FraudRequest, FraudResponse
from backend.app.services.fraud_service import predict_fraud
from backend.app.database.db import get_db
from backend.app.models.fraud_model import FraudPrediction

# Create router
router = APIRouter(prefix="/fraud", tags=["Fraud Detection"])

# Predict endpoint
@router.post("/predict", response_model=FraudResponse)
def predict_claim(data: FraudRequest, db: Session = Depends(get_db)):
    # Call the prediction service
    prob, prediction = predict_fraud(data)

    # Save to database
    fraud_row = FraudPrediction(
        claim_amount=data.claim_amount,
        patient_age=data.patient_age,
        length_of_stay_days=data.length_of_stay_days,
        number_of_procedures=data.number_of_procedures,
        deductible_amount=data.deductible_amount,
        copay_amount=data.copay_amount,
        previous_claims_patient=data.previous_claims_patient,
        previous_claims_provider=data.previous_claims_provider,
        provider_patient_distance_miles=data.provider_patient_distance_miles,
        claim_submitted_late=data.claim_submitted_late,
        admission_type=data.admission_type,
        provider_type=data.provider_type,
        fraud_probability=round(prob, 2),
        fraud_prediction=prediction
    )
    db.add(fraud_row)
    db.commit()
    db.refresh(fraud_row)

    return {
        "fraud_probability": round(prob, 2),
        "fraud_prediction": prediction
    }

# Metrics endpoint
@router.get("/metrics")
def fraud_metrics():
    return {
        "model": "RandomForest",
        "target": "Is_Fraudulent"
    }
