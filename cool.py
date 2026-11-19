import requests

url = 'https://discord.com/api'
TOKEN = "MTU1MzkxOTkwMDAzMDk5NjU5MA.Gj1abc.QbV9gHNE1GF99KdFdl68eNpi02MIT9YFjMXxX8"
headers = {
    "Authorization": f"Bot {TOKEN}"
}

r = requests.get(url, headers=headers)


print("Status Code:", r.status_code)
print("Raw Response:", repr(r.text))

# 2. Safely parse JSON only if the request succeeded and has content
if r.status_code == 200 and r.text.strip():
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response was not valid JSON.")
else:
    print("Request failed or returned an empty body.")