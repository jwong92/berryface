from django.shortcuts import render

# Create your views here.
import requests
import json
from django.http import HttpResponse

def index(request):
    return HttpResponse("Berry Face Index Page")


def view_json(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    return HttpResponse(json_obj)
