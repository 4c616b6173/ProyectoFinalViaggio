from django.urls import path
from appBlog import views
from django.contrib.auth.views import LogoutView

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
    path(r'^detalleCurso(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='DetailCurso'),
    path(r'^nuevoCurso$', views.CursoCreacion.as_view(), name='NewCurso'),
    path(r'^editarCurso/(?P<pk>\d+)$', views.CursoUpdate.as_view(),name='EditCurso'),
    path(r'^borrarCurso/(?P<pk>\d+)$', views.CursoBorrar.as_view(), name='DeleteCurso'),
    #URL LISTA DE RESERVAS:
    path('reservas/list', views.ReservaLista.as_view(), name='listaReservas'),
    path(r'^detalleReserva/(?P<pk>\d+)$', views.ReservaDetalle.as_view(), name='DetailReserva'),
    path(r'^editarReserva/(?P<pk>\d+)$', views.ReservaUpdate.as_view(), name='EditReserva'),
    path(r'^borrarReserva/(?P<pk>\d+)$', views.ReservaDelete.as_view(), name='DeleteReserva'),
    #URL LISTA DE RESERVAS:\
    path('estudiante/list', views.EstudianteLista.as_view(), name='listaEstudiantes'),
    path(r'^detalleEstudiante/(?P<pk>\d+)$', views.EstudianteDetalle.as_view(), name='DetailEstudiante'),
    path(r'^borrarEstudiante/(?P<pk>\d+)$', views.EstudianteDelete.as_view(), name='DeleteEstudiante'),
    path('login', views.loginRequest, name='login'),
    path('register/', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='appBlog/homePage/logout.html'), name='logout'),
]