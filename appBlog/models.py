from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    evento = models.CharField(max_length=100)
    def __str__(self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | E-mail: {self.correo} | Evento: {self.evento}.'
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    edad = models.IntegerField(default=0)
    def __str__(self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | E-mail: {self.correo} | Edad: {self.edad}.'
    class Meta:
        verbose_name = 'Estudiantes'
        verbose_name_plural = 'Estudiantes'

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField(default=0)
    duracion = models.IntegerField(default=3)
    def __str__(self):
        return f'Nombre: {self.nombre} | Codigo: {self.codigo} | Duracion: {self.duracion} semanas.'
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'