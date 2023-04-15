from django.urls import path
from .views import *

urlpatterns = [
    path("", buscarComision, name="inicioApp"),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    path("busquedaComisiones/", buscandoComision),
   
]    