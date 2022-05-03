from django import forms

class ReservasFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    evento = forms.CharField()