from django.conf.urls import patterns, url
from django.contrib.auth.views import logout_then_login, login
from .views import Index


urlpatterns = patterns('',
    url(r'^$', login, {'template_name': 'inicio/login.html'}, name='login'),
    url(r'^index/$',Index.as_view(), name='index'),
    url(r'^salir/$', logout_then_login, name='logout'),
)


