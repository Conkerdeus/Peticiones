from django.db import models
from apps.usuarios.models import Usuario
from apps.comentarios.models import Comentario


class Tarea(models.Model):
    prioridad_choices = {
            ('1', 'Para ayer'),
            ('2', 'Alta',),
            ('3', 'Normal'),
            ('4', 'Baja')
        }

    status_choices = {
            ('L', 'Levantada'),
            ('P', 'Planeacion'),
            ('D', 'Desarrollo'),
            ('V', 'Verificacion'),
            ('T', 'Terminada')
        }

    titulo = models.CharField(
        max_length=30
    )

    descripcion = models.TextField(
        max_length=200
    )

    creada = models.ForeignKey(
        Usuario, related_name= 'Creada'
    )

    asignada = models.ForeignKey(
        Usuario, related_name= 'Asignada'
    )

    fecha_creacion = models.DateField(
        auto_now_add = True
    )

    status = models.CharField(
        max_length = 3,
        choices = status_choices
    )

    prioridad = models.CharField(
        max_length = 3,
        choices = prioridad_choices
    )

    comentarios = models.ManyToManyField(
        Comentario
    )

    def __unicode__(self):
        return self.titulo


