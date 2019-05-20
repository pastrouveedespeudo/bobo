
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(r'/admin_pollu', views.admin_pollu),
    path(r'/database', views.database),
    path(r'/prédiction', views.prédiction),
    path(r'/remplir_database', views.remplir_database),
]
