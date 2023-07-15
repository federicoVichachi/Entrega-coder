from django.urls import path
from inicio import views  

app_name = 'inicio'

urlpatterns = [ 
    path('', views.inicio, name='inicio'),
    path("aboutme/", views.about_me , name="about_me"),
    path("alumnos/insertar/", views.insert_alumno, name="insertar_alumno"),
    path("alumnos/", views.list_alumno, name="lista_alumnos"),
    path("cursos/insertar/", views.insert_curso, name ="insertar_curso"),
    path("profesores/insertar/", views.insert_profesor, name ="insertar_profesor"),
]