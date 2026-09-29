
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load("models/cybersecurity_model.joblib")


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Cybersecurity Threat Detection API is running"
    }


# Serve the HTML interface
@app.get("/app")
def serve_app():
    return FileResponse("app/index.html")


# Input data structure
class TrafficData(BaseModel):
    src_port: int
    dst_port: int
    protocol: str
    bytes_sent: int
    bytes_received: int
    user_agent: str
    is_internal_traffic: bool


# Prediction endpoint
@app.post("/predict")
def predict(data: TrafficData):

    # Convert input data to DataFrame
    input_data = pd.DataFrame([data.model_dump()])

    print(input_data)
    print(model.predict_proba(input_data))
    print(model.predict(input_data))

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probabilities
    probability = model.predict_proba(input_data)[0]

    # Convert prediction to readable label
    label = "Attack" if prediction == 1 else "Normal"

    # Get confidence
    confidence = probability[prediction] * 100

    return {
        "prediction": label,
        "confidence": round(float(confidence), 2)
    }

