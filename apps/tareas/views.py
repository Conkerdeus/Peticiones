from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail, EmailMultiAlternatives
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

        if tarea.prioridad == 'Para ayer':
            tarea.orden_prioridad = 'A'
            tarea.color_prioridad = 'danger'
        elif tarea.prioridad == 'Alta':
            tarea.orden_prioridad = 'B'
            tarea.color_prioridad = 'warning'
        elif tarea.prioridad == 'Normal':
            tarea.orden_prioridad = 'C'
            tarea.color_prioridad = 'success'
        elif tarea.prioridad == 'Baja':
            tarea.orden_prioridad = 'D'
            tarea.color_prioridad = 'info'

        tarea.asignada = form.cleaned_data['Programador']
        tarea.status = 'Levantada'
        tarea.save()
        asunto = "Te asignaron una nueva tarea"
        de = 'Sistema de peticiones <peticiones@redmagisterial.com'
        destinatario = Usuario.objects.get(pk=tarea.asignada._get_pk_val())
        msgtxt = ''
        msghtml = '<strong>Hola ' + destinatario.username.first_name + ':</strong> <br><br>' + \
                  'Te asignaron una nueva tarea: <br> ' + \
                  'Titulo: ' + tarea.titulo +  "<br>" + \
                  'Descripcion: ' + tarea.descripcion + '<br>' + \
                  'Prioridad: ' + tarea.prioridad + '<br>' + \
                  '<br><br> Da click <a href="http://127.0.0.1:8000">aqui</a> para revisarla'

        msg = EmailMultiAlternatives(asunto, msgtxt, de, [destinatario.username.email])
        msg.attach_alternative(msghtml, "text/html")
        msg.send()
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
    template_name = 'tareas/misTareas.html'
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