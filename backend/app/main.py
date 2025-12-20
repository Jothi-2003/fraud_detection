from fastapi import FastAPI
from backend.app.api.v1.routers.fraud_router import router
from backend.app.database.db import Base, engine

app = FastAPI(title="Health Insurance Fraud Detection")

# Create all tables
Base.metadata.create_all(bind=engine)

# Register router with a single consistent tag
app.include_router(router, tags=["Fraud Detection"])

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running"}
