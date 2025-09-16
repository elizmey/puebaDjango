from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'genero', 'año']
        widgets = {
            'año': forms.TextInput(attrs={'placeholder': ''})
        }