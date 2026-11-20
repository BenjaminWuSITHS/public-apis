import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
if not token:
    print("Warning: TOKEN environment variable is missing or empty!")

url = "https://discord.com"
headers = {"Authorization": f"Bot {token}"}

r = requests.get(url, headers=headers)

print("Status Code:", r.status_code)
print("Raw Response:", repr(r.text))

if r.status_code == 200 and r.text.strip():
    try:
        data = r.json()
        print("Bot User Data:", data)
    except requests.exceptions.JSONDecodeError:
        print("Response was not valid JSON.")
else:
    print("Request failed or returned an empty body.")