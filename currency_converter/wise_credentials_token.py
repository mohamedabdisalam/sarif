import requests
from requests.auth import HTTPBasicAuth

url_credentials = "https://api.sandbox.transferwise.tech/oauth/token"
client_id = "mohamed.abdisalam@gmail.com"
client_secret = "znq*zxy6KHR*jpe4tnf"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "grant_type": "client_credentials"
}

response = requests.post(
    url_credentials,
    auth=HTTPBasicAuth(client_id, client_secret),
    headers=headers,
    data=data
)

print(response.status_code)
# print(response.json())
