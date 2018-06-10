from django.shortcuts import render

# Create your views here.
import requests
import json
from django.http import HttpResponse
from .models import SensorType, Sensor, MeasureType, Entry

def index(request):
    return HttpResponse("Berry Face Index Page")

def view_json(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    return HttpResponse(json_obj)

def clear_db(request):
    SensorType.objects.all().delete()
    MeasureType.objects.all().delete()
    return HttpResponse("Cleared")

def insert_sensor(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    result = SensorType.objects.insert_sensor(json_obj)
    return HttpResponse(result)