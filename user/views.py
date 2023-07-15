from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user.forms import LoginForm, MiFormularioDeEdicionDeDatosUsuario
from django.urls import reverse_lazy
from user.models import InfoExtra
# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario .is_valid():
            usuario = formulario.cleaned_data['username']
            contrasena = formulario.cleaned_data['password']
            
            user =authenticate(username = usuario, password = contrasena)
            
            django_login(request,user)
            
            InfoExtra.objects.get_or_create(user=user)
            
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

@login_required
def edicion_perfil (request):

    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosUsuario (request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()

            formulario.save()
            return redirect('inicio:inicio')           
    else:
        formulario= MiFormularioDeEdicionDeDatosUsuario (initial={'avatar':request.user.infoextra.avatar},instance= request.user) 
                
    return render(request,'user/edicion_perfil.html',{'formulario':formulario})

class ModificarPass (LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/modificar_pass.html'
    success_url= reverse_lazy('user:edicion_perfil')
    