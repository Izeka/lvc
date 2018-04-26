# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from agenda.views import Proveedor
from contabilidad.models import Compra

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}

# Create your models here.

TIPOS = (
        ('INSUMO', 'Insumo'),
        ('INGREDIENTE', 'Ingrediente'),
        ('EQUIPAMIENTO', 'Equipamiento'),
    )
UNIDADES = (
           ('Kg','Kilogramos'),
           ('g','Gramos'),
           ('l','Litros'),
)

PRESENTACIONES = (
           ('U','Unidad'),
           ('100G','100 Gramos'),
           ('500G','500 Gramos'),
           ('1K','1 Kg'),
           ('10K','10 Kg'),
           ('25K','25 Kg'),
           ('1L','1 Litro'),
           ('5L','5 Litros'),
)

class Insumo(models.Model):
    Nombre            = models.CharField(max_length=100, error_messages=my_default_errors)
    Tipo              = models.CharField(max_length=20, choices=TIPOS, error_messages=my_default_errors)
    Uso               = models.CharField(max_length=100, error_messages=my_default_errors, blank=True,null=True)
    Unidad_de_medida  = models.CharField(max_length=20, choices=UNIDADES,error_messages=my_default_errors, blank=True,null=True)
    Cantidad          = models.FloatField(error_messages=my_default_errors)
    Stock_minimo      = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Stock_maximo      = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)
    objects           = InheritanceManager()

    def __str__(self):
       return self.Nombre

class Lupulo(Insumo):
    Alfa_Acido        = models.FloatField( error_messages=my_default_errors,blank=True, null=True)

class Malta(Insumo):
    Ganancia    = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)
    Humedad     = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)
    Color       = models.CharField( max_length=10,error_messages=my_default_errors,blank=True, null=True)

class Levadura(Insumo):
    pass

class Agregado(Insumo):
    pass

class Barril(models.Model):
    Numero_serie    = models.CharField(max_length=10, error_messages=my_default_errors,primary_key=True)
    compra          = models.ForeignKey(Compra, error_messages=my_default_errors)
    Litros          = models.IntegerField( error_messages=my_default_errors)
    Ubicacion       = models.CharField( max_length=100,error_messages=my_default_errors,default="Keñua")
    p_unitario      = models.FloatField(error_messages=my_default_errors,default=1)
    Lleno           = models.BooleanField( error_messages=my_default_errors,default=False)
    Carbonatado     = models.BooleanField( error_messages=my_default_errors,default=False)
    Observaciones   = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __unicode__(self):
       return unicode(self.Numero_serie)

class Botellas(models.Model):
    Litros      = models.FloatField( error_messages=my_default_errors)
    compra      = models.ForeignKey(Compra, error_messages=my_default_errors)
    p_unitario  = models.FloatField(error_messages=my_default_errors)
    Cantidad    = models.FloatField( error_messages=my_default_errors)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __unicode__(self):
       return unicode(self.Numero_serie)

class Fermentador(models.Model):
    Numero_serie    = models.CharField(max_length=10, error_messages=my_default_errors,primary_key=True)
    compra          = models.ForeignKey(Compra, error_messages=my_default_errors)
    Litros          = models.FloatField( error_messages=my_default_errors)
    p_unitario      = models.FloatField(error_messages=my_default_errors)
    Lleno           = models.BooleanField( error_messages=my_default_errors,default=False)
    Observaciones   = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __unicode__(self):
       return unicode(self.Numero_serie)

class CompraInsumo(models.Model):
     compra          = models.ForeignKey(Compra, error_messages=my_default_errors)
     insumo          = models.ForeignKey(Insumo, error_messages=my_default_errors, related_name="add_insumo")
     presentacion    = models.CharField(max_length=20, choices=PRESENTACIONES,error_messages=my_default_errors,default="U")
     cantidad        = models.FloatField(error_messages=my_default_errors)
     p_unitario      = models.FloatField(error_messages=my_default_errors)
     subtotal        = models.FloatField(error_messages=my_default_errors)

     def __unicode__(self):
        return unicode(self.id)

     def save(self, *args, **kwargs):
         #Obtengo el insumo que se compro
         insumo = Insumo.objects.get(pk=self.insumo_id)
         #Obtengo la presentacion de la compra
         presentacion = str(self.presentacion)
         #Extraigo la unidad de presentacion (K, G, L)
         unidad = filter(str.isalpha, presentacion )
         #Extraigo la cantidad de la presentacion 10,25, 100 etc
         p_cantidad = int(filter(str.isdigit, presentacion))
         #Compruebo si el insumo comprado es un Lupulo o un agregado
         if any( [Lupulo.objects.filter(id=self.insumo_id), Agregado.objects.filter(id=self.insumo_id)] ):
           #si la compra fue de Kgs lo paso a gramos multiplicandolo por 1000
             if unidad == 'K':
                 p_cantidad = p_cantidad*1000
         #sumo la cantidad comprara a la cantidad actual del insumo
         insumo.Cantidad = insumo.Cantidad + int(self.cantidad)*p_cantidad
         #guardo el insumo
         insumo.save()
         return super(CompraInsumo, self).save(*args,**kwargs)
