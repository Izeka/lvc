from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from inventario.models import Insumo, Proveedor, Unidad_medida

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}

class Compra(models.Model):
    Fecha_compra      = models.DateField('Fecha de Compra',error_messages=my_default_errors)
    Fecha_entrega     = models.DateField('Fecha de Entrega',error_messages=my_default_errors)
    Producto          = models.ForeignKey(Insumo, error_messages=my_default_errors)
    Factura           = models.CharField(max_length=100,error_messages=my_default_errors, blank=True,null=True)
    Proveedor         = models.ForeignKey(Proveedor,error_messages=my_default_errors)
    Comprador         = models.ForeignKey(User, error_messages=my_default_errors)
    Unidad_de_medida  = models.ForeignKey(Unidad_medida, error_messages=my_default_errors, blank=True,null=True)
    Cantidad          = models.IntegerField(error_messages=my_default_errors)
    Precio_unidad     = models.FloatField(error_messages=my_default_errors)
    Precio_total      = models.FloatField(error_messages=my_default_errors)
    Observaciones     = models.TextField(max_length=300,error_messages=my_default_errors, blank=True,null=True)

    def __str__(self):
      return str(self.id)
