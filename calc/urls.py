from django.urls import path

from . import views

urlpatterns = [
    path('aa',views.home, name = 'home'),
    path('add',views.add, name = 'add'),
    path('get_name',views.get_name, name = "get_name"),
    path('',views.get_name, name = "get_name"),
]