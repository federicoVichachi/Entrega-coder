from django.shortcuts import render, redirect
from inicio.forms import InsertAlumnoForm, SearchAlumno, InsertCursoForm, InsertProfesorForm
from inicio.models import Alumno, Curso, Profesor
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
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
            return redirect('inicio:lista_alumnos')
        else:
            return render(request, 'inicio/insert_alumno.html', {'formularioA': formulario})
    
    formulario = InsertAlumnoForm()
    return render(request, 'inicio/insert_alumno.html', {'formularioA': formulario})

def list_alumno(request):
    
    formulario = SearchAlumno(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_alumnos = Alumno.objects.filter(nombre__icontains = nombre_a_buscar)
    return render(request, 'inicio/lista_alumnos.html', {'formularioBusqueda': formulario, 'alumnos': listado_alumnos})

class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "inicio/detalle_alumnos.html"

class ModificarAlumno(UpdateView):
    model = Alumno
    fields = ['nombre', 'edad', 'curso', 'descripcion', 'foto', 'fecha_ingreso'] 
    template_name = "inicio/modificar_alumnos.html"
    success_url = reverse_lazy('inicio:lista_alumnos')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class EliminarAlumno(DeleteView):
    model = Alumno
    template_name = "inicio/eliminar_alumnos.html"
    success_url = reverse_lazy('inicio:lista_alumnos')


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

def about_me(request):
    return render(request, 'inicio/about_me.html')