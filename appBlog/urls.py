from django.urls import path
from appBlog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutDeveloper', views.aboutDeveloper, name='aboutDeveloper'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('serEstudiante', views.serEstudiante, name='serEstudiante'),
    path('adminCursos', views.adminCursos, name='adminCursos'),
    path('buscar/', views.buscar),
    path('resultadoBusqueda', views.buscar, name='resultadoBusqueda'),
    path('projects/', views.projects, name='projects'),
    path('apply/', views.apply, name='apply'),
    path('listaCursos/', views.listaCursos, name='listaCursos'),
    path('listaReservas/', views.listaReservas, name='listaReservas'),
    path('borrarCurso/<curso_nombre>', views.borrarCurso, name='borrarCurso'),
    path('editarCurso/<curso_nombre>', views.editarCursos, name='editarCurso'),
    path('borrarReserva/<reserva_nombre>', views.borrarReserva, name='borrarReserva'),
    path('editarReserva/<reserva_nombre>', views.editarReservas, name='editarReserva'),
    
]