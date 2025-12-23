import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("datasets/health_claims.csv")

print("Columns in dataset:", df.columns)

# ===============================
# TARGET COLUMN
# ===============================
TARGET_COLUMN = "Is_Fraudulent"

# ===============================
# SELECT IMPORTANT FEATURES
# (Numerical + useful categorical)
# ===============================
features = [
    "Claim_Amount",
    "Patient_Age",
    "Length_of_Stay_Days",
    "Number_of_Procedures",
    "Deductible_Amount",
    "CoPay_Amount",
    "Number_of_Previous_Claims_Patient",
    "Number_of_Previous_Claims_Provider",
    "Provider_Patient_Distance_Miles",
    "Claim_Submitted_Late",
    "Admission_Type",
    "Provider_Type"
]

X = df[features]
y = df[TARGET_COLUMN]

# ===============================
# HANDLE CATEGORICAL DATA
# ===============================
label_encoders = {}
for col in X.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le

# ===============================
# TRAIN-TEST SPLIT
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# TRAIN MODEL
# ===============================
model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# ===============================
# SAVE MODEL
# ===============================
joblib.dump(model, "backend/app/mlmodels/fraud_model.pkl")

print("✅ Model trained successfully")
print("✅ Target column used:", TARGET_COLUMN)
print("✅ fraud_model.pkl saved")
