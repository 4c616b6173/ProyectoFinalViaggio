from django.urls import path
from appBlog import views

urlpatterns = [
    path('', views.home, name='home'),
    
]