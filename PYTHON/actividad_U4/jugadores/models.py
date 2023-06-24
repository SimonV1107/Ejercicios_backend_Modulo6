from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50)

    