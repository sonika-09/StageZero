import requests
import time
import os

SERVER_URL = "http://localhost:8000/upload_log"
LOG_DIR = "extracted_logs"   # where your logs were extracted

def stream_logs():
    for root, _, files in os.walk(LOG_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r", errors="ignore") as f:
                for line in f:
                    yield line.strip()

# Send logs one by one to server
for log_line in stream_logs():
    if log_line:  # skip empty lines
        try:
            response = requests.post(SERVER_URL, json={"log": log_line})
            print("Sent:", log_line[:80], "...")  # print first 80 chars
            print("Server response:", response.json())
        except Exception as e:
            print("Error:", e)
    time.sleep(1)  # simulate real-time feed
