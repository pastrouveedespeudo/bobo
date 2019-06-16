from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    
    path(r'', views.home),
    path(r'/photo', include('photo.urls')),
    path(r'/polution', views.polution),
    path(r'/graphe', views.graphe),
    path(r'/donnée', views.donnée),
    path(r'/machine_a_o', views.machine_a_o),
    path(r'/prediction', views.prediction),
    path(r'/info_pollu', views.info_pollu),

    
]
