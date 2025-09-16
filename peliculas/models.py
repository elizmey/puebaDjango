from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    año = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo