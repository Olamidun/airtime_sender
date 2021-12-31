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

### Explanation:

The function takes in base_currency and to_currency as parameters, i.e If you want to know the exchange rate of US dollars to Nigerian naira, US dollars is the base_currency and Nigerian Naira is the to_currency. Because I am using the free version of the API, only USD is allowed to be the base_currency.
Like I said, I will be using openexchangerates API for this functionality. The endpoint to get the exchange rate is assigned to the `url` variable. The API requires an application ID (You can get yours by creating an account with openexchangerates) when making a request, since my app ID is a sensitive information and I do not want anybody else to know about it, I have saved it in a .env file and retrieved it with `os.getenv('app_id)`. This .env file will be created shortly.
To make HTTP request to openexchangerate's API, I used the requests library that I installed earlier on, since the HTTP request to get exchange rate for currency is a GET request, I am using `requests.get()` and passing the base url along with the my app ID, base_currency and to_currency as query parameters. The response of the HTTP request to the API is a json response, so I extracted the value of the the exchange rate with `response.json()['rates'][to_currency]`. This will also be used in the views file.

Before I proceed, I will create my .env file by simply going into my project root directory and create a file named ".env", it is important the file is named ".env", else it won't work. After creating, copy your app ID on openexchangerate and paste it into the .env file. Your file should look like in the picture below:

![env screenshot](/sender/env-screenshot.png)

The redacted part is the value of your app ID.

Now, I am going to write the code for the USSD feature, to do this, I will be using a platform called [africastalking](https://africastalking.com/). Go to africastalking and create an account, after creating an account click on the sandbox button on your dashboard and then click on the USSD option in the side menu bar, subsequently click on create channel in the drop down, and click on "create channel". In the channel field in the form that will be displayed, I am going to enter any number to be my USSD code (In your own case, your preferred code might not be available, africastalking will suggest some for you.), after that I am going to fill in the Callback URL field with a random url (I will change this later, and I am going to tell you why) as it is a required field, click create channel and we can start writing the code to make use of africastalking USSD feature.

Let me briefly explain how the USSD feature on africastalking works. When I dial my code say * 384*09#, and africastalking server receives the request, a HTTP POST request is sent to the callback URL I specified, this callback URL will respond with a response or "menu" which is basically options that the users can choose from, of course I am going to show you how to build out these menus. The menus in my case are just questions I ask the user to know what they want to do on the USSD application. When africastalking makes a POST request to the callback specified, they send some parameters along with it, these parameters are: 
- sessionID (string): A unique value generated when the session starts and sent every time a mobile subscriber response has been received. This means USSD is session based, i.e whatever you are doing ends when you exit or press "cancel".
- phoneNumber (string): The number of the mobile subscriber interacting with your ussd application.

- networkCode (string): The telecomunication company of the phoneNumber interacting with the ussd application.
- serviceCode (string): This is the USSD code assigned to your application
- text (string): This shows the user input. It is an empty string in the first notification of a session. After that, it concatenates all the user input within the session with a * until the session ends.

Now I am going to start building out the menus/response. I will do so in bits so I can explain the code:

```
from django.shortcuts import HttpResponse
from .crypto_function import  currency_exchange_rate, get_cryptocurrency_price
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def crypto_ussd_callback(request):
    if request.method == 'POST':
        session_id = request.POST.get("sessionId", None)
        service_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")

        input = text.split('*')

        response = ""
        if text == '':
            response = "CON Welcome, kindly choose what you want to do\n"
            response += "1. To check price of cryptocurrency in your preferred currency\n"
            response += "2. To check the exchange rate of your currency with other currencies\n"
            return HttpResponse(response)
```

## Explanation:

The first three import lines are to import the things I need. The functions I created in `crypto_function.py` file, `csrf_exempt` decorator to bypass CSRF security mechanism Django provides, and HttpResponse.

Since africastalking sends a POST request to the callback URL I supplied, and the view associated with the callback URL is the one I am working on, I have to check if the request coming in is a POST request so I will be able to get the POST parameters sent along with the request