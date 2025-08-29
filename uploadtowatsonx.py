import json
from ibm_watsonxdata import DataClient

API_KEY = "kwYkece0-5S2xaH1EawcAuGr5WEePEtNQILm6HqQFd4w"
URL = "https://eu-de.ml.cloud.ibm.com"

data_client = DataClient(api_key=API_KEY, url=URL)

with open('log_classification.json', 'r') as f:
    log_classification = json.load(f)

dataset = [
    {'log_id': k, 'log_text': v['text'], 'matched_techniques': v['matched_techniques']}
    for k, v in log_classification.items()
]

# Upload dataset (replace table_name and workspace as needed)
table_name = "mitre_logs"
workspace = "YOUR_WORKSPACE_ID"

data_client.upload_table(dataset, table_name=table_name, workspace=workspace)
print(f"Uploaded {len(dataset)} logs to Watsonx Data")
