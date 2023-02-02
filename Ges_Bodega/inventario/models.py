from django.db import models

# Create your models here.

class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre_familia = models.CharField(max_length=100, blank=False, null=False)
    producto_hijo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    is_active = model.CharField(max_length=100, blank=False, null=False)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100, blank=False, null=False)
    is_active = model.CharField(max_length=100, blank=False, null=False)

class Inventario(models.Model):
    id_inventaro = models.AutoField(primary_key=True)
    fecha_inventario = models.DateField(blank=True, null=True)
    is_active = model.CharField(max_length=100, blank=False, null=False)
