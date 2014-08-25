from django.db import models
from apps.usuarios.models import Usuario

class Comentario(models.Model):
    descripcion = models.CharField(
        max_length = 300
    )

    autor = models.ForeignKey(
        Usuario
    )

    fecha_creacion = models.DateField(
        auto_now_add = True
    )
