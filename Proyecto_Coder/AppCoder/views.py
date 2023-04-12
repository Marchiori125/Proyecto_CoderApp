from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def busquedaCamada(request):
    return render(request, "busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada= request.GET["camada"]
        curso = Curso.objects.filter(camada=camada)
        return render(request, "resultadosBusqueda.html", {"cursos": curso, "camada": camada})
    else:
        return HttpResponse(f'No enviaste nada')

def cursos(request):
    print("method: ", request.method)
    print("post: ", request.POST)

    if request.method == 'POST':
        curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
        curso.save()
        return render(request, "inicio.html")

    return render(request, "cursos.html")

def estudiantes(request):

    if request.method == 'POST':
        estudiante = Estudiante(usuario=request.POST["usuario"], email=request.POST["email"], contraseña=request.POST["contraseña"])
        estudiante.save()
        return render(request, "inicio.html")

    return render(request, "estudiantes.html")

def profesores(request):
    if request.method == 'POST':
        profesor = Profesor(usuario=request.POST["usuario"], email=request.POST["email"], contraseña=request.POST["contraseña"], profesion=request.POST["profesion"])
        profesor.save()
        return render(request, "inicio.html")

    return render(request, "profesores.html")

def entregables(self):

    return render(self, "entregables.html")