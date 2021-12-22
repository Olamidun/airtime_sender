import requests
import os
import dotenv
from .models import AirtimeUser
from pycoingecko import CoinGeckoAPI


coin_gecko = CoinGeckoAPI()

dotenv.load_dotenv()
def fetch_list_of_banks():
    app_id = os.getenv('appid')
    secret_key = os.getenv('production_secret_key')
    print(secret_key)
    headers = {
        "Accept": "text/plain",
        "AppId": app_id,
        "Authorization": secret_key
    }
    # url = f'https://sandbox.dojah.io/api/v1/kyc/phone_number/basic?phone_number={phone_number}'

    url = f'https://api.dojah.io/api/v1/general/banks'
    # payload = {
    #     "amount": amount,
    #     "destination": destination
    # }
    # try:
    response = requests.get(url, headers=headers)
    return {
        'status': True,
        'data': response.text
    }
    # except:
    #     return False


        #     "Accept": "text/plain",
    # "Content-Type": "application/json"


def send_airtime(amount, destination):
    app_id = os.getenv('appid')
    secret_key = os.getenv('production_secret_key')
    print(secret_key)
    headers = {
        "Accept": "text/plain",
        "AppId": app_id,
        "Authorization": secret_key
    }
    # url = f'https://sandbox.dojah.io/api/v1/kyc/phone_number/basic?phone_number={phone_number}'

    url = f'https://api.dojah.io/api/v1/purchase/airtime'
    payload = {
        "amount": amount,
        "destination": destination
    }
    # try:
    response = requests.post(url, headers=headers, json=payload)
    return {
        'status': True,
        'data': response.text
    }


def get_cryptocurrency_price(ids, currencies):
    coin_gecko = CoinGeckoAPI()
    price = coin_gecko.get_price(ids=ids, vs_currencies=currencies)
    return price
