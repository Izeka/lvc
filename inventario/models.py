# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}

# Create your models here.
class Unidad_medida(models.Model):
    valor = models.CharField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
       return self.valor

class Forma(models.Model):
   valor = models.CharField(max_length=100,error_messages=my_default_errors)

   def __str__(self):
      return self.valor

class Tipo(models.Model):
   valor = models.CharField(max_length=100,error_messages=my_default_errors)

   def __str__(self):
       return self.valor

class Proveedor(models.Model):
    Nombre         = models.CharField(max_length=100,error_messages=my_default_errors)
    Representante  = models.CharField(max_length=100,error_messages=my_default_errors)
    Telefono       = models.IntegerField(error_messages=my_default_errors)
    Direccion      = models.CharField(max_length=100,error_messages=my_default_errors)
    Email          = models.EmailField(max_length=100,error_messages=my_default_errors, blank=True,null=True)

    def __str__(self):
       return self.Nombre

class Cliente(models.Model):
    Nombre         = models.CharField(max_length=100,error_messages=my_default_errors)
    Representante  = models.CharField(max_length=100,error_messages=my_default_errors)
    Telefono       = models.IntegerField(error_messages=my_default_errors)
    Direccion      = models.CharField(max_length=100,error_messages=my_default_errors)
    Email          = models.EmailField(max_length=100,error_messages=my_default_errors, blank=True,null=True)

    def __str__(self):
       return self.Nombre


class Insumo(models.Model):
    Nombre            = models.CharField(max_length=100, error_messages=my_default_errors)
    Tipo              = models.ForeignKey(Tipo, error_messages=my_default_errors)
    Origen            = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    Forma             = models.ForeignKey(Forma, error_messages=my_default_errors, blank=True,null=True)
    Uso               = models.CharField(max_length=100, error_messages=my_default_errors, blank=True,null=True)
    Vencimiento       = models.DateField('Fecha de Vencimiento',error_messages=my_default_errors,blank=True,null=True)
    Proveedor         = models.ForeignKey(Proveedor, error_messages=my_default_errors)
    Unidad_de_medida  = models.ForeignKey(Unidad_medida, error_messages=my_default_errors, blank=True,null=True)
    Cantidad          = models.IntegerField(error_messages=my_default_errors)
    Precio_unidad     = models.FloatField(error_messages=my_default_errors)
    Stock_minimo      = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Stock_maximo      = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)
    objects           = InheritanceManager()

    def __str__(self):
       return self.Nombre

class Lupulo(Insumo):
    Alfa_Acido        = models.FloatField( error_messages=my_default_errors)

class Malta(Insumo):
    DBFG      = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)
    MC        = models.CharField( max_length=10,error_messages=my_default_errors)
    EBC       = models.CharField( max_length=10,error_messages=my_default_errors)

class Levadura(Insumo):
    pass

class Agregado(Insumo):
    pass


class Barril(Insumo):
    Litros          = models.IntegerField( error_messages=my_default_errors)
    Numero_serie    = models.IntegerField( error_messages=my_default_errors,blank=True,null=True)
    Ubicacion       = models.CharField( max_length=100,error_messages=my_default_errors,blank=True,null=True)
    Diametro        = models.IntegerField( error_messages=my_default_errors)
    Altura          = models.IntegerField( error_messages=my_default_errors)
    Material        = models.CharField( max_length=100,error_messages=my_default_errors)
    Lleno           = models.BooleanField( error_messages=my_default_errors,default=False)

class Botella(Insumo):
    Litros    = models.FloatField( error_messages=my_default_errors)
    Numero_serie    = models.IntegerField( error_messages=my_default_errors,blank=True,null=True)
    Llenas    = models.IntegerField( error_messages=my_default_errors, default=0)

class Fermentador(Insumo):
    Litros    = models.FloatField( error_messages=my_default_errors)
    Numero_serie    = models.IntegerField( error_messages=my_default_errors,blank=True,null=True)
    Material        = models.CharField( max_length=100,error_messages=my_default_errors,blank=True,null=True)
    Lleno     = models.BooleanField( error_messages=my_default_errors,default=False)
