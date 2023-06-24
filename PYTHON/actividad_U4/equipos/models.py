from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    ligas = models.IntegerField()
    champions = models.IntegerField()
