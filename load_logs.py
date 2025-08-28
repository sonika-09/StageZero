# scripts/load_logs.py

import os
import json
import pandas as pd

LOGS_DIR = "../logs"  # path to your logs folder
OUTPUT_FILE = "../all_logs.json"

all_logs = []

# Walk through all subfolders
for root, dirs, files in os.walk(LOGS_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            if file.endswith(".txt") or file.endswith(".log"):
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    all_logs.append({"filename": file_path, "text": text})
            elif file.endswith(".csv"):
                df = pd.read_csv(file_path).dropna()
                for _, row in df.iterrows():
                    # assuming text column exists
                    if "text" in row:
                        all_logs.append({"filename": file_path, "text": str(row["text"])})
            elif file.endswith(".json"):
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for entry in data:
                            all_logs.append({"filename": file_path, "text": str(entry)})
                    elif isinstance(data, dict):
                        all_logs.append({"filename": file_path, "text": str(data)})
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Save all logs to one JSON file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_logs, f, indent=2)

print(f"Loaded {len(all_logs)} logs into {OUTPUT_FILE}")
