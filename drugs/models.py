from django.db import models
from django.utils import timezone


class Consulta(models.Model):
    nombre = models.CharField(max_length=200)
    email = models. EmailField(max_length=200)
    consulta = models.TextField(max_length=200)
    respuesta = models.TextField(max_length=200)
    respondida = models.BooleanField(default=False)

    def publish(self):
        self.respondida = True
        self.save()

    def __str__(self):
        return self.consulta

