# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from inventario.models import *

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}

class Compra(models.Model):
    Fecha_compra      = models.DateField('Fecha de Compra',error_messages=my_default_errors)
    Factura           = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    Proveedor         = models.ForeignKey(Proveedor,error_messages=my_default_errors)
    Comprador         = models.ForeignKey(User, error_messages=my_default_errors)
    Importe_Total     = models.FloatField(error_messages=my_default_errors)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __str__(self):
      return str(self.id)

PRESENTACIONES = (
           ('U','Unidad'),
           ('1K','1 Kg'),
           ('10K','10 Kg'),
           ('25K','25 Kg'),
           ('1L','1 Litro'),
           ('5L','5 Litros'),
)
class CompraInsumo(models.Model):
     compra          = models.ForeignKey(Compra, error_messages=my_default_errors)
     insumo          = models.ForeignKey(Insumo, error_messages=my_default_errors, related_name="add_insumo")
     presentacion    = models.CharField(max_length=20, choices=PRESENTACIONES,error_messages=my_default_errors,default="U")
     cantidad        = models.FloatField(error_messages=my_default_errors)
     p_unitario      = models.FloatField(error_messages=my_default_errors)
     subtotal        = models.FloatField(error_messages=my_default_errors)

class CompraBarril(models.Model):
     compra          = models.ForeignKey(Compra, error_messages=my_default_errors)
     barril          = models.ForeignKey(Barril, error_messages=my_default_errors, related_name="add_barril")
     presentacion    = models.CharField(max_length=20, choices=PRESENTACIONES,error_messages=my_default_errors,default="U")
     cantidad        = models.FloatField(error_messages=my_default_errors)
     p_unitario      = models.FloatField(error_messages=my_default_errors)
     subtotal        = models.FloatField(error_messages=my_default_errors)
