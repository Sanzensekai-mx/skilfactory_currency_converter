import os
import json

import requests
from dotenv import load_dotenv

load_dotenv(encoding='utf-8')


class ConvertionException(Exception):
    pass


class CurrencyAPI:

    @staticmethod
    def get_price(base, quote, amount):
        valute_names = CurrencyAPI.valute_dict()
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        if not valute_names.get(quote):
            raise ConvertionException(f'Не удалось найти валюту {quote} среди поддерживаемых.')

        if not valute_names.get(base):
            raise ConvertionException(f'Не удалось найти валюту {base} среди поддерживаемых.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалость обработать количество валюты: {amount}')

        api_url = 'https://api.apilayer.com/currency_data/convert'
        headers = {
            "apikey": str(os.getenv("API_KEY"))
        }
        params = {'to': quote, 'from': base, 'amount': amount}
        cur_request = requests.request('GET', url=api_url, headers=headers, params=params)
        price = json.loads(cur_request.text)['result']
        return price

    @staticmethod
    def valute_dict():
        with open('currencies_list.json', 'r', encoding='utf-8') as json_file:
            valute_name = json.load(json_file)
        return valute_name
