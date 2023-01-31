from django import forms
from .models import Solicitud, Solicitud_Recurso



class SolicitudForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Solicitud
        fields = ['solicitante', 'fecha_solicitud']
        widgets = {
            'solicitante': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'fecha_solicitud': forms.DateInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                }
            ),
}

