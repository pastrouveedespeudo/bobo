from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'/mode', views.mode),
    path(r'/database_mode', views.database_mode)
 
]
