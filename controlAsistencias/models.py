from django.db import models


# Create your models here.


class Eventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    hora_inicio = models.DateTimeField()
    imagen = models.CharField(max_length=300)

    class Meta:
        default_related_name = 'eventos'
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        db_table = 'eventos'

    def __str__(self):
        return self.nombre


class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    HOMBRE = 'H'
    MUJER = 'M'
    SEX_CHOICES = (
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer')
    )
    sexo = models.CharField(max_length=100, choices=SEX_CHOICES, default=HOMBRE)
    evento = models.ManyToManyField(Eventos)

    class Meta:
        default_related_name = 'personas'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        db_table = 'persona'

    def __str__(self):
        return self.nombre


class Actividades(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    hora_inicio = models.TimeField()
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'actividades'
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        db_table = 'actividades'

    def __str__(self):
        return self.titulo
