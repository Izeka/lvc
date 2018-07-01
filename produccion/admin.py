from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Lupulo_x_Receta)
admin.site.register(Lupulo_x_Coccion)
admin.site.register(Malta_x_Receta)
admin.site.register(Malta_x_Coccion)
admin.site.register(Agregado_x_Receta)
admin.site.register(Receta)
admin.site.register(Coccion)
admin.site.register(Fermentacion)
admin.site.register(Maduracion)
admin.site.register(fermentacion_x_madurador)
admin.site.register(Embarrilado)
