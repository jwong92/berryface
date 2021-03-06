from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^view_json/', views.view_json, name="view_json"),
    url(r'^clear_db/', views.clear_db, name="clear_db"),
    #url(r'^insert_sensor/', views.insert_sensor, name="insert_sensor"),
    url(r'^get_json/', views.get_json, name="get_json"),
    url(r'^insert_types/', views.insert_types, name="insert_types"),
    url(r'^add_sensor/', views.add_sensor, name="add_sensor"),
    url(r'^add_entry/', views.add_entry, name="add_entry"),
    url(r'^add_roles/', views.add_roles, name="add_roles"),
    url(r'^add_user/', views.add_user, name="add_user"),
    url(r'^view_token/', views.view_token, name="view_token"),
    url(r'^json_live/', views.json_live, name="json_live"),
]
