# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from inventario.models import Proveedor, Insumo

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

class CompraItem(models.Model):
     compra          = models.ForeignKey(Compra, error_messages=my_default_errors)
     insumo          = models.ForeignKey(Insumo, error_messages=my_default_errors, related_name="add_insumo")
     cantidad        = models.FloatField(error_messages=my_default_errors)
     p_unitario      = models.FloatField(error_messages=my_default_errors)
     subtotal       = models.FloatField(error_messages=my_default_errors)
