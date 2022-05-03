from django import forms

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