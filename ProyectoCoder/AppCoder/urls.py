from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, cursos, profesores, estudiantes, entregables, inicio
from AppCoder import views

urlpatterns = [
    #path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    #path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('', views.inicio),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables', views.entregables),
]