from django.http import HttpResponse
from django.shortcuts import render

from appBlog.forms import CursoFormulario, EstudianteFormulario, UserRegisterForm, ReservasFormulario
from appBlog.models import Curso, Estudiante, Reserva
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def loginRequest(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            user = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user1 = authenticate(username=user, password=passw)

            if user:

                login(request, user1)

                return render(request, 'appBlog/homePage/index.html', {'mensaje':f'Bienvenido{user1}.'})

        else:
            return render(request, 'appBlog/homePage/index.html', {'mensaje':f'Error. Datos incorrectos.'})

    else:
        form = AuthenticationForm

    return render(request, 'appBlog/homePage/login.html', {'form':form})

@login_required

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.cleaned_data['username']
            form.save()
            return render(request, 'appBlog/homePage/index.html')
    
    else:
        form = UserRegisterForm
    return render(request, 'appBlog/homePage/register.html', {'form':form})



def home(request):
    return render(request, 'appBlog/homePage/index.html')

def apply(request):
    if request.method == 'POST':

        reservasF = ReservasFormulario(request.POST)

        print(reservasF)

        if reservasF.is_valid():

            informacion = reservasF.cleaned_data

            reservas = Reserva(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], evento=informacion['evento'])

            reservas.save()

            return render(request, "appBlog/blank/vuelveAlInicio.html")
        
    else:

        reservasF = ReservasFormulario()
    return render(request, 'appBlog/apply/apply.html', {'reservasF':reservasF})

def projects(request):
    return render(request, 'appBlog/projects/projects.html')

def aboutDeveloper(request):
    return render(request, 'appBlog/about/aboutDeveloper.html')

def aboutMe(request):
    return render(request, 'appBlog/about/aboutMe.html')

def serEstudiante(request):
    if request.method == 'POST':

        estudiantesF = EstudianteFormulario(request.POST)

        print(estudiantesF)

        if estudiantesF.is_valid():

            informacion = estudiantesF.cleaned_data

            estudiantes = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], edad=informacion['edad'])

            estudiantes.save()

            return render(request, "appBlog/blank/vuelveAlInicio.html")
        
    else:

        estudiantesF = EstudianteFormulario()
    return render(request, 'appBlog/serEstudiante/serEstudiante.html', {'estudiantesF':estudiantesF})

@login_required

def adminCursos(request):
    if request.method == 'POST':

        cursoF = CursoFormulario(request.POST)

        print(cursoF)

        if cursoF.is_valid():

            informacion = cursoF.cleaned_data

            curso = Curso(nombre=informacion['nombre'], codigo=informacion['codigo'], duracion=informacion['duracion'])

            curso.save()

            return render(request, "appBlog/blank/vuelveAlInicio.html")
        
    else:

        cursoF = CursoFormulario()
    return render(request, 'appBlog/adminCursos/adminCursos.html', {'cursoF':cursoF})

def busquedaCodigo(request):
    
    return render(request, 'appBlog/adminCursos/adminCursos.html')


def buscar(request):

    if request.GET['codigo']:
        
        codigo = request.GET['codigo']

        cursos = Curso.objects.filter(codigo__icontains=codigo)
        
        return render(request, 'appBlog/adminCursos/resultadoBusqueda.html', {'cursos':cursos, 'codigo':codigo})
    else:
        respuesta = 'No eviaste datos'

    return HttpResponse(respuesta)

#================================================================================================================================
#Lista de cursos:
#================================================================================================================================

#CRUD en vistas SIMPLIFICADO:

class CursoLista(LoginRequiredMixin, ListView):

    model = Curso

    template_name = 'appBlog/listas/listaDeCursos.html'

class CursoDetalle(LoginRequiredMixin, DetailView):

    model = Curso

    template_name = 'appBlog/listas/detallesCurso.html'

class CursoCreacion(LoginRequiredMixin, CreateView):

    model = Curso

    success_url = '/appBlog/curso/list'

    fields = ['nombre', 'codigo', 'duracion']

class CursoUpdate(LoginRequiredMixin, UpdateView):

    model = Curso

    success_url = '/appBlog/curso/list'

    fields = ['nombre', 'codigo', 'duracion']

class CursoBorrar(LoginRequiredMixin, DeleteView):

    model = Curso

    success_url = '/appBlog/cursos/list'

#================================================================================================================================
#Lista de reservas:
#================================================================================================================================

class ReservaLista(LoginRequiredMixin, ListView):

    model = Reserva

    template_name = 'appBlog/listas/listaDeReservas.html'

class ReservaDetalle(LoginRequiredMixin, DetailView):

    model = Reserva

    template_name = 'appBlog/listas/detallesReserva.html'

class ReservaUpdate(LoginRequiredMixin, UpdateView):

    model = Reserva

    success_url = '/appBlog/reservas/list'

    fields = ['nombre', 'apellido', 'correo', 'evento']

class ReservaDelete(LoginRequiredMixin, DeleteView):

    model = Reserva

    success_url = '/appBlog/reservas/list'

#================================================================================================================================
#Lista de estudiantes:
#================================================================================================================================

class EstudianteLista(LoginRequiredMixin, ListView):

    model = Estudiante

    template_name = 'appBlog/listas/listaDeEstudiante.html'

class EstudianteDetalle(LoginRequiredMixin, DetailView):

    model = Estudiante

    template_name = 'appBlog/listas/detallesEstudiante.html'

class EstudianteUpdate(LoginRequiredMixin, UpdateView):

    model = Estudiante

    success_url = '/appBlog/estudiante/list'

    fields = ['nombre', 'apellido', 'correo', 'edad']

class EstudianteDelete(LoginRequiredMixin, DeleteView):

    model = Estudiante

    success_url = '/appBlog/estudiante/list'










# Lista antigua de modelo Curso
# def listaCursos(request):
    
#     cursos = Curso.objects.all()
#     contexto = {"cursos":cursos}
#     return render(request, "appBlog/listas/listaDeCursos.html",contexto)

# def borrarCurso(request, curso_nombre):
    
#     curso = Curso.objects.get(nombre=curso_nombre)
    
#     curso.delete()
    
#     cursos = Curso.objects.all()

#     contexto = {'cursos':cursos}

#     return render(request, "appBlog/listas/listaDeCursos.html",contexto)

# def editarCursos(request, curso_nombre):

#     curso = Curso.objects.get(nombre=curso_nombre)

#     if request.method == 'POST':
        
#         editarCForm = CursoFormulario(request.POST)

#         if editarCForm.is_valid():

#             informacion = editarCForm.cleaned_data

#             curso.nombre= informacion['nombre']
#             curso.codigo= informacion['codigo']
#             curso.duracion= informacion['duracion']

#             curso.save()

#             return render(request, 'appBlog/homePage/index.html')

#     else:

#         editarCForm = CursoFormulario(initial={'nombre':curso.nombre, 'codigo':curso.codigo, 'duracion':curso.duracion})

#     return render(request, 'appBlog/listas/editarCurso.html', {'editarCForm':editarCForm, 'curso_nombre':curso_nombre})



#LISTAS VIEJAS DE RESERVAS:

# def listaReservas(request):
    
#     reservas = Reserva.objects.all()
#     contexto = {"reservas":reservas}
#     return render(request, "appBlog/listas/listaDeReservas.html",contexto)

# def borrarReserva(request, reserva_nombre):
    
#     reserva = Reserva.objects.get(nombre=reserva_nombre)
    
#     reserva.delete()
    
#     reservas = Reserva.objects.all()

#     contexto = {'reservas':reservas}

#     return render(request, "appBlog/listas/listaDeReservas.html",contexto)

# def editarReservas(request, reserva_nombre):

#     reserva = Reserva.objects.get(nombre=reserva_nombre)

#     if request.method == 'POST':
        
#         miFormulario = ReservasFormulario(request.POST)

#         if miFormulario.is_valid():

#             informacion = miFormulario.cleaned_data

#             reserva.nombre= informacion['nombre']
#             reserva.apellido= informacion['apellido']
#             reserva.duracion= informacion['correo']
#             reserva.duracion= informacion['evento']

#             reserva.save()

#             return render(request, 'appBlog/homePage/index.html')

#     else:

#         miFormulario = ReservasFormulario(initial={'nombre':reserva.nombre, 'apellido':reserva.apellido, 'correo':reserva.correo, 'evento':reserva.evento})

#     return render(request, 'appBlog/listas/editarReserva.html', {'miFormulario':miFormulario, 'reserva_nombre':reserva_nombre})
