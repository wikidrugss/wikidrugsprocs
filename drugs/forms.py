from django import forms
from .models import Consulta

class crearConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('consulta',)

class responderConsultaForm(forms.ModelForm):
    class Meta:
        model= Consulta
        fields = ('respuesta',)