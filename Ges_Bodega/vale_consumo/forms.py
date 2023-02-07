from django.forms import *
import datetime
from .models import Solicitud




class SolicitudForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'solicitante': Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'',
                }
            ),
            'unidad_negocio': Select(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',

                }
            ),
            'id_centro_costo': Select(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                }
            ),
            'piso': TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'',
                    'id':'',
                    'type': 'number',
                    'min':1,
                }
            ),
        }
    fecha_solicitud = DateField(widget=NumberInput(attrs={'type': 'date', 'class':'form-control ' }), initial=datetime.date.today)

