
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.home),
    path(r'photo', include('photo.urls')),
    path(r'polution', include('polution.urls')),
    path(r'accounts', include('accounts.urls')),
    path(r'administrateur', include('administrateur.urls')),
    path(r'admin_pollu', include('admin_pollu.urls')),
    
]
