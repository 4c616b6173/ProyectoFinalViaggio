from django.urls import path
from appBlog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutDeveloper', views.aboutDeveloper, name='aboutDeveloper'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('serEstudiante', views.serEstudiante, name='serEstudiante'),
    path('addCursos', views.addCursos, name='addCursos'),
    path('buscar/', views.buscar),
    path('resultadoBusqueda', views.buscar, name='resultadoBusqueda')
]