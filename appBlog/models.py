from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    mail = models.EmailField()
    event = models.CharField(max_length=100)
    def __str__(self):
        return f'Name: {self.name} | Lastname: {self.lastname} | E-mail: {self.mail} | Event: {self.event}.'
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Student(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    mail = models.EmailField()
    age = models.IntegerField(default=0)
    def __str__(self):
        return f'Name: {self.name} | Lastname: {self.lastname} | E-mail: {self.mail} | Edad: {self.age}.'
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField(default=0)
    duration = models.IntegerField(default=3)
    def __str__(self):
        return f'Name: {self.name} | Code: {self.code} | Duration: {self.duration} weeks.'
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='avatars', null = True, blank = True)

