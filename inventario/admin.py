# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Unidad_medida, Forma, Tipo, Proveedor, Insumo, Barril, Botella, Fermentador, Lupulo, Malta, Levadura, Clarificante

# Register your models here.
admin.site.register(Unidad_medida)
admin.site.register(Forma)
admin.site.register(Tipo)
admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Barril)
admin.site.register(Botella)
admin.site.register(Fermentador)
admin.site.register(Lupulo)
admin.site.register(Levadura)
admin.site.register(Clarificante)
