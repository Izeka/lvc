from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from inventario.models import *

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}


class Receta(models.Model):
    nombre = models.CharField(max_length=100, error_messages=my_default_errors)
    litros = models.IntegerField(error_messages=my_default_errors)
#    DI                     = models.CharField(max_length=100,error_messages=my_default_errors)
    DF = models.CharField(
        max_length=100, error_messages=my_default_errors, blank=True)
    IBUs = models.CharField(
        max_length=100, error_messages=my_default_errors, blank=True, null=True)
    color = models.CharField(
        max_length=100, error_messages=my_default_errors, blank=True, null=True)
#    Temp_Maceracion        = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Maceracion      = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Filtrado        = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Lavado          = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Coccion         = models.IntegerField(error_messages=my_default_errors)
#    Temp_Final             = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Fermentacion    = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
        return self.nombre


class Malta_x_Receta(models.Model):
    malta = models.ForeignKey(Malta, error_messages=my_default_errors)
    receta = models.ForeignKey(Receta, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)


class Lupulo_x_Receta(models.Model):
    lupulo = models.ForeignKey(Lupulo, error_messages=my_default_errors)
    receta = models.ForeignKey(Receta, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)
#    tiempo         = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)


class Levadura_x_Receta(models.Model):
    levadura = models.ForeignKey(Levadura, error_messages=my_default_errors)
    receta = models.ForeignKey(Receta, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)


class Agregado_x_Receta(models.Model):
    agregado = models.ForeignKey(Agregado, error_messages=my_default_errors)
    receta = models.ForeignKey(Receta, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)
#    tiempo        = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)


class Coccion(models.Model):
    lote = models.CharField(max_length=20,error_messages=my_default_errors,primary_key=True)
    fecha = models.DateField(error_messages=my_default_errors, default=None)
    receta = models.ForeignKey(
        Receta, error_messages=my_default_errors, related_name="recetas")
#    Temp_Maceracion        = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Maceracion      = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Filtrado        = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Lavado          = models.IntegerField(error_messages=my_default_errors)
#    Tiempo_Coccion         = models.IntegerField(error_messages=my_default_errors)
#    Temp_Final             = models.IntegerField(error_messages=my_default_errors)
    DF = models.CharField(
        max_length=100, error_messages=my_default_errors, blank=True)
    litros = models.IntegerField(error_messages=my_default_errors)
    observaciones = models.TextField(
        max_length=100, error_messages=my_default_errors, blank=True, null=True)

    def __str__(self):
        return unicode(self.lote)




class Malta_x_Coccion(models.Model):
    malta = models.ForeignKey(Malta, error_messages=my_default_errors)
    coccion = models.ForeignKey(Coccion, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        malta = Insumo.objects.get(pk=self.malta.id)
        try:
            malta_coccion = Malta_x_Coccion.objects.get(pk=self.id)
            nueva_cantidad_coccion = self.cantidad - malta_coccion.cantidad
            malta.cantidad = malta.cantidad - nueva_cantidad_coccion
        except:
            malta.cantidad = malta.cantidad - int(self.cantidad)
        malta.save()
        return super(Malta_x_Coccion, self).save(*args, **kwargs)


class Lupulo_x_Coccion(models.Model):
    lupulo = models.ForeignKey(Lupulo, error_messages=my_default_errors)
    coccion = models.ForeignKey(Coccion, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)
#    tiempo         = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        lupulo = Insumo.objects.get(pk=self.lupulo.id)
        # Si la receta existe, actualizo la cantidad de insumo
        try:
            # busco la cantidad de lupulo actual en la coccion
            lupulo_coccion = Lupulo_x_Coccion.objects.get(pk=self.id)
            # resto a la nueva cantidad la cantidad anterior de lupulo
            nueva_cantidad_coccion = self.cantidad - lupulo_coccion.cantidad
            # actualizo la cantidad del lupulo en el inventario
            lupulo.cantidad = lupulo.cantidad - nueva_cantidad_coccion
        except:
            # si no existe, resto la cantidad de lupulo en la reseta en el inventario
            lupulo.cantidad = lupulo.cantidad - int(self.cantidad)
        # guardo la instancia del lupulo
        lupulo.save()
        return super(Lupulo_x_Coccion, self).save(*args, **kwargs)


class Levadura_x_Coccion(models.Model):
    levadura = models.ForeignKey(Levadura, error_messages=my_default_errors)
    coccion = models.ForeignKey(Coccion, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        levadura = Insumo.objects.get(pk=self.levadura.id)
        # Si la receta existe, actualizo la cantidad de insumo
        try:
            # busco la cantidad de levadura actual en la coccion
            levadura_coccion = Levadura_x_Coccion.objects.get(pk=self.id)
            # resto a la nueva cantidad la cantidad anterior de levadura
            nueva_cantidad_coccion = self.cantidad - levadura_coccion.cantidad
            # actualizo la cantidad del levadura en el inventario
            levadura.cantidad = levadura.cantidad - nueva_cantidad_coccion
        except:
            # si no existe, resto la cantidad de levadura en la reseta en el inventario
            levadura.cantidad = levadura.cantidad - int(self.cantidad)
        # guardo la instancia del levadura
        levadura.save()
        return super(Levadura_x_Coccion, self).save(*args, **kwargs)


class Agregado_x_Coccion(models.Model):
    agregado = models.ForeignKey(Agregado, error_messages=my_default_errors)
    coccion = models.ForeignKey(Coccion, error_messages=my_default_errors)
    cantidad = models.FloatField(error_messages=my_default_errors)
    #tiempo        = models.IntegerField(error_messages=my_default_errors)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        agregado = Insumo.objects.get(pk=self.agregado.id)
        # Si la receta existe, actualizo la cantidad de insumo
        try:
            # busco la cantidad de agregado actual en la coccion
            agregado_coccion = Agregado_x_Coccion.objects.get(pk=self.id)
            # resto a la nueva cantidad la cantidad anterior de agregado
            nueva_cantidad_coccion = self.cantidad - agregado_coccion.cantidad
            # actualizo la cantidad del agregado en el inventario
            agregado.cantidad = agregado.cantidad - nueva_cantidad_coccion
        except:
            # si no existe, resto la cantidad de agregado en la reseta en el inventario
            agregado.cantidad = agregado.cantidad - int(self.cantidad)
        # guardo la instancia del agregado
        agregado.save()
        return super(Agregado_x_Coccion, self).save(*args, **kwargs)

class Fermentacion(models.Model):
    lote = models.ForeignKey(Coccion, error_messages=my_default_errors)
    fermentador = models.ForeignKey(
        Fermentador, error_messages=my_default_errors)
    fecha_inicio = models.DateField(
        error_messages=my_default_errors, default=None)
    fecha_final = models.DateField(
        error_messages=my_default_errors, default=None)
    litros = models.IntegerField(error_messages=my_default_errors)
    observaciones = models.TextField(
        max_length=100, error_messages=my_default_errors)

class Embarrilado(models.Model):
    lote = models.ForeignKey(Fermentacion, error_messages=my_default_errors)
    barril = models.ForeignKey(
        Barril, error_messages=my_default_errors)
    fecha = models.DateField(
        error_messages=my_default_errors, default=None)
    litros = models.IntegerField(error_messages=my_default_errors)
    observaciones = models.TextField(
        max_length=100, error_messages=my_default_errors)

class Embotellado(models.Model):
    lote = models.ForeignKey(Fermentacion, error_messages=my_default_errors)
    pallet = models.ForeignKey(
        Pallet, error_messages=my_default_errors)
    fecha = models.DateField(
        error_messages=my_default_errors, default=None)
    cantidad = models.IntegerField(error_messages=my_default_errors)
    observaciones = models.TextField(
        max_length=100, error_messages=my_default_errors)
