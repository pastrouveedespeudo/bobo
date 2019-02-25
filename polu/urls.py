from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    
    path(r'', views.home),
    path(r'/photo', include('photo.urls')),
    path(r'/polution', views.polution),
]
