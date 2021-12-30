# How To Create A USSD Application Using Python And Django.

In this article, I will be showing you how to create a USSD application using Python and Django. I will be doing so by building a USSD application that retrieves the price of popular cryptocurrencies in popular fiat currencies, in addition to this, the application will also be able to tell us the current exchange rate of US dollars to few other currencies.

## Prerequisite

- Python
- Basic knowledge of Django

Without futher ado, let us get started.

According to [wikipedia](https://en.wikipedia.org/wiki/Unstructured_Supplementary_Service_Data), USSD stands for Unstructured Supplementary Service Data. It is a communications protocol used by GSM cellular telephones to communicate with the mobile network operator's computers. The computer's response is sent back to the phone, generally in a basic format that can easily be seen on the phone display.

I am going to start by setting up a django project. I am going to run the following commands to create a django project.

- Run `python -m venv ussd_tut` and `.\ussd_tut\scripts\activate` to create and activate virtual environment respectively - where ussd_tut is the name of my virtual environment. For linux, `source ussd_tut/bin/activate` will activate the virtual environment.
- run `pip install django` to install Django.
- In the same folder where I created virtual environment, I will run `django-admin startproject ussd_project` to create a django project.
- After that, I will run `django-admin startapp ussd_app` to create a django app.

On successful creation of the app, I will add the app to the `INSTALLED_APP` variable in my settings.py file so django can recognize it. 

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ussd_app',
]
```

I will be using a [CoinGecko's](https://www.coingecko.com/en) official python [SDK](https://github.com/man-c/pycoingecko) to fetch the price of the cryptocurrencies and for the exchange rate functionality, I will be using [Openexchnagerate](https://openexchangerates.org/api/latest.json) API.

Before I start writing code, I am going to install some libraries like requests (for making HTTP requests), python-dotenv(for handling .env files), and pycoingecko (The SDK I talked about above). So I am going to run `pip install requests python-dotenv pycoingecko` to install these libraries.

In the app folder, I am going to create a file called `crypto_function.py` (You can name yours anything). Inside this file is where I will create the functions to handle the functionalities of the USSD application. In the file, enter the code below

```
import requests
import os
import dotenv
from pycoingecko import CoinGeckoAPI

dotenv.load_dotenv()

def get_cryptocurrency_price(ids, currencies):
    coin_gecko = CoinGeckoAPI()
    price = coin_gecko.get_price(ids=ids, vs_currencies=currencies)
    return price
```

### Explanation: 
I imported the libraries I installed earlier on. `dotenv.load_dotenv()` is to get environment variables from .env file which I will create shortly. After that, I declared a function that retrieves cryptocurrency prices using the pycoingecko SDK and named it `get_cryptocurrency_price`. This function takes in two parameters; the id of the cryptocurrency and the currency we want to check the current price in. The next thing I did was instantiate the `CoinGeckoAPI` class that I imported above so I can access the various cryptocurrency methods including `get_price` method which is used to get the current price of cryptocurrencies in various fiat currencies. `The get_price` method returns a json response of the current price of the cryptocurrency specified in the fiat currency specified. Below is a screenshot of the price of bitcoin in Nigerian Naira

![response screenshot](/sender/bitcoin_response.png)

I am going to use this function in the views file later.

To handle the exchange rate functionality, I am going to create another function just under `get_cryptocurrency_price` function. The code for that function is below:

```
def currency_exchange_rate(base_currency, to_currency):
    url = "https://openexchangerates.org/api/latest.json"
    app_id = os.getenv('app_id')
    response = requests.get(f"{url}/?app_id={app_id}&base={base_currency}&symbols={to_currency}")
    return response.json()['rates'][to_currency]

```

