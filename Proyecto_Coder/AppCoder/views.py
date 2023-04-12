from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def inicio(self):

    return render(self, "Inicio.html")

def cursos(self):

    return HttpResponse("Vista Cursos")

def estudiantes(self):

    return HttpResponse("Vista Estudiantes")

def profesores(self):

    return HttpResponse("Vista Profesores")

def entregables(self):

    return HttpResponse("Vista Entegables")