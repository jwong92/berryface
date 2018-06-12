from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^view_json/', views.view_json, name="view_json"),
    url(r'^clear_db/', views.clear_db, name="clear_db"),
    url(r'^insert_types/', views.insert_types, name="insert_types"),
    url(r'^add_sensor/', views.add_sensor, name="add_sensor"),
    url(r'^add_entry/', views.add_entry, name="add_entry"),
]