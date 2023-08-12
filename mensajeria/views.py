from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from mensajeria.models import Mensaje
from mensajeria.forms import MensajeForm

@login_required
def enviar_mensaje(request, destinatario_id):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False) 
            mensaje.remitente = request.user
            mensaje.destinatario_id = destinatario_id
            mensaje.save()  
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('mensajeria:lista_mensajes')
    else:
        form = MensajeForm()

    destinatario = User.objects.get(pk=destinatario_id)
    context = {
        'form': form,
        'destinatario': destinatario,
    }
    return render(request, 'mensajeria/enviar_mensaje.html', context)

@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)

    # Marcar los mensajes como leídos
    for mensaje in mensajes:
        if not mensaje.leido:
            mensaje.leido = True
            mensaje.save()

    context = {
        'mensajes': mensajes,
    }
    return render(request, 'mensajeria/lista_mensajes.html', context)

def lista_usuarios(request):
    usuarios = User.objects.exclude(id=request.user.id)
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'mensajeria/usuarios.html', context)