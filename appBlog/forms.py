from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservasFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    evento = forms.CharField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    edad = forms.IntegerField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    duracion = forms.IntegerField()

# class UserRegisterForm(UserCreationForm):

#     email = forms.EmailField()
#     password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']