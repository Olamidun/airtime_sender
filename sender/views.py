from django.shortcuts import render, HttpResponse
from airtime_sender import get_cryptocurrency_price

# Create your views here.

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
            response += "2. To check the list of 10 nigerian banks\n"
            return HttpResponse(response)
        if len(input) == 1:
            if input[0] == "1":
                response = "CON Choose the cryptocurrency whose price you want to know\n"
                response += "1. bitcoin\n"
                response += "2. ethereum\n"
                response += "3. litecoin\n"
                response += "4. shiba-INU\n"
                response += "5. BNB" # id = binancecoin
                return HttpResponse(response)
            elif input[0] == "2":
                pass
            else:
                response = "END Invalid input. Must either be 1 or 2."
                return HttpResponse(response)
        elif len(input) == 2:
            if input[0] == "1":
                possible_input = ['1', '2', '3', '4', '5']
                if input[1] in possible_input:
                    response = "CON Choose the currency in which you want to know how much your choose cryptocurrency costs\n"
                    response += "1. Nigerian Naira (NGN)"
                    response += "2. US Dollars (USD)"
                    response += "3. Euro (EUR)"
                else:
                    response = "END. Invalid input. Please try again"
            elif input[0] == "2":
                pass
        elif len(input) == 3:
            if input[0] == "1":
                if input[1] == "1":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('bitcoin', 'ngn')
                        response = f"END Current price of Bitcoin in Nigerian Naira is {result['bitcoin']['ngn']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('bitcoin', 'usd')
                        response = f"END Current price of Bitcoin in US Dollars is {result['bitcoin']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('bitcoin', 'eur')
                        response = f"END Current price of Bitcoin in Euro is {result['bitcoin']['eur']}"
                        return HttpResponse(response)
                elif input[1] == "2":
                    if input[2] == "1":
                        result = get_cryptocurrency_price('ethereum', 'ngn')
                        response = f"END Current price of Ethereum in Nigerian Naira is {result['bitcoin']['ngn']}"
                        return HttpResponse(response)
                    elif input[2] == "2":
                        result = get_cryptocurrency_price('ethereum', 'usd')
                        response = f"END Current price of Ethereum in US Dollars is {result['bitcoin']['usd']}"
                        return HttpResponse(response)
                    elif input[2] == "3":
                        result = get_cryptocurrency_price('ethereum', 'eur')
                        response = f"END Current price of Ethereum in Euro is {result['bitcoin']['eur']}"
                        return HttpResponse(response)

        return HttpResponse(response)
