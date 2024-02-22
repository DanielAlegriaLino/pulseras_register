from django import forms
from .models import t_registro

class t_registroForm(forms.ModelForm):
    class Meta:
        model = t_registro
        fields = ['cNombreCompleto', 'cPaisEmpresa', 'cModalidadActividad']
        widgets = {
            'cNombreCompleto': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre'}),
            'cPaisEmpresa': forms.TextInput(attrs={'class': 'form-control', 'id': 'pais'}),
            'cModalidadActividad': forms.TextInput(attrs={'class': 'form-control', 'id': 'modalidad'}),
        }