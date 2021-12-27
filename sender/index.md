# How To Create A USSD Application Using Python And Django.

In this article, I will be showing you how to create a USSD application using Python and Django. I will be doing so by building a USSD application that retrieves the price of popular cryptocurrencies in popular fiat currencies, in addition to this, the USSD will be able to tell us the current exchange rate of US dollars to few other currencies.

## Prerequisite

- Python
- Basic knowledge of Django

Without futher ado, let us get started.

According to [wikipedia](https://en.wikipedia.org/wiki/Unstructured_Supplementary_Service_Data), USSD stands for Unstructured Supplementary Service Data. It is a communications protocol used by GSM cellular telephones to communicate with the mobile network operator's computers. The computer's response is sent back to the phone, generally in a basic format that can easily be seen on the phone display.

I am going to start by creating a django project. I am going to run the following commands to create a django project.

- Run `python -m venv ussd_tut` and `.\ussd_tut\scripts\activate` to create and activate virtual environment respectively - where ussd_tut is the name of my virtual environment. For linux, `source ussd_tut/bin/activate` will activate the virtual environment
- In the same folder where I created virtual environment, I will run `django-admin startproject ussd_project` to create a django project.
- After that, I will run `django-admin startapp ussd_app` to create a django app.

