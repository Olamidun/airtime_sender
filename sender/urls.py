from . import views
from django.urls import path


app_name = 'sender'

urlpatterns = [
    path('callback', views.crypto_ussd_callback, name='callback')
]