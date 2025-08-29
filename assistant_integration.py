# retrieve relevant logs based on MITRE IDs.
from ibm_watsonxdata import DataClient

API_KEY = "kwYkece0-5S2xaH1EawcAuGr5WEePEtNQILm6HqQFd4w"
URL = "https://eu-de.ml.cloud.ibm.com"

data_client = DataClient(api_key=API_KEY, url=URL)

# Example: query logs for a specific technique
technique_id = "T1059"
query = f"SELECT * FROM mitre_logs WHERE ARRAY_CONTAINS(matched_techniques, '{technique_id}')"

results = data_client.execute_sql(query)
for row in results['data']:
    print(row)
