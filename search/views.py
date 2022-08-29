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
        search = requests.Post
        requests.get('https://www.youtube.com/results?search_query=' + search)
        return render(requests, 'news.html', )
    else:
        return HttpResponse('Error')