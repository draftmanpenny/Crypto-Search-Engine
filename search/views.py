from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def news(request, article): 
    if request.method == 'POST':
        url = "https://google-finance4.p.rapidapi.com/search/"

        querystring = {"q":"airbnb","hl":"en","gl":"US"}

        headers = {
            "X-RapidAPI-Key": "31c5541e87msh0684494d7f7396fp117984jsn574856ff6d0c",
            "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

       

        return render(request, 'news.html')
             "article": response 
    else:
        return HttpResponse('Error')
