from django.shortcuts import render

# Create your views here.
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import SensorType, Sensor, MeasureType, Entry, Role, User

def index(request):
    return HttpResponse("Berry Face Index Page")

def view_json(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    return HttpResponse(response, content_type="application/json")

def clear_db(request):
    SensorType.objects.all().delete()
    MeasureType.objects.all().delete()
    Sensor.objects.all().delete()
    Entry.objects.all().delete()
    return HttpResponse("Cleared")

def insert_types(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    result = SensorType.objects.insert_sensor(json_obj)
    return HttpResponse(result, content_type="application/json")

def get_json(request):
    filter_date = str_to_datetime_default(request.GET.get('date'))
    sensors_json = Sensor.objects.get_all_json(filter_date)
    return HttpResponse(json.dumps(sensors_json), content_type='application/json')

def str_to_datetime_default(query):
    if not query:
        return query
    query = None
    return query

def add_sensor(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    Sensor.objects.add_sensor(json_obj)
    return HttpResponse("All inserted")

def add_entry(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    Entry.objects.add_entry(json_obj)
    return HttpResponse("Entries Added")

def add_roles(request):
    data = json.loads(open("berryface/roles.json").read())
    Role.objects.add_role(data)
    return HttpResponse("Added Roles")

def add_user(request):
    data = json.loads(open("berryface/user.json").read())
    User.objects.insert_user(data)
    return HttpResponse("User Added")

@csrf_exempt
def view_token(request):
    if request.method == "POST":
        # BECUASE I AM PASSING A JSON STRING, I WILL RENDER THE BODY, THEN SERIALIZE THE JSON TO A DICT
        json_str = request.body
        json_dict = json.loads(json_str)
        email = json_dict['user'][0]['email']
        password = json_dict['user'][0]['password']

        # CHECK THE CREDENTIALS
        credentials = User.objects.check_cred_get_token(email, password)
        print credentials
        return HttpResponse(json.dumps(credentials))
        
        # IF USING FORM ENCODED DATA, USE REQUEST.POST AND MAKE SURE THAT THE ENCTYPE IS FORM!
        # json_obj = json.dumps(request.POST)


# Posting JSON in Python without Requests Library

# https://gist.github.com/kennethreitz/1294570