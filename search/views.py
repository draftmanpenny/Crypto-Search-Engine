from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import TemplateView
# Create your views here.


def index(requests):
    return render(requests, 'index.html')


#def news(requests): 
    #if requests == 'POST': 
        #requests.get()