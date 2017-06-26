from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
        url(r'^$', views.Start, name='start'),
        url(r'^signup/$', views.AddUser, name='signup'),
        url(r'^login/$', views.LoginUser, name='login'),
        url(r'^main/logout$', views.LogoutUser, name='logout'),
        url(r'^main/$', views.Main, name='main'),
        url(r'^main/childadd/$', views.ChildAdd, name='childadd'),
        url(r'^main/parentadd/$', views.ParentAdd, name='parentadd'),
        url(r'^main/child/(?P<pk>\d+)$',views.ChildView, name='childview'),
        url(r'^main/parent/(?P<parent_id>\d+)$',views.ParentView, name='parentview'),
        ]
