from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    curso = models.CharField(max_length=30)
    descripcion = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='alumnos_fotos/', null=True, blank=True)
    fecha_ingreso = models.DateField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} | Edad: {self.edad} | Cursando: {self.curso}'
    
class Curso(models.Model):
    contenido = models.CharField(max_length=30)
    duracion = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()