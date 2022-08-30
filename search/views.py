from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


def index(requests):
    return render(requests, 'index.html')


def news(requests): 
    if requests.method == 'POST':
        url = "https://google-finance4.p.rapidapi.com/search/"

        querystring = {"q":"airbnb","hl":"en","gl":"US"}

        headers = {
            "X-RapidAPI-Key": "31c5541e87msh0684494d7f7396fp117984jsn574856ff6d0c",
            "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

        return render(requests, 'news.html')
    else:
        return HttpResponse('Error')