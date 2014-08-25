from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    username = models.OneToOneField(
        User
    )

    es_directivo = models.BooleanField(
        default=False
    )

    es_programador = models.BooleanField(
        default=False
    )

    es_usuario = models.BooleanField(
        default=False
    )

    def __unicode__(self):
        return self.username.username
