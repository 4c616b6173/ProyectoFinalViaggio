from django.contrib import admin

from appBlog.models import Curso, Estudiante, Reservas

# Register your models here.

admin.site.register(Reservas)

admin.site.register(Estudiante)

admin.site.register(Curso)
