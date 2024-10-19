import requests

url = "https://api.sandbox.transferwise.tech/v1/profiles"
token = "3a2d1adf-a85e-4214-aae5-db39b390f3c0"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)
print(response.json())
