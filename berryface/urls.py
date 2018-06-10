from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^view_json/', views.view_json, name="view_json"),
]
