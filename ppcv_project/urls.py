from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ppcv_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^review/', include('ppcv.urls')),
    url(r'^cart/$','checkout.views.view', name='cart'),
    url(r'^checkout/$','checkout.views.checkout', name='checkout'),
    url(r'^orders/$','checkout.views.orders', name='user_orders'),
    url(r'^cart/(?P<slug>[\w-]+)/$','checkout.views.update_cart', name='update_cart'),
    url(r'^$', 'ppcv_project.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name = 'auth_logout'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name = 'auth_login'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name = 'auth_register'),
)

if settings.DEBUG: #setting media url
    urlpatterns += patterns(
    'django.views.static',
    (r'^media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )
