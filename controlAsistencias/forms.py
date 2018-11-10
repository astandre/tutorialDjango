from django import forms
from .models import *


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['cedula', 'nombre', 'sexo', 'evento']


class InscripcionUpdateForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['nombre', 'evento']
