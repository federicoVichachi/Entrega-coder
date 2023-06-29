from django import forms

class InsertAlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    curso = forms.CharField(max_length=30)

class SearchAlumno(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)

class InsertCursoForm(forms.Form):
    contenido = forms.CharField(max_length=30)
    duracion = forms.IntegerField()

class InsertProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()