import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from.models import Solicitud, Recurso, Solicitud_Recurso
from .forms import SolicitudForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.http import JsonResponse
# Create your views here.

# Vistas basadas en clases
class ListarSolicitud (ListView):
    model = Solicitud
    template_name = "vale_consumo/listar_vale.html"
    context_object_name = 'solicitudes'
    queryset = Solicitud.objects.all()

class CrearSolicitud(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'vale_consumo/crear_vale.html'
    success_url = reverse_lazy('vale_consumo/listar_vale.html')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Recurso.objects.filter(nombre_recurso__icontains=request.POST['term'])
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.nombre_recurso
                    data.append(item)
            elif action == "add":
                vents = json.loads(request.POST['vents'])
                soli = Solicitud()
                soli.solicitante = vents['solicitante']
                soli.fecha_solicitud = vents['fecha_solicitud']
                soli.save()
                for i in vents['recursos']:
                    sol_rec = Solicitud_Recurso()
                    sol_rec.id_solicitud = soli.id_solicitud
                    sol_rec.id_recurso = i['id_recurso']
                    sol_rec.cantidad_solicitada = int(i['cantidad_solicitada'])
                    sol_rec.save()
                
                

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = e
        return JsonResponse(data, safe=False)
