import os
import json

import requests
from dotenv import load_dotenv

load_dotenv(encoding='utf-8')


class CurrencyAPI:

    @staticmethod
    def get_price(base, quote, amount):
        api_url = 'https://api.apilayer.com/currency_data/convert'
        headers = {
            "apikey": str(os.getenv("API_KEY"))
        }
        params = {'to': base, 'from': quote, 'amount': amount}
        cur_request = requests.request('GET', url=api_url, headers=headers, params=params)
        price = json.loads(cur_request.text)['result']
        return price
