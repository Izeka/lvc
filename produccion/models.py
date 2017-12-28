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

class Receta(models.Model):
    Nombre                 = models.CharField(max_length=100,error_messages=my_default_errors)
    Tipo                   = models.ForeignKey(Estilo,error_messages=my_default_errors)
    Litros                 = models.IntegerField(error_messages=my_default_errors)
    DI                     = models.CharField(max_length=100,error_messages=my_default_errors)
    DF                     = models.CharField(max_length=100,error_messages=my_default_errors)
    IBUs                   = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    EBC                    = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    Rendimiento            = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    Alcohol                = models.FloatField(error_messages=my_default_errors, blank=True,null=True)
    Temp_Maceracion        = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Maceracion      = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Filtrado        = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Lavado          = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Coccion         = models.IntegerField(error_messages=my_default_errors)
    Temp_Final             = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Fermentacion    = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
       return self.Nombre


class Malta_x_Receta(models.Model):
    Malta          = models.ForeignKey(Malta,error_messages=my_default_errors)
    Receta        = models.ForeignKey(Receta,error_messages=my_default_errors)
    Cantidad       = models.IntegerField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
      return str(self.id)

class Lupulo_x_Receta(models.Model):
    Lupulo         = models.ForeignKey(Lupulo,error_messages=my_default_errors)
    Receta         = models.ForeignKey(Receta,error_messages=my_default_errors)
    Cantidad       = models.IntegerField(max_length=100,error_messages=my_default_errors)
    Tiempo         = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
       return str(self.id)

class Levadura_x_Receta(models.Model):
    Levadura      = models.ForeignKey(Levadura,error_messages=my_default_errors)
    Receta        = models.ForeignKey(Receta,error_messages=my_default_errors)
    Cantidad      = models.IntegerField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
       return str(self.id)

class Agregados_x_Receta(models.Model):
    Agregados     = models.ForeignKey(Agregado,error_messages=my_default_errors)
    Receta        = models.ForeignKey(Receta,error_messages=my_default_errors)
    Cantidad      = models.IntegerField(max_length=100,error_messages=my_default_errors)
    Tiempo        = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
       return str(self.id)

class Coccion(models.Model):
    Nombre                 = models.CharField(max_length=100,error_messages=my_default_errors)
    Fecha                  = models.DateField(error_messages=my_default_errors,default=None)
    Receta                 = models.ForeignKey(Receta,error_messages=my_default_errors)
    DI                     = models.CharField(max_length=100,error_messages=my_default_errors)
    Temp_Maceracion        = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Maceracion      = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Filtrado        = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Lavado          = models.IntegerField(error_messages=my_default_errors)
    Tiempo_Coccion         = models.IntegerField(error_messages=my_default_errors)
    Temp_Final             = models.IntegerField(error_messages=my_default_errors)
    DF                     = models.CharField(max_length=100,error_messages=my_default_errors)
    Litros                 = models.IntegerField(error_messages=my_default_errors)
    Observaciones          = models.TextField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
       return unicode(self.id)


class Malta_x_Coccion(models.Model):
    Malta          = models.ForeignKey(Malta,error_messages=my_default_errors)
    Coccion        = models.ForeignKey(Coccion,error_messages=my_default_errors)
    Cantidad       = models.IntegerField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
      return str(self.id)

class Lupulo_x_Coccion(models.Model):
    Lupulo         = models.ForeignKey(Lupulo,error_messages=my_default_errors)
    Coccion        = models.ForeignKey(Coccion,error_messages=my_default_errors)
    Cantidad       = models.IntegerField(max_length=100,error_messages=my_default_errors)
    Tiempo         = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
       return str(self.id)

class Levadura_x_Coccion(models.Model):
    Levadura      = models.ForeignKey(Levadura,error_messages=my_default_errors)
    Coccion       = models.ForeignKey(Coccion,error_messages=my_default_errors)
    Cantidad      = models.IntegerField(max_length=100,error_messages=my_default_errors)

    def __str__(self):
       return str(self.id)

class Agregados_x_Coccion(models.Model):
    Agregados     = models.ForeignKey(Agregado,error_messages=my_default_errors)
    Coccion       = models.ForeignKey(Coccion,error_messages=my_default_errors)
    Cantidad      = models.IntegerField(max_length=100,error_messages=my_default_errors)
    Tiempo        = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
       return str(self.id)
