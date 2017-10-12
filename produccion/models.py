from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from inventario.models import Malta, Lupulo, Levadura, Agregado

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}

class Estilo(models.Model):
    Nombre    = models.CharField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
       return self.Nombre


class Malta_x_Receta(models.Model):
    Malta          = models.ForeignKey(Malta,error_messages=my_default_errors)
    Cantidad       = models.IntegerField(max_length=100,error_messages=my_default_errors)
 

class Lupulo_x_Receta(models.Model):
    Lupulo         = models.ForeignKey(Lupulo,error_messages=my_default_errors)
    Cantidad       = models.IntegerField(max_length=100,error_messages=my_default_errors)
    Tiempo         = models.IntegerField(error_messages=my_default_errors)


class Levadura_x_Receta(models.Model):
    Levadura      = models.ForeignKey(Levadura,error_messages=my_default_errors)
    Cantidad      = models.IntegerField(max_length=100,error_messages=my_default_errors)

class Agregados_x_Receta(models.Model):
    Agregados     = models.ForeignKey(Agregado,error_messages=my_default_errors,default=None)
    Cantidad      = models.IntegerField(max_length=100,error_messages=my_default_errors)

class Receta(models.Model):
    Nombre                 = models.CharField(max_length=100,error_messages=my_default_errors)
    Tipo                   = models.ForeignKey(Estilo,error_messages=my_default_errors)
    Litros                 = models.IntegerField(error_messages=my_default_errors)
    DI                     = models.IntegerField(error_messages=my_default_errors)
    DF                     = models.IntegerField(error_messages=my_default_errors)
    IBUs                   = models.FloatField(error_messages=my_default_errors, blank=True,null=True)
    EBC                    = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Eficiencia             = models.IntegerField(error_messages=my_default_errors, blank=True,null=True)
    Alochol                = models.FloatField(error_messages=my_default_errors, blank=True,null=True)
    Temp_Maceracion        = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Maceracion      = models.IntegerField(error_messages=my_default_errors)
    Temp_Coccion           = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Coccion         = models.IntegerField(error_messages=my_default_errors)
    Temp_Fermantacion      = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Fermentacion    = models.IntegerField(error_messages=my_default_errors)
    Malta                  = models.ForeignKey(Malta_x_Receta,error_messages=my_default_errors)
    Lupulo                 = models.ForeignKey(Lupulo_x_Receta,error_messages=my_default_errors)
    Agregado               = models.ForeignKey(Agregados_x_Receta,error_messages=my_default_errors)
    Levadura               = models.ForeignKey(Levadura_x_Receta,error_messages=my_default_errors)

    def __unicode__(self):
       return self.id



