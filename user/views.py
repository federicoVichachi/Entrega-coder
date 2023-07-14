from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from user.forms import LoginForm

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario .is_valid():
            usuario = formulario.cleaned_data['username']
            contrasena = formulario.cleaned_data['password']
            
            user =authenticate(username = usuario, password = contrasena)
            django_login(request,user)
            return redirect('inicio:inicio')    
        else:
            return render(request, 'user/login.html', {'formulario': formulario} )
        
    
    formulario = AuthenticationForm()
    return render(request, 'user/login.html', {'formulario': formulario} )

def register (request):
    
    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('user:login')
        else:
            return render(request,'user/register.html',{'formulario':formulario})
            
            
    
    formulario = LoginForm()
    
    return render(request,'user/register.html',{'formulario':formulario})