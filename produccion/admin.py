from django.contrib import admin

# Register your models here.
from .models import Estilo, Malta_x_Receta, Lupulo_x_Receta, Agregados_x_Receta, Levadura_x_Receta, Receta

# Register your models here.
admin.site.register(Estilo)
admin.site.register(Malta_x_Receta)
admin.site.register(Lupulo_x_Receta)
admin.site.register(Agregados_x_Receta)
admin.site.register(Levadura_x_Receta)
admin.site.register(Receta)
