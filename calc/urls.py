from django.urls import path

from . import views

urlpatterns = [
    path('get_name',views.get_name, name = "get_name"),
    path('about', views.about, name = "about"),
    path('',views.get_name, name = "get_name"),
]