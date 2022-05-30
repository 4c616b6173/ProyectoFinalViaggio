from django.http import HttpResponse
from django.shortcuts import render

from appBlog.forms import CourseForm, StudentForm, UserRegisterForm, BookForm
from appBlog.models import Course, Student, Book
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
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

        bookF = BookForm(request.POST)

        print(bookF)

        if bookF.is_valid():

            information = bookF.cleaned_data

            book = Book(name=information['name'], lastname=information['lastname'], mail=information['mail'], event=information['event'])

            book.save()

            return render(request, "appBlog/blank/backToHome.html")
        
    else:

        bookF = BookForm()
    return render(request, 'appBlog/apply/apply.html', {'bookF':bookF})

def projects(request):
    return render(request, 'appBlog/projects/projects.html')

def aboutDeveloper(request):
    return render(request, 'appBlog/about/aboutDeveloper.html')

def aboutMe(request):
    return render(request, 'appBlog/about/aboutMe.html')

def beStudent(request):
    if request.method == 'POST':

        studentsF = StudentForm(request.POST)

        print(studentsF)

        if studentsF.is_valid():

            information = studentsF.cleaned_data

            students = Student(name=information['name'], lastname=information['lastname'], mail=information['mail'], age=information['age'])

            students.save()

            return render(request, "appBlog/blank/backToHome.html")
        
    else:

        studentsF = StudentForm()
    return render(request, 'appBlog/beStudent/beStudent.html', {'studentsF':studentsF})

@login_required

def courseAdmin(request):
    if request.method == 'POST':

        courseF = CourseForm(request.POST)

        print(courseF)

        if courseF.is_valid():

            information = courseF.cleaned_data

            course = Course(name=information['name'], code=information['code'], duration=information['duration'])

            course.save()

            return render(request, "appBlog/blank/backToHome.html")
        
    else:

        courseF = CourseForm()
    return render(request, 'appBlog/coursesAdmin/coursesAdmin.html', {'courseF':courseF})

def busquedaCodigo(request):
    
    return render(request, 'appBlog/coursesAdmin/coursesAdmin.html')


def search(request):

    if request.GET['code']:
        
        code = request.GET['code']

        courses = Course.objects.filter(code__icontains=code)
        
        return render(request, 'appBlog/coursesAdmin/searchResults.html', {'courses':courses, 'code':code})
    else:
        respuesta = 'Wrong data'

    return HttpResponse(respuesta)

def userEdit(request):
    
    user = request.user

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            information = form.cleaned_data

            user.username = information['username']
            user.email = information['email']
            user.password1 = information['password1']
            user.password2 = information['password2']

            user.save()

            return render(request,'appBlog/homePage/index.html')

    else:
        form = UserRegisterForm(initial={'username':user.username, 'email':user.username})

    return render(request, 'appBlog/profiles/editProfile.html',{'form':form, 'userE':user.username})

#================================================================================================================================
#Lista de cursos:
#================================================================================================================================

#CRUD en vistas SIMPLIFICADO:

class CourseList(LoginRequiredMixin, ListView):

    model = Course

    template_name = 'appBlog/lists/coursesList.html'

class CourseDetail(LoginRequiredMixin, DetailView):

    model = Course

    template_name = 'appBlog/lists/courseDetails.html'

class CourseCreation(LoginRequiredMixin, CreateView):

    model = Course

    success_url = '/appBlog/course/list'

    fields = ['name', 'code', 'duration']

class CourseUpdate(LoginRequiredMixin, UpdateView):

    model = Course

    success_url = '/appBlog/course/list'

    fields = ['name', 'code', 'duration']

class CourseDelete(LoginRequiredMixin, DeleteView):

    model = Course

    success_url = '/appBlog/course/list'

#================================================================================================================================
#Lista de reservas:
#================================================================================================================================

class BookList(LoginRequiredMixin, ListView):

    model = Book

    template_name = 'appBlog/lists/reservationsList.html'

class BookDetail(LoginRequiredMixin, DetailView):

    model = Book

    template_name = 'appBlog/lists/reservationDetails.html'

class BookUpdate(LoginRequiredMixin, UpdateView):

    model = Book

    success_url = '/appBlog/book/list'

    fields = ['nombre', 'apellido', 'correo', 'evento']

class BookDelete(LoginRequiredMixin, DeleteView):

    model = Book

    success_url = '/appBlog/book/list'

#================================================================================================================================
#Lista de estudiantes:
#================================================================================================================================

class StudentList(LoginRequiredMixin, ListView):

    model = Student

    template_name = 'appBlog/lists/studentsList.html'

class StudentDetail(LoginRequiredMixin, DetailView):

    model = Student

    template_name = 'appBlog/lists/studentDetails.html'

class StudentUpdate(LoginRequiredMixin, UpdateView):

    model = Student

    success_url = '/appBlog/student/list'

    fields = ['name', 'lastname', 'mail', 'age']

class StudentDelete(LoginRequiredMixin, DeleteView):

    model = Student

    success_url = '/appBlog/student/list'










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
