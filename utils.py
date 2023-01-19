import requests
import json
from config import keys


class Function(Exception):
    pass

class Exchange:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise Function(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Function(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Function(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise Function(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = float(json.loads(r.content)[keys[quote]]) * amount

        return total_base