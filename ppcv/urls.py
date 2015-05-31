from django.conf.urls import patterns, url
from ppcv import views

urlpatterns = patterns('',
        url(r'^(?P<slug>[\w-]+)/$', views.single , name='single_service'),
        #(?P<slug>.*)
        url(r'^$', views.usr_home , name='usr_home'),
)
