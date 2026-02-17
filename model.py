import os
from dotenv import load_dotenv
import requests

load_dotenv()  # loads .env into environment variables

url = os.getenv("ENDPOINT_URL")
token = os.getenv("JSON_API_TOKEN")
print(token)

headers = {"Authorization": f"Bearer {token}"}

r = requests.get(url, headers=headers)

get_data = r.json()