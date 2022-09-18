from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse
import json 

# Create your views here.

coins = {
    "Ethereum": "ETH-USD",
    "Bitcoin": "BIT-USD", 
    "Litcoin": "LIT-USD", 
    "Solona": "SOL-USD", 
    "Binance": "BNB-USD", 
    "Ripple": "XRP-USD", 
    "XRP": "XRP-USD", 
    "Cardano": "ADA-USD", 
    "Dogeoin": "DOGE-USD", 
    "Chainlink": "LINK-USD" }

def index(request):
    return render(request, 'index.html')


def news(request): 
    if request.method == 'POST':
       
        url = "https://google-finance4.p.rapidapi.com/ticker/"

        querystring = {"t":"ETH-USD","hl":"en","gl":"US"}


        headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": "US",
            "X-RapidAPI-Key": "31c5541e87msh0684494d7f7396fp117984jsn574856ff6d0c",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
        }


        response = requests.request("GET", url, headers=headers)
        result = response.json()['entries']
        return render(request, 'news.html', {
            "article": result })  
