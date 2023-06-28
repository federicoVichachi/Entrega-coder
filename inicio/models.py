from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    curso = models.CharField(max_length=30)
    
class Curso(models.Model):
    contenido = models.CharField(max_length=30)
    duracion = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()