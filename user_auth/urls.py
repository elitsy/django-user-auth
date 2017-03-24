from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    url(r'^login/$', login, name='auth_login'),
    url(r'^logout/$', logout_then_login, name='auth_logout'),
]