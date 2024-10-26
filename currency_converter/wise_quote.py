import requests
import json
from typing import Dict, Union
import logging

logging.basicConfig(level=logging.DEBUG)
def get_wise_quote(source_currency: str, target_currency: str, target_amount: float) -> Dict[str, Union[float, str]]:
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
        "sourceAmount": None,
        "targetAmount": target_amount,
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
        source_amount = response_data['paymentOptions'][0]['sourceAmount']
        wise_fees = response_data['paymentOptions'][0]['fee']['total']
        target_amount = response_data['paymentOptions'][0]['targetAmount']
        rate = response_data['rate']
        total_cost = target_amount / rate

        return {
            'sourceAmount': source_amount,
            'wise_fees': wise_fees,
            'targetAmount': target_amount,
            'rate': rate,
        }
    else:
        #Handle error case
        try:
            error_message = response.json()
        except ValueError:
            error_message = response.text
        logging.error(f"Error: {error_message}")
        return {'error': error_message}

        # print(f"Source amount: {sourceAmount}")
        # print(f"Wise fees: {wise_fees}")
        # print(f"Tota cost with fees: {total}")





