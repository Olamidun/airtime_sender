from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def bank_and_airtime_callback(request):
    if request.method == 'POST':
        session_id = request.POST.get("sessionId", None)
        service_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")

        input = text.split('*')
