from django.contrib import admin

from appBlog.models import Curso, Estudiante, Reserva

# Register your models here.

admin.site.register(Reserva)

admin.site.register(Estudiante)

admin.site.register(Curso)
