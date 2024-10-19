import requests

sourceCurrency = str(
    input("Enter in the currency you'd like to convert from: ")
).upper()

targetCurrency = str(
    input("Enter in the currency you'd like to convert to: ")
).upper()

targetAmount = float(input("Enter the amount you'd like to convert: "))

url_rates = f"https://api.sandbox.transferwise.tech/v1/rates?source={sourceCurrency}&target={targetCurrency}"
url_quotes = f"https://api.sandbox.transferwise.tech/v3/quotes/"
url_credentials = f"https://api.sandbox.transferwise.tech/oauth/token"
token = "3a2d1adf-a85e-4214-aae5-db39b390f3c0"

headers = {f'Authorization': 'Bearer {token}'.format(token=token)}
content_type = {'Content-type': 'application/json'}
client_id = {'mohamed.abdisalam@gmail.com': 'znq*zxy6KHR*jpe4tnf'}


# response = requests.get(url_quotes, headers=headers)
# response = (requests.post(url_quotes, content_type, headers=headers))
response = requests.post(url_credentials, client_id, 'grant_type=client_credentials')

print(response.status_code)
# print(response.json())
# print(f"{targetAmount} {sourceCurrency} is {response.json()['quotes'][targetCurrency]}{targetCurrency}")
