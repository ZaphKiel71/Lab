
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('login', views.login),
    re_path('carreras/add/', views.add_carrera),
    re_path('alumnos/add/', views.add_alumno),
]