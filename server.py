from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/upload_log")
async def upload_log(request: Request):
    data = await request.json()
    log_entry = data["log"]

    classified = classify_logs(log_entry)
    return {"received_log": log_entry, "classified": classified}

def classify_logs(log_entry):
    # Super simple dummy classifier
    if "failed" in log_entry.lower() and "login" in log_entry.lower():
        return {"technique": "Brute Force", "mitre_id": "T1110"}
    elif "ransomware" in log_entry.lower():
        return {"technique": "Data Encrypted for Impact", "mitre_id": "T1486"}
    else:
        return {"technique": "Unknown", "mitre_id": None}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
