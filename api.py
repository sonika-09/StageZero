# serve classified logs locally.
from fastapi import FastAPI
import json
import os

app = FastAPI()

CLASSIFIED_LOGS_JSON = os.path.join(os.getcwd(), "classified_logs.json")

@app.get("/classify")
def classify_logs():
    with open(CLASSIFIED_LOGS_JSON, "r", encoding="utf-8") as f:
        classified_logs = json.load(f)
    return classified_logs

@app.get("/sample")
def sample_log():
    return {"example": "Log classification API running locally."}
