from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
        url(r'^$', views.AddUser, name='singup'),
        url(r'^main/$', views.Main, name='main'),
        ]
