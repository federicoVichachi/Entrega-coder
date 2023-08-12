from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje  # Especifica el modelo a utilizar
        fields = ['contenido']  # Incluye los campos deseados en el formulario
        widgets = {
            'contenido': forms.Textarea,  # Opcionalmente, personaliza los widgets
        }