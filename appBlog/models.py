from django.db import models

# Create your models here.
class Reservas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    evento = models.CharField(max_length=100)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    edad = models.IntegerField(default=0)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    edad = models.IntegerField(default=0)
    duracion = models.IntegerField(default=3)
