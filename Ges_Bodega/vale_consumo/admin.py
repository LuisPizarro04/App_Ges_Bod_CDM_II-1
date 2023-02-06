from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Unidad_Negocio, Centro_Costo, Bodega, Categoria, Recurso, Solicitud, Solicitud_Recurso
from usuario.models import  Usuario # Preparador,
# Register your models here.

class Unidad_NegocioResource(resources.ModelResource):
    class Meta:
        model = Unidad_Negocio



# UNIDAD DE NEGOCIO
class Unidad_NegocioAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = (
        'id_unidad_negocio',
        'nombre_unidad_negocio',
        'is_active_unidad_negocio'
    )
    search_fields=['id_unidad_negocio']
    resources_class = Unidad_NegocioResource
# CENTRO DE COSTOS
class Cetro_CostoAdmin(admin.ModelAdmin):
    list_display = (
        'unidad_negocio',
        'crr',
        'nombre_centro_costo',
        'g_part',
        'cc',
        'comentario',
        'is_active_centro_costo'
    )
    search_fields=['id_centro_costo']
#PREPARADOR
"""class PreparadorAdmin(admin.ModelAdmin):
    list_display = (
        'id_preparador',
        'nombre_preparador',
        'is_active_preparador'
    )"""

#BODEGA
class BodegaAdmin(admin.ModelAdmin):
    list_display = (
        'id_bodega',
        'nombre_bodega',
        'is_active_bodega'
    )
    search_fields=['id_bodega']
#CATEGORIA
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id_categoria',
        'nombre_categoria',
        'is_active_categoria'
    )
#RECURSO
class RecursoAdmin(admin.ModelAdmin):
    list_display = (
        'id_recurso',
        'categoria_recurso',
        'nombre_recurso',
        'unidad',
        'is_active_recurso'
    )
    search_fields =['id_recurso', 'nombre_recurso']
#SOLICITUD RECURSO INLINE
class Solicitud_RecursoInline(admin.TabularInline):
    model = Solicitud_Recurso
    extra = 2
    search_fields = ['id_recurso']
    autocomplete_fields = ['id_recurso']
#SOLICITUD
class SolicitudAdmin(admin.ModelAdmin):
    search_fields=['id_centro_costo','bodega','solicitante', 'preparador']
    autocomplete_fields=['id_centro_costo','bodega','solicitante', 'preparador']
    inlines = [Solicitud_RecursoInline,]
    list_display = (
        'id_solicitud',
        'solicitante',
        'fecha_solicitud',
        'unidad_negocio',
        'id_centro_costo',
        #'edificio',
        'piso',
        'preparador',
        'bodega',
        'estado_solicitud',
        'observacion',
        'is_active_solicitud'
    )
    fieldsets = (('Datos de la Solicitud', 
                    {'fields':
                        (('solicitante', 'fecha_solicitud'), ('id_centro_costo', 'unidad_negocio', 'piso')),
                            'classes':'collapse'}),
                 ('Asignaciones de la solicitud', 
                    {'fields': 
                        (('preparador', 'bodega'), ('estado_solicitud', 'observacion', 'is_active_solicitud')),
                            'classes':'collapse wide'}),)
    
"""class SolicitudAdmin(admin.ModelAdmin):
    exclude = ('is_active_solicitud',)"""
# SOLICITUD RECURSO
class Solicitud_RecursoAdmin(admin.ModelAdmin):
    list_display = (
        'id_solicitud_recurso',
        'id_solicitud',
        'id_recurso',
        'cantidad_solicitada',
        'estado_despacho'
    )

admin.site.register(Unidad_Negocio, Unidad_NegocioAdmin)
admin.site.register(Centro_Costo, Cetro_CostoAdmin)
#admin.site.register(Preparador, PreparadorAdmin)
admin.site.register(Bodega, BodegaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Solicitud_Recurso, Solicitud_RecursoAdmin)