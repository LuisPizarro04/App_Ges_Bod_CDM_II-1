from django.db import models


is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES =[(is_active, 'Activo'),
                    (is_inactive, 'Inactivo'),]

# MODELO: UNIDAD DE NEGOCIO
class Unidad_Negocio (models.Model):
    id_unidad_negocio = models.AutoField(primary_key=True)
    nombre_unidad_negocio = models.CharField(max_length=100, blank=False, null=False)
    is_active_unidad_negocio = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)
    
    def __str__(self):
        return self.nombre_unidad_negocio

# MODELO: CENTRO DE COSTOS
class Centro_Costo (models.Model):
    id_centro_costo = models.AutoField(primary_key=True)
    nombre_centro_costo = models.CharField(max_length=100, blank=False, null=False)
    is_active_unidad_negocio = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)
    unidad_negocio = models.ForeignKey(Unidad_Negocio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_centro_costo

#MODELO: PREPARADOR
class Preparador (models.Model):
    id_preparador = models.AutoField(primary_key=True)
    nombre_preparador = models.CharField(max_length=100, blank=False, null=False)
    is_active_preparador = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)

    def __str__(self):
        return self.nombre_preparador

#MODELO: SUPERVISOR
class Supervisor (models.Model):
    id_supervisor = models.AutoField(primary_key=True)
    nombre_supervisor = models.CharField(max_length=100, blank=False, null=False)
    is_active_supervisor = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)
    area_supervisor = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre_supervisor

#MODELO:BODEGA
class Bodega (models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=100, blank=False, null=False)
    is_active_bodega = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)

    def __str__(self):
        return self.nombre_bodega

#MODELO:CATEGORIA
class Categoria (models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100, blank=False, null=False)
    is_active_categoria = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)

    def __str__(self):
        return self.nombre_categoria

#MODELO:RECURSO
unidad_1 = 'Unidad 1'
unidad_2 = 'Unidad 2'
unidad_3 = 'Unidad 3'

UNIDADES_CHOICES = [(unidad_1, 'Unidad 1'), 
                (unidad_2, 'Unidad 2'), 
                (unidad_3, 'Unidad 3'), ]

class Recurso (models.Model):
    id_bodega = models.AutoField(primary_key=True)
    categoria_recurso = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre_recurso = models.CharField(max_length=100, blank=False, null=False)
    unidad = models.CharField(max_length=10, blank=False, null=False, choices=UNIDADES_CHOICES, default=unidad_1)
    is_active_recurso = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)

    def __str__(self):
        return self.nombre_recurso

#MODELO: SOLICITUD
estado_1 = 'Pendiente'
estado_2 = 'Entregado'
estado_3 = 'Rechazado'

ESTADOS_CHOICES = [(estado_1, 'Pendiente'), 
                (estado_2, 'Entregado'), 
                (estado_3, 'Rechazado'), ]  
class Solicitud (models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    is_active_solicitud = models.CharField(max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES, default=is_active)
    solicitante = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    preparador = models.ForeignKey(Preparador, on_delete=models.CASCADE)
    estado_solicitud = models.CharField(max_length=10, blank=False, null=False, choices=ESTADOS_CHOICES, default=estado_1)
    fecha_solicitud = models.DateField()

#MODELO: SOLICITUD_RECURSO
despacho_1 = 'No realizado'
despacho_2 = 'Realizado'

DESPACHO_CHOICES = [(despacho_1, 'No realizado'), 
                    (despacho_2, 'Realizado'),]
class Solicitud_Recurso (models.Model):
    id_solicitud_recurso = models.AutoField(primary_key=True)
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    id_recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    id_centro_costo = models.ForeignKey(Centro_Costo, on_delete=models.CASCADE)
    cantidad_solicitada = models.IntegerField()
    estado_despacho = models.CharField(max_length=10, blank=False, null=False, choices=DESPACHO_CHOICES, default=despacho_1)