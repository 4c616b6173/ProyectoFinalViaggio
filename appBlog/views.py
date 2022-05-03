from django.shortcuts import render

from appBlog.forms import ReservasFormulario
from appBlog.models import Reservas

# Create your views here.
def home(request):
    if request.method == 'POST':

        reservasF = ReservasFormulario(request.POST)

        print(reservasF)

        if reservasF.is_valid():

            informacion = reservasF.cleaned_data

            reservas = Reservas(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], evento=informacion['evento'])

            reservas.save()

            return render(request, "home.html")
        
    else:

        reservasF = ReservasFormulario()
    return render(request, 'home.html', {'reservasF':reservasF})

def about_creator(request):
    return render(request, 'about_creator.html')

def about_me(request):
    return render(request, 'about_me.html')

def prueba(request):
    return render(request, 'prueba.html')
