from django.conf.urls import patterns, include, url
from .views import NuevaTarea, DetalleTarea, ListarTareas, ModificarTarea, BorrarTarea, MisTareas

urlpatterns = patterns('',
    url(r'^NuevaTarea/$', NuevaTarea.as_view() , name='NuevaTarea'),
    url(r'^DetalleTarea/(?P<pk>[\w\d]+)/$', DetalleTarea.as_view(), name='DetalleTarea'),
    url(r'^ListarTareas/$', ListarTareas.as_view(), name='ListarTareas'),
    url(r'^MisTareas/$', MisTareas.as_view(), name='MisTareas'),
    url(r'^ModificarTarea/(?P<pk>[\w-]+)/$',ModificarTarea.as_view(), name='ModificarTarea'),
    url(r'^BorrarTarea/(?P<pk>[\w-]+)/$',BorrarTarea.as_view(), name='BorrarTarea'),
)