from email import message
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from appBlog.forms import CourseForm, StudentForm, UserRegisterForm, BookForm
from appBlog.models import Avatar, Course, Student, Book
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from appBlog.decorators import unauthenticated_user, allowed_users

# Create your views here.
@unauthenticated_user
def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            user = form.save()

            group = Group.objects.get(name='users')

            user.groups.add(group)


            return render(request, 'appBlog/homePage/index.html')
    
    else:
        form = UserRegisterForm
    return render(request, 'appBlog/homePage/register.html', {'form':form})




@unauthenticated_user
def loginRequest(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            user = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user1 = authenticate(username=user, password=passw)

            if user:

                login(request, user1)

                return redirect('home')

        else:
            return render(request, 'appBlog/homePage/index.html', {'mensaje':f'Error. Datos incorrectos.'})

    else:
        form = AuthenticationForm

    return render(request, 'appBlog/homePage/login.html', {'form':form})

@unauthenticated_user
def home(request):

    return render(request, 'appBlog/homePage/index.html')


@login_required
@allowed_users(allowed_roles=['admin', 'users'])
def homeLogin(request):

    avatars = Avatar.objects.filter(user=request.user.id)
    return render(request, 'appBlog/homePage/index.html', {'url':avatars[0].image.url})

@login_required
@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    return render(request, 'appBlog/admin/adminPage.html', {'url':avatars[0].image.url})

@login_required
@allowed_users(allowed_roles=['admin', 'users'])
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
    avatars = Avatar.objects.filter(user=request.user.id)
    return render(request, 'appBlog/about/aboutDeveloper.html', {'url':avatars[0].image.url})

def aboutMe(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    return render(request, 'appBlog/about/aboutMe.html', {'url':avatars[0].image.url})

@login_required
@allowed_users(allowed_roles=['admin', 'users'])
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
@allowed_users(allowed_roles=['admin'])
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

@login_required
@allowed_users(allowed_roles=['admin', 'users'])
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

def unauthorized(request):
    
    return render(request, 'appBlog/blank/unauthorized.html')
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

    fields = ['name', 'lastname', 'mail', 'event']

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




