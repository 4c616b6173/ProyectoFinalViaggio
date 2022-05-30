from django.contrib import admin

from appBlog.models import Avatar, Course, Student, Book

# Register your models here.

admin.site.register(Book)

admin.site.register(Student)

admin.site.register(Course)

admin.site.register(Avatar)
