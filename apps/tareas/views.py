from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from apps.usuarios.models import Usuario


from .models import Tarea
from .forms import CrearTareaForm


class NuevaTarea(FormView):
    template_name = "tareas/nuevaTarea.html"
    form_class = CrearTareaForm
    success_url = reverse_lazy('ListarTareas')

    def form_valid(self, form):
        tarea = Tarea()
        tarea.titulo = form.cleaned_data['Titulo']
        tarea.descripcion = form.cleaned_data['Descripcion']
        tarea.creada = Usuario.objects.get(username__username = self.request.user.username)
        tarea.prioridad = form.cleaned_data['Prioridad']
        tarea.asignada = form.cleaned_data['Programador']
        tarea.status = ('L', 'Levantada')
        tarea.save()
        return super(NuevaTarea, self).form_valid(form)


class DetalleTarea(DetailView):
    model = Tarea
    template_name = 'tareas/detalleTarea.html'
    context_object_name = 'Tarea'


class ListarTareas(ListView):
    model = Tarea
    template_name = 'tareas/listarTareas.html'
    context_object_name = 'Tareas'


class MisTareas(ListView):
    model = Tarea
    template_name = 'tareas/listarTareas.html'
    context_object_name = 'Tareas'

    def get_queryset(self):
        return Tarea.objects.filter(asignada=self.request.user.pk)


class ModificarTarea(UpdateView):
    model = Tarea
    template_name = 'tareas/modificarTarea.html'
    success_url = reverse_lazy('ListarTareas')
    context_object_name = 'Tarea'


class BorrarTarea(DeleteView):
    model = Tarea
    template_name = 'tareas/borrarTarea.html'
    context_object_name = 'Tarea'
    success_url = reverse_lazy('ListarTareas')