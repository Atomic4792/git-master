from dotenv import load_dotenv
from rich import print_json
import os
import requests

load_dotenv()  # loads .env into environment variables

url = os.getenv("ENDPOINT_URL")
token = os.getenv("JSON_API_TOKEN")
print(token)

headers = {"Authorization": f"Bearer {token}"}

r = requests.get(url, headers=headers)
print(r.status_code)
print_json(data = r.json())