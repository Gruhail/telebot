import json
import requests
from test import API_KEY
from test import keys

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIException("Неверное количество параметров")
        quote, base, amount = values
        if quote == base:
            raise APIException(f"Вы ввели одинаковые валюты: {base}")
        try:
            quote_formated = keys[quote]
        except KeyError:
            raise APIException(f"Такая валюта не поддерживается: {quote}")
        try:
            base_formated = keys[base]
        except KeyError:
            raise APIException(f"Такая валюта не поддерживается: {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не корректно введено количество валюты: {amount}")

        query = str(quote_formated + "_" + base_formated)
        html = requests.get(f'https://free.currconv.com/api/v7/convert?q={query}&compact=ultra&apiKey={API_KEY}')

        result = (json.loads(html.content)[query]) * amount

        return round(result, 2)
