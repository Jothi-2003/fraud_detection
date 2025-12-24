from pydantic import BaseModel,Field,validator

class FraudRequest(BaseModel):
    claim_amount: float
    patient_age: int
    length_of_stay_days: int
    number_of_procedures: int
    deductible_amount: float
    copay_amount: float
    previous_claims_patient: int
    previous_claims_provider: int
    provider_patient_distance_miles: float
    claim_submitted_late: int
    admission_type: str
    provider_type: str

class FraudResponse(BaseModel):
    fraud_probability: float
    fraud_prediction: str
