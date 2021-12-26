import requests
import os
import dotenv
from pycoingecko import CoinGeckoAPI

dotenv.load_dotenv()

def get_cryptocurrency_price(ids, currencies):
    coin_gecko = CoinGeckoAPI()
    price = coin_gecko.get_price(ids=ids, vs_currencies=currencies)
    return price


def currency_exchange_rate(base_currency, to_currency):

    url = "https://openexchangerates.org/api/latest.json"

    app_id = os.getenv('app_id')

    response = requests.get(f"{url}/?app_id={app_id}&base={base_currency}&symbols={to_currency}")
    return response.json()['rates'][to_currency]

    # 