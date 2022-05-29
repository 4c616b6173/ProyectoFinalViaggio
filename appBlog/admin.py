from django.contrib import admin

from appBlog.models import Course, Student, Book

# Register your models here.

admin.site.register(Book)

admin.site.register(Student)

admin.site.register(Course)
