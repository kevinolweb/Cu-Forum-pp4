
from django.contrib import admin
from django.urls import path,include
from .views import hello

urlpatterns = [
    path('/home',hello,name="home"),
]
