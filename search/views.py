from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse

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
        querystring = {"t":" ","hl":"en","gl":"US"}
        url = "https://google-finance4.p.rapidapi.com/ticker/"
        headers = {
            "X-RapidAPI-Key": "31c5541e87msh0684494d7f7396fp117984jsn574856ff6d0c",
            "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }
        crypto = request.POST["search"]
        if crypto not in coins:
            querystring["t"] = crypto
            response = requests.request("GET", url, headers=headers, params=querystring)
            response.status_code
            response.text
            response.json()
            articles = response.json()['news']

            return render(request, 'news.html', {
                "article": articles })  
        else:
            return HttpResponse('<h1> Error </h1>')
