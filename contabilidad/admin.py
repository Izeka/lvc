from django.contrib import admin
# Register your models here.
from .models import Compra, CompraInsumo

# Register your models here.
admin.site.register(Compra)
admin.site.register(CompraInsumo)
