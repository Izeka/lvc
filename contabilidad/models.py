# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from agenda.models import Proveedor

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}
TIPOS = (
        ('INS', 'Insumo'),
        ('ING', 'Ingrediente'),
        ('EQ', 'Equipamiento'),
    )
class Compra(models.Model):
    fecha_compra      = models.DateField('Fecha de Compra',error_messages=my_default_errors)
    producto          = models.CharField(max_length=20,  error_messages=my_default_errors)
    factura           = models.CharField(max_length=100,error_messages=my_default_errors, blank=True)
    proveedor         = models.ForeignKey(Proveedor,error_messages=my_default_errors)
    comprador         = models.ForeignKey(User, error_messages=my_default_errors)
    importe_total     = models.FloatField(error_messages=my_default_errors)
    observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True)

    def __str__(self):
      return str(self.id)

class Servicio(models.Model):
     compra           = models.ForeignKey(Compra, error_messages=my_default_errors)
     detalle          = models.CharField(max_length=100,error_messages=my_default_errors, blank=True)
     precio_unitario  = models.FloatField(error_messages=my_default_errors)
