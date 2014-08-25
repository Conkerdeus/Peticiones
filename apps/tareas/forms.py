from django import forms
from apps.usuarios.models import Usuario
from .models import Tarea


class CrearTareaForm(forms.Form):

    Titulo = forms.CharField(
        label='Titulo de la Tarea',
        max_length=30
    )

    Descripcion = forms.CharField(
        label='Descripcion',
        widget=forms.Textarea()
    )

    Programador = forms.ModelChoiceField(
        label='Programador Asignado',
        queryset = Usuario.objects.filter(
            es_programador=True)
    )

    Prioridad = forms.CharField(
        label = 'Prioridad de la Tarea',
        widget = forms.Select(
            choices = Tarea.prioridad_choices
        )
    )

    class Meta:
        model = Tarea





