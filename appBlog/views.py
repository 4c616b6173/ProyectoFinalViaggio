from django.http import HttpResponse
from django.shortcuts import render

from appBlog.forms import CursoFormulario, EstudianteFormulario, ReservasFormulario
from appBlog.models import Curso, Estudiante, Reserva

# Create your views here.
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
    return render(request, 'appBlog/blank/adminCursos.html', {'cursoF':cursoF})

def busquedaCodigo(request):
    
    return render(request, 'appBlog/blank/adminCursos.html')


def buscar(request):

    if request.GET['codigo']:
        
        codigo = request.GET['codigo']

        cursos = Curso.objects.filter(codigo__icontains=codigo)
        
        return render(request, 'appBlog/blank/resultadoBusqueda.html', {'cursos':cursos, 'codigo':codigo})
    else:
        respuesta = 'No eviaste datos'

    return HttpResponse(respuesta)

def listaCursos(request):
    
    cursos = Curso.objects.all()
    contexto = {"cursos":cursos}
    return render(request, "appBlog/blank/listaDeCursos.html",contexto)

def borrarCurso(request, curso_nombre):
    
    curso = Curso.objects.get(nombre=curso_nombre)
    
    curso.delete()
    
    cursos = Curso.objects.all()

    contexto = {'cursos':cursos}

    return render(request, "appBlog/blank/listaDeCursos.html",contexto)

def editarCursos(request, curso_nombre):

    curso = Curso.objects.get(nombre=curso_nombre)

    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso.nombre= informacion['nombre']
            curso.codigo= informacion['codigo']
            curso.duracion= informacion['duracion']

            curso.save()

            return render(request, 'appBlog/homePage/index.html')

    else:

        miFormulario = CursoFormulario(initial={'nombre':curso.nombre, 'codigo':curso.codigo, 'duracion':curso.duracion})

    return render(request, 'appBlog/blank/editarCurso.html', {'miFormulario':miFormulario, 'curso_nombre':curso_nombre})

def listaReservas(request):
    
    reservas = Reserva.objects.all()
    contexto = {"reservas":reservas}
    return render(request, "appBlog/blank/listaDeReservas.html",contexto)

def borrarReserva(request, reserva_nombre):
    
    reserva = Reserva.objects.get(nombre=reserva_nombre)
    
    reserva.delete()
    
    reservas = Reserva.objects.all()

    contexto = {'reservas':reservas}

    return render(request, "appBlog/blank/listaDeReservas.html",contexto)

def editarReservas(request, reserva_nombre):

    reserva = Reserva.objects.get(nombre=reserva_nombre)

    if request.method == 'POST':
        
        miFormulario = ReservasFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            reserva.nombre= informacion['nombre']
            reserva.apellido= informacion['apellido']
            reserva.duracion= informacion['correo']
            reserva.duracion= informacion['evento']

            reserva.save()

            return render(request, 'appBlog/homePage/index.html')

    else:

        miFormulario = ReservasFormulario(initial={'nombre':reserva.nombre, 'apellido':reserva.apellido, 'correo':reserva.correo, 'evento':reserva.evento})

    return render(request, 'appBlog/blank/editarReserva.html', {'miFormulario':miFormulario, 'reserva_nombre':reserva_nombre})



    
