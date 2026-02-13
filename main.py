from dotenv import load_dotenv
import os
import requests

load_dotenv()  # loads .env into environment variables

url = "https://api.json-generator.com/templates/2ireVV0w37TX/data"
token = os.getenv("JSON_API_TOKEN")
print(token)

headers = {"Authorization": f"Bearer {token}"}
print("HEADER SENT:", headers)

r = requests.get(url, headers=headers)
print(r.status_code)
print(r.json())