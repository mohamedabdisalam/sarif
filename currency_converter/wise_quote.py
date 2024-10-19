import requests
import json

profile_id = 19555947

url_quotes = f"https://api.sandbox.transferwise.tech/v3/quotes"
token = "3a2d1adf-a85e-4214-aae5-db39b390f3c0"

headers = {
    'Authorization': f'Bearer {token}',
    "Content-Type": "application/json"
}

# sourceCurrency = str(input("Enter in the currency you'd like to convert from: ")).upper()
# targetCurrency = str(input("Enter in the currency you'd like to convert to: ")).upper()
# sourceAmount = float(input("Enter the amount you'd like to convert: "))

payload = {
    "sourceCurrency": "GBP",
    "targetCurrency": "USD",
    "sourceAmount": None,
    "targetAmount": 100,
    "payOut": None,
    "preferredPayIn": None,
    "targetAccount": None,
    "paymentMetadata": {
        "transferNature": "MOVING_MONEY_BETWEEN_OWN_ACCOUNTS"
    }
}


response = requests.post(
    url_quotes,
    headers=headers,
    data=json.dumps(payload)
)

# response_data = response.json().option.price.total

sourceAmount = response.json()['paymentOptions'][0]['sourceAmount']
wise_fees = response.json()['paymentOptions'][0]['fee']['total']
targetAmount = response.json()['paymentOptions'][0]['targetAmount']
rate = response.json()['rate']
total = targetAmount / rate
print(sourceAmount)
print(wise_fees)
print(total)





