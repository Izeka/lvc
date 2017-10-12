from django import forms
from django.core.urlresolvers import reverse_lazy

from django_addanother.widgets import AddAnotherWidgetWrapper, AddAnotherEditSelectedWidgetWrapper

from .models import Receta

class RecetaForm(forms.ModelForm):
#Agrego el widget "Agregar Otro" al campo muestras en el formulario de Solicitudes
    class Meta:
        model = Receta
        fields = "__all__"
        widgets = {
                'Tipo': AddAnotherWidgetWrapper(
                    forms.Select,
                    reverse_lazy('add_receta'),
                    )
                }
