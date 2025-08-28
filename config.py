from ibm_watsonxdata import DataClient
from ibm_watsonx_ai import AIClient

API_KEY = "3d6AlqLJWWtZHceoa5XkDmCA3ctqxcqSkobFV8X9wLds"
URL = "https://eu-de.dataplatform.cloud.ibm.com/projects/73c3e5ed-164f-4676-b5b1-eed6307148cd?context=wx"

# Initialize data client
data_client = DataClient(api_key=API_KEY, url=URL)

# Initialize AI client
ai_client = AIClient(api_key=API_KEY, url=URL)