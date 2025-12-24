import streamlit as st
import requests

st.title("🏥 Health Insurance Fraud Detection")

# Input fields
claim_amount = st.number_input("Claim Amount")
patient_age = st.number_input("Patient Age", 0, 100)
length_of_stay_days = st.number_input("Length of Stay (Days)", 0, 60)
number_of_procedures = st.number_input("Number of Procedures", 0, 20)
deductible_amount = st.number_input("Deductible Amount")
copay_amount = st.number_input("CoPay Amount")
previous_claims_patient = st.number_input("Previous Claims (Patient)", 0, 20)
previous_claims_provider = st.number_input("Previous Claims (Provider)", 0, 50)
provider_patient_distance_miles = st.number_input("Distance (Miles)")
claim_submitted_late = st.selectbox("Claim Submitted Late", [0, 1])
admission_type = st.selectbox("Admission Type", ["Emergency", "Planned"])
provider_type = st.selectbox("Provider Type", ["Hospital", "Clinic"])

# Button to predict
if st.button("Predict Fraud"):
    payload = {
        "claim_amount": claim_amount,
        "patient_age": patient_age,
        "length_of_stay_days": length_of_stay_days,
        "number_of_procedures": number_of_procedures,
        "deductible_amount": deductible_amount,
        "copay_amount": copay_amount,
        "previous_claims_patient": previous_claims_patient,
        "previous_claims_provider": previous_claims_provider,
        "provider_patient_distance_miles": provider_patient_distance_miles,
        "claim_submitted_late": claim_submitted_late,
        "admission_type": admission_type,
        "provider_type": provider_type
    }

    try:
        response = requests.post("http://localhost:8000/fraud/predict", json=payload)
        result = response.json()
        
        # Debug: see what FastAPI actually returned
        st.write(result)

        # Safe access
        if "fraud_probability" in result and "fraud_prediction" in result:
            st.success(f"Fraud Probability: {result['fraud_probability']}")
            st.warning(f"Prediction: {result['fraud_prediction']}")
        else:
            st.error(f"API error: {result}")
    except Exception as e:
        st.error(f"Request failed: {e}")
