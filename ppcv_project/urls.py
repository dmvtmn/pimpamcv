from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ppcv_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^review/$', include('ppcv.urls')),
    url(r'^cart/$','checkout.views.view', name='cart'),
    url(r'^$', 'ppcv_project.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG: #setting media url
    urlpatterns += patterns(
    'django.views.static',
    (r'^media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )
