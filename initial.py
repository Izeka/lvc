import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mosto.settings")
django.setup()

from inventario.models import Tipo, Forma, Unidad_medida

unidades= ["Litros", "MiliLitros", "Gramos","Kilogramos","Unidad"]

for u in unidades:
  Unidad_medida.objects.create(valor=u)


#tipos= ["Equipamiento", "Ingrediente"]

#for t in tipos:
 # Tipo.objects.create(valor=t)


formas= ["Liquido", "Polvo", "Grano", "Molido"]

for f in formas:
  Forma.objects.create(valor=f)
