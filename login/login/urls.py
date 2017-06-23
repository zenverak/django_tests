from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
        url(r'^$', views.AddUser, name='signup'),
        url(r'^main/$', views.Main, name='main'),
        url(r'^main/childadd/$', views.ChildAdd, name='childadd'),
        url(r'^main/parentadd/$', views.ParentAdd, name='parentadd'),
        url(r'',view),
        ]
