
from django.contrib import admin
from django.urls import path,include
from .views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/home',hello,name="home"),
]
