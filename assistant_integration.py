from ibm_watsonxdata import DataClient

API_KEY = "YOUR_WATSONX_API_KEY"
URL = "YOUR_WATSONX_URL"

data_client = DataClient(api_key=API_KEY, url=URL)

# Example: query logs for a specific technique
technique_id = "T1059"
query = f"SELECT * FROM mitre_logs WHERE ARRAY_CONTAINS(matched_techniques, '{technique_id}')"

results = data_client.execute_sql(query)
for row in results['data']:
    print(row)
