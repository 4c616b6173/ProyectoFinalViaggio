from django.urls import path
from appBlog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_creator', views.about_creator, name='about_creator'),
    path('about_me', views.about_me, name='about_me'),
    path('prueba', views.prueba, name='prueba'),
]