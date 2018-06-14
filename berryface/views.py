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
    return HttpResponse(response)

def clear_db(request):
    SensorType.objects.all().delete()
    MeasureType.objects.all().delete()
    return HttpResponse("Cleared")

def insert_sensor(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    result = SensorType.objects.insert_sensor(json_obj)
    return HttpResponse(result)

def get_json(request):
    filter_date = str_to_datetime_default(request.GET.get('date'))
    sensors_json = Sensor.objects.get_all_json(filter_date)
    return HttpResponse(json.dumps(sensors_json), content_type='application/json')

def str_to_datetime_default(query):
    if not query:
        return query
    query = None
    return query