# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from agenda.views import Proveedor

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

class Insumo(models.Model):
    Nombre            = models.CharField(max_length=100, error_messages=my_default_errors)
    Tipo              = models.ForeignKey(Tipo, error_messages=my_default_errors)
    #Origen            = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    #Forma             = models.ForeignKey(Forma, error_messages=my_default_errors, blank=True,null=True)
    Uso               = models.CharField(max_length=100, error_messages=my_default_errors, blank=True,null=True)
    Unidad_de_medida  = models.ForeignKey(Unidad_medida, error_messages=my_default_errors, blank=True,null=True)
    Cantidad          = models.IntegerField(error_messages=my_default_errors)
    Stock_minimo      = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Stock_maximo      = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)
    objects           = InheritanceManager()

    def __str__(self):
       return self.Nombre

class Lupulo(Insumo):
    Alfa_Acido        = models.FloatField( error_messages=my_default_errors,blank=True, null=True)

class Malta(Insumo):
    DBFG      = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)
    MC        = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)
    EBC       = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)

class Levadura(Insumo):
    pass

class Agregado(Insumo):
    pass

class Barril(models.Model):
    Numero_serie    = models.IntegerField( error_messages=my_default_errors,blank=True,null=True)
    Litros          = models.IntegerField( error_messages=my_default_errors)
    Ubicacion       = models.CharField( max_length=100,error_messages=my_default_errors,blank=True,null=True)
    Diametro        = models.IntegerField( error_messages=my_default_errors,blank=True, null=True)
    Altura          = models.IntegerField( error_messages=my_default_errors,blank=True, null=True)
    Material        = models.CharField( max_length=100,error_messages=my_default_errors,blank=True, null=True)
    Lleno           = models.BooleanField( error_messages=my_default_errors,default=False)
    Observaciones   = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __unicode__(self):
       return unicode(self.id)

class Botella(models.Model):
    Litros    = models.FloatField( error_messages=my_default_errors)
    Cantidad    = models.FloatField( error_messages=my_default_errors)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __unicode__(self):
       return unicode(self.id)

class Fermentador(models.Model):
    Numero_serie    = models.IntegerField( error_messages=my_default_errors,blank=True,null=True)
    Litros    = models.FloatField( error_messages=my_default_errors)
    Material        = models.CharField( max_length=100,error_messages=my_default_errors,blank=True,null=True)
    Lleno     = models.BooleanField( error_messages=my_default_errors,default=False)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __unicode__(self):
       return unicode(self.id)
