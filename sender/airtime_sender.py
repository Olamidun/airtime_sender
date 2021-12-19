import requests
import os
import dotenv
from .models import AirtimeUser



dotenv.load_dotenv()
def fetch_list_of_banks():
    app_id = os.getenv('appid')
    secret_key = os.getenv('production_secret_key')
    print(secret_key)
    headers = {
        "Accept": "text/plain",
        "AppId": "5fc144c4318b66003e7644c2",
        "Authorization": "prod_sk_O5ZaI2rKmA1u4niXtJWUeJsoQ"
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