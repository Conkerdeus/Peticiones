from django.db import models
from apps.usuarios.models import Usuario
from apps.comentarios.models import Comentario


class Tarea(models.Model):
    prioridad_choices = {
            ('Para ayer', 'Para ayer'),
            ('Alta', 'Alta',),
            ('Normal', 'Normal'),
            ('Baja', 'Baja')
        }

    status_choices = {
            ('Aceptada', 'Aceptada'),
            ('En planeacion', 'Planeacion'),
            ('Desarrollando', 'Desarrollo'),
            ('En verificacion de errores', 'Verificacion'),
            ('Terminada', 'Terminada')
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
        max_length = 15,
        choices = status_choices
    )

    prioridad = models.CharField(
        max_length = 15,
        choices = prioridad_choices
    )

    color_prioridad = models.CharField(
        max_length = 15,
        null = True
    )

    orden_prioridad = models.CharField(
        null = True,
        max_length=1
    )


    comentarios = models.ManyToManyField(
        Comentario
    )

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ["orden_prioridad"]


