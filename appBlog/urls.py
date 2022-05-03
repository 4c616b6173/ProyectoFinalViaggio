from django.urls import path
from appBlog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_developer', views.about_developer, name='about_developer'),
    path('about_me', views.about_me, name='about_me'),
    path('serEstudiante', views.serEstudiante, name='serEstudiante'),
    path('addCursos', views.addCursos, name='addCursos'),
    path('buscar/', views.buscar),
    path('resultadoBusqueda', views.buscar, name='resultadoBusqueda')
]