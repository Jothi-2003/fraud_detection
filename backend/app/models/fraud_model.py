from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.sql import func
from backend.app.database.db import Base

class FraudPrediction(Base):
    __tablename__ = "fraud_predictions"

    id = Column(Integer, primary_key=True, index=True)

    claim_amount = Column(Float)
    patient_age = Column(Integer)
    length_of_stay_days = Column(Integer)
    number_of_procedures = Column(Integer)
    deductible_amount = Column(Float)
    copay_amount = Column(Float)
    previous_claims_patient = Column(Integer)
    previous_claims_provider = Column(Integer)
    provider_patient_distance_miles = Column(Float)
    claim_submitted_late = Column(Integer)
    admission_type = Column(String)
    provider_type = Column(String)
    fraud_probability = Column(Float)
    fraud_prediction = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())