from django.shortcuts import render
from inicio.forms import InsertAlumnoForm, InsertCursoForm, InsertProfesorForm
from inicio.models import Alumno, Curso, Profesor
# Create your views here.

def inicio (request):
    return render(request, 'inicio/inicio.html')

def insert_alumno(request):
    
    if request.method == 'POST':
        formulario = InsertAlumnoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(nombre = info['nombre'], edad = info['edad'], curso = info['curso'])
            alumno.save()
            return render(request, 'inicio/insert_alumno.html', {'formularioA': formulario, 'mensajeA': f'Se inscribio el alumno con nombre {alumno.nombre}, edad {alumno.edad} y esta cursando {alumno.curso}'})
        else:
            return render(request, 'inicio/insert_alumno.html', {'formularioA': formulario})
    
    formulario = InsertAlumnoForm()
    return render(request, 'inicio/insert_alumno.html', {'formularioA': formulario})

def insert_curso(request):
    
    if request.method == 'POST':
        formulario = InsertCursoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Curso(contenido = info['contenido'], duracion = info['duracion'])
            curso.save()
            return render(request, 'inicio/insert_curso.html', {'formularioB': formulario, 'mensajeB': f'Se guardo el curso de {curso.contenido}, su duración es de {curso.duracion} dias'})
        else:
            return render(request, 'inicio/insert_curso.html', {'formularioB': formulario})
    formulario = InsertCursoForm()
    return render(request, 'inicio/insert_curso.html', {'formularioB': formulario})

def insert_profesor(request):
    
    if request.method == 'POST':
        formulario = InsertProfesorForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            profesor = Profesor(nombre = info['nombre'], edad = info['edad'])
            profesor.save()
            return render(request, 'inicio/insert_profesor.html', {'formularioC': formulario, 'mensajeC': f'Se guardó el profesor de nombre {profesor.nombre}, tiene {profesor.edad} años'})
        else:
            return render(request, 'inicio/insert_profesor.html', {'formularioC': formulario})
    formulario = InsertProfesorForm()
    return render(request, 'inicio/insert_profesor.html', {'formularioC': formulario})