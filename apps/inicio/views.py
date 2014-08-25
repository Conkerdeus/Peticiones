from django.shortcuts import render_to_response
from django.views.generic import ListView
from apps.tareas.models import Tarea

# Create your views here.

class Index(ListView):
    model = Tarea
    template_name = 'inicio/index.html'
    context_object_name = 'Tareas'
