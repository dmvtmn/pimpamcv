from django.conf.urls import patterns, url
from ppcv import views

urlpatterns = patterns('',
        url(r'^(?P<slug>.*)/$', views.single , name='single_service'),
        url(r'^$', views.usr_home , name='usr_home'),
)
