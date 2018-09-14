from django.db import models


# Create your models here.
class Persona(models.Model):
    idPersona = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)


class Evento(models.Model):
    idEvento = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Asistencia(models.Model):
    idAsistencia = models.CharField(primary_key=True, max_length=50)
    persona_idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    evento_idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
