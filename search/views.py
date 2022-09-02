from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse
from . import coins 
# Create your views here.


def index(request):
    return render(request, 'index.html')


def news(request): 
    if request.method == 'POST':
        crypto = 'POST'
        if crypto == coins[0:]:
            querystring.append([0])
        else: 
            pass 
        url = "https://google-finance4.p.rapidapi.com/ticker/"

        querystring = {"t":"ETH-USD","hl":"en","gl":"US"}

        headers = {
            "X-RapidAPI-Key": "31c5541e87msh0684494d7f7396fp117984jsn574856ff6d0c",
            "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response.status_code
        response.text
        response.json()
        articles = response.json()['news']

       

        return render(request, 'news.html', {
             "article": articles })  
    else:
        return HttpResponse('Error')
