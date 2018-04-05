from django.db import models

my_default_errors = {
    'required': 'Este valor es requerido',
    'invalid': 'Ingrese un valor valido',
    'unique': 'Este valor ya fue utilizado'
}

# Create your models here.
class Proveedor(models.Model):
    Nombre         = models.CharField(max_length=100,error_messages=my_default_errors)
    Representante  = models.CharField(max_length=100,error_messages=my_default_errors,blank=True,null=True)
    Rubro          = models.CharField(max_length=100,error_messages=my_default_errors,blank=True,null=True)
    Telefono       = models.IntegerField(error_messages=my_default_errors)
    Direccion      = models.CharField(max_length=100,error_messages=my_default_errors,blank=True,null=True)
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
