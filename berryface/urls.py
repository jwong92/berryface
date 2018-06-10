from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^view_json/', views.view_json, name="view_json"),
    url(r'^clear_db/', views.clear_db, name="clear_db"),
    url(r'^insert_sensor/', views.insert_sensor, name="insert_sensor"),
]
