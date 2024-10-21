import requests
import json
from typing import Dict, Union
import logging

logging.basicConfig(level=logging.DEBUG)
def get_wise_quote(source_currency: str, target_currency: str, source_amount: float) -> Dict[str, Union[float, str]]:
    profile_id = 19555947
    url_quotes = f"https://api.sandbox.transferwise.tech/v3/quotes"
    token = "3a2d1adf-a85e-4214-aae5-db39b390f3c0"

    headers = {
        'Authorization': f'Bearer {token}',
        "Content-Type": "application/json"
    }
    payload = {
        "sourceCurrency": source_currency,
        "targetCurrency": target_currency,
        "sourceAmount": source_amount,
        "targetAmount": None,
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
    if response.status_code == 200:
        response_data = response.json()
        logging.basicConfig(level=logging.DEBUG)
        source_amount = response.json()['paymentOptions'][0]['sourceAmount']
        wise_fees = response.json()['paymentOptions'][0]['fee']['total']
        target_amount = response.json()['paymentOptions'][0]['targetAmount']
        rate = response.json()['rate']
        total = target_amount / rate

        return {
            'sourceAmount': source_amount,
            'wise_fees': wise_fees,
            'targetAmount': target_amount,
            'rate': rate,
        }
    else:
        #Handle error case
        logging.error(f"Error: {response.json()}")
        return {'error': response.json()}

        # print(f"Source amount: {sourceAmount}")
        # print(f"Wise fees: {wise_fees}")
        # print(f"Tota cost with fees: {total}")





