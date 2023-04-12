from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('entregables/', entregables),
]
