from django.http import HttpResponse
from django.shortcuts import render

from appBlog.forms import CursoFormulario, EstudianteFormulario, ReservasFormulario
from appBlog.models import Curso, Estudiante, Reservas

# Create your views here.
def home(request):
    return render(request, 'appBlog/homePage/index.html')

def apply(request):
    if request.method == 'POST':

        reservasF = ReservasFormulario(request.POST)

        print(reservasF)

        if reservasF.is_valid():

            informacion = reservasF.cleaned_data

            reservas = Reservas(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], evento=informacion['evento'])

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

def addCursos(request):
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
    return render(request, 'appBlog/blank/addCursos.html', {'cursoF':cursoF})

def busquedaCodigo(request):
    
    return render(request, 'appBlog/blank/addCursos.html')


def buscar(request):

    if request.GET['codigo']:
        
        codigo = request.GET['codigo']

        cursos = Curso.objects.filter(codigo__icontains=codigo)
        
        return render(request, 'appBlog/blank/resultadoBusqueda.html', {'cursos':cursos, 'codigo':codigo})
    else:
        respuesta = 'No eviaste datos'

    return HttpResponse(respuesta)
    
