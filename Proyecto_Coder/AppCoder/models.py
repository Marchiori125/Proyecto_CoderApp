from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.camada}"

class Estudiante(models.Model):

    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.email}"

class Profesor(models.Model):

    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.email}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()