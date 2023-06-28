from django.urls import path
from inicio import views  

app_name = 'inicio'

urlpatterns = [ 
    path('', views.inicio, name='inicio'),
    path("alumnos/insertar/", views.insert_alumno, name="insertar_alumno"),
    path("cursos/insertar/", views.insert_curso, name ="insertar_curso"),
    path("profesores/insertar/", views.insert_profesor, name ="insertar_profesor"),
]