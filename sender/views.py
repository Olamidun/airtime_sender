from django.shortcuts import HttpResponse
from .crypto_function import  currency_exchange_rate, get_cryptocurrency_price
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def crypto_ussd_callback(request):
    # if
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
        if len(input) == 1:
            if input[0] == "1":
                response = "CON Choose the cryptocurrency whose price you want to know\n"
                response += "1. bitcoin\n"
                response += "2. ethereum\n"
                response += "3. litecoin\n"
                response += "4. shiba-INU\n" # confirm the id to be shiba-INU
                response += "5. BNB" # id = binancecoin
                return HttpResponse(response)
            elif input[0] == "2":
                response += "CON Choose the currency whose exchange rate you want to know.\n"
                response += "1. US Dollars USD\n"
                return HttpResponse(response)
            else:
                response = "END Invalid input. Must either be 1 or 2."
                return HttpResponse(response)
        elif len(input) == 2:
            if input[0] == "1":
                possible_input = ['1', '2', '3', '4', '5']
                if input[1] in possible_input:
                    response = "CON Choose the currency in which you want to know how much your chosen cryptocurrency costs\n"
                    response += "1. Nigerian Naira (NGN)\n"
                    response += "2. US Dollars (USD)\n"
                    response += "3. Euro (EUR)\n"
                else:
                    response = "END. Invalid input. Please try again"
                    return HttpResponse(response)
            elif input[0] == "2":
                possible_input = ['1', '2', '3', '4']
                
                if input[1] in possible_input:
                    response = "CON Choose the currency\n" # gotta find better word for this
                    response += "1. Nigerian Naira (NGN)\n"
                    response += "2. US Dollars (USD)\n"
                    response += "3. Euro (EUR)\n"
                    return HttpResponse(response)
                else:
                    response = "END. Invalid input. Please try again"
                    return HttpResponse(response)
        elif len(input) == 3:
            if input[0] == "1":
                # BITCOIN
                if input[1] == "1":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('bitcoin', 'ngn')
                        response = f"END Current price of Bitcoin in US Dollars is {result['bitcoin']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('bitcoin', 'usd')
                        response = f"END Current price of Bitcoin in US Dollars is {result['bitcoin']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('bitcoin', 'eur')
                        response = f"END Current price of Bitcoin in Euro is {result['bitcoin']['eur']}"
                        return HttpResponse(response)
                # ETHEREUM
                elif input[1] == "2":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('ethereum', 'ngn')
                        response = f"END Current price of Ethereum in Nigerian Naira is {result['ethereum']['ngn']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('ethereum', 'usd')
                        response = f"END Current price of Ethereum in US Dollars is {result['ethereum']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('ethereum', 'eur')
                        response = f"END Current price of Ethereum in Euro is {result['ethereum']['eur']}"
                        return HttpResponse(response)
                # LITECOIN
                elif input[1] == "3":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('litecoin', 'ngn')
                        response = f"END Current price of LiteCoin in Nigerian Naira is {result['litecoin']['ngn']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('litecoin', 'usd')
                        response = f"END Current price of litecoin in US Dollars is {result['litecoin']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('litecoin', 'eur')
                        response = f"END Current price of litecoin in Euro is {result['litecoin']['eur']}"
                        return HttpResponse(response)
                # SHIBA-INU
                elif input[1] == "4":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('shiba-INU', 'ngn')
                        response = f"END Current price of Shiba-INU in Nigerian Naira is {result['shiba-inu']['ngn']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('shiba-INU', 'usd')
                        response = f"END Current price of Shiba-INU in US Dollars is {result['shiba-inu']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('shiba-INU', 'eur')
                        response = f"END Current price of Shiba-INU in Euro is {result['shiba-inu']['eur']}"
                        return HttpResponse(response)
                # BNB
                elif input[1] == "5":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('binancecoin', 'ngn')
                        response = f"END Current price of BNB in Nigerian Naira is {result['binancecoin']['ngn']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('binancecoin', 'usd')
                        response = f"END Current price of BNB in US Dollars is {result['binancecoin']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('binancecoin', 'eur')
                        response = f"END Current price of BNB in Euro is {result['binancecoin']['eur']}"
                        return HttpResponse(response)
                    else:
                        response = "END Invalid input. Please try again"
                        return HttpResponse(response)
                else:
                    response = "END Invalid input. Please try again"
                    return HttpResponse(response)
            elif input[0] == "2":
                if input[1] == "1":
                    if input[2] == "1":
                        result = currency_exchange_rate("USD", "NGN")
                        response = f"END The current exchange rate of 1 US Dollars to Nigerian Naira is {result}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        response = f"END You are checking exchange rate of USD to USD"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = currency_exchange_rate("USD", "EUR")
                        response = f"END The current exchange rate of 1 US Dollars to Euro is {result} "
                        return HttpResponse(response)
                    else:
                        response = "END Invalid input"
                        return HttpResponse(response)
                else:
                    response = "END Invalid input"
                    return HttpResponse(response)
            else:
                response = "END Invalid input. Please try again."
                return HttpResponse(response)
        return HttpResponse(response)
