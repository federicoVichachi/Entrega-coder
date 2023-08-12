from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user.forms import LoginForm, MiFormularioDeEdicionDeDatosUsuario
from django.urls import reverse_lazy
from user.models import InfoExtra
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
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
def ver_perfil(request):
    info_extra = request.user.infoextra
    context = {
        'info_extra': info_extra,
    }
    return render(request, 'user/ver_perfil.html', context)


class EdicionPerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = MiFormularioDeEdicionDeDatosUsuario
    template_name = 'user/edicion_perfil.html'
    success_url = reverse_lazy('user:perfil')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        
        fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento:
            self.object.infoextra.fecha_nacimiento = fecha_nacimiento
            self.object.infoextra.save()

        return response


class ModificarPass (LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/modificar_pass.html'
    success_url= reverse_lazy('user:edicion_perfil')
    