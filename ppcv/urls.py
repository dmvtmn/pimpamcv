from django.conf.urls import patterns, url
from ppcv import views

urlpatterns = patterns('',
        url(r'^$', views.usr_home, name='usr_home'))
