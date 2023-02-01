from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import Solicitud



class SolicitudForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'solicitante': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'',
                }
            ),
            'unidad_negocio': forms.Select(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                    'readonly':'readonly',
                }
            ),
            'id_centro_costo': forms.Select(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                }
            ),
            'edificio': forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                    'type': 'number',
                    'min':1,
                    'required':'',
                }
            ),
            'piso': forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                    'type': 'number',
                    'min':1,
                }
            ),
        }
    fecha_solicitud = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class':'form-control ' }), initial=datetime.date.today)

