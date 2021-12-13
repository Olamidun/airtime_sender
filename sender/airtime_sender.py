import requests
import os
import dotenv
from .models import AirtimeUser



dotenv.load_dotenv()
def send_airtime(phone_number, amount, destination):
    app_id = os.getenv('appid')
    secret_key = os.getenv('test_private_key')
    headers  = {
        'Accept': 'text/plain',
        'Authorization': secret_key,
        'AppId': app_id,
        'Content-Type': 'application/json',
    }
    url = 'https://sandbox.dojah.io/api/v1/purchase/airtime'
    payload = {
        "amount": amount,
        "destination": destination
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        return {
            'status': True,
            'data': response.json()
        }
    except:
        return False


        #     "Accept": "text/plain",
    # "Content-Type": "application/json"