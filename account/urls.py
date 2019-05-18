from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'/login', views.login_view),
    path(r'/register_view', views.register_view),
    path(r'/logout_view', views.logout_view),

   
]
