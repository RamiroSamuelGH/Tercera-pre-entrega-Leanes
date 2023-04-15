from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.
def cursos(request):
    
    if request.method == "POST":
        
        form=CursoForm(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            curso=Curso(nombre=info["nombre"], comision=info["comision"])

            curso.save()

    else:
        form = CursoForm()         

    cursos = Curso.objects.all()
    context = {"cursos" : cursos, "form" : form}
    return render(request, "cursos.html", context)

def buscarComision(request):
    
    return render(request, "inicio.html")

def buscandoComision(request):

    comisionIngresada=request.GET["comision"] 
    if comisionIngresada!="":
        comisiones=Comision.objects.filter(comision__icontains==comisionIngresada)
        print(comisiones)
        return render(request, "busquedaComisiones.html", {"comisiones" : comisiones})   
    else:
        return render(request, "inicio.html", {"mensaje" : "Ingrese una comision porfavor"})
def profesores(request):

    if request.method == "POST":
        form=ProfesorForm(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            profesor=Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])

            profesor.save()

    else:
        form = ProfesorForm()         

    profesores = Profesor.objects.all()
    context = {"profesores" : profesores, "form" : form}
    return render(request, "profesores.html", context)

def estudiantes(request):
    
    if request.method == "POST":
        form=EstudianteForm(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            estudiante=Estudiante(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])

            estudiante.save()

    else:
        form = EstudianteForm()         

    estudiantes = Estudiante.objects.all()
    context = {"estudiantes" : estudiantes, "form" : form}
    return render(request, "estudiantes.html", context)

def entregables(request):

    if request.method == "POST":

        form=EntregableForm(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            entregable=Entregable(nombre=info["nombre"], fecha_entrega=info["fecha_entrega"], entregado=info["entregado"])

            entregable.save()

    else:
        form = EntregableForm()         

    entregables = Entregable.objects.all()
    context = {"entregables" : entregables, "form" : form}
    return render(request, "entregables.html", context)

   

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

