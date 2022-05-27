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
    #URL LISTA DE CURSOS:
    path('cursos/list', views.CursoLista.as_view(), name='listaCursos'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoBorrar.as_view(), name='Delete'),
    #URL LISTA DE RESERVAS:
    path('reservas/list', views.ReservaLista.as_view(), name='listaReservas'),
    
]