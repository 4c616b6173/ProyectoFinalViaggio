from django.contrib import admin

from appBlog.models import Curso, Estudiante, Book

# Register your models here.

admin.site.register(Book)

admin.site.register(Estudiante)

admin.site.register(Curso)
