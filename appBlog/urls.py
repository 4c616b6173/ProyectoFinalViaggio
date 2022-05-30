from django.urls import path, re_path
from appBlog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutDeveloper', views.aboutDeveloper, name='aboutDeveloper'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('beStudent', views.beStudent, name='beStudent'),
    path('courseAdmin', views.courseAdmin, name='courseAdmin'),
    path('search/', views.search),
    path('resultadoBusqueda', views.search, name='resultadoBusqueda'),
    path('projects/', views.projects, name='projects'),
    path('apply/', views.apply, name='apply'),
    #URL LISTA DE CURSOS:
    path('course/list', views.CourseList.as_view(), name='courseList'),
    re_path(r'^courseDetail(?P<pk>\d+)$', views.CourseDetail.as_view(), name='CourseDetail'),
    re_path(r'^newCourse$', views.CourseCreation.as_view(), name='NewCourse'),
    re_path(r'^courseEdit/(?P<pk>\d+)$', views.CourseUpdate.as_view(),name='CourseEdit'),
    re_path(r'^courseDelete/(?P<pk>\d+)$', views.CourseDelete.as_view(), name='CourseDelete'),
    #URL LISTA DE RESERVAS:
    path('book/list', views.BookList.as_view(), name='bookList'),
    re_path(r'^bookDetail/(?P<pk>\d+)$', views.BookDetail.as_view(), name='BookDetail'),
    re_path(r'^bookEdit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='BookEdit'),
    re_path(r'^bookDelete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='BookDelete'),
    #URL Student list:\
    path('students/list', views.StudentList.as_view(), name='studentList'),
    re_path(r'^studentDetails/(?P<pk>\d+)$', views.StudentDetail.as_view(), name='StudentDetail'),
    re_path(r'^studentDelete/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='StudentDelete'),
    path('login', views.loginRequest, name='login'),
    path('register/', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='appBlog/homePage/logout.html'), name='logout'),
    path('userEdit/', views.userEdit, name='userEdit'),
]