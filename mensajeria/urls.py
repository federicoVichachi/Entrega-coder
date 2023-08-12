from django.urls import path
from . import views

app_name = 'mensajeria'

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('enviar/<int:destinatario_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('lista/', views.lista_mensajes, name='lista_mensajes'),
]