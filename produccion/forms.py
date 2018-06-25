# -*- coding: utf-8 -*-
from django import forms
from django.db.models import F
from produccion.models import *

maltaFormSet = forms.modelformset_factory(Malta_x_Receta, fields ="__all__")
lupuloFormSet = forms.modelformset_factory(Lupulo_x_Receta, fields ="__all__")
levaduraFormSet = forms.modelformset_factory(Levadura_x_Receta, fields ="__all__")
agregadoFormSet = forms.modelformset_factory(Agregado_x_Receta, fields ="__all__")

class EmbarriladoForm(forms.ModelForm):
    class Meta:
        model = Embarrilado
        exclude = ['litros']

    def __init__(self, *args, **kwargs):
        super(EmbarriladoForm, self).__init__(*args, **kwargs)
        self.fields["barril"].queryset = Barril.objects.filter(lleno=False)
        self.fields["lote"].queryset = Maduracion.objects.filter(litros__gt=F('embarrilados'))


    #antes de guardar el form, cualculo la cantidad de litros segun la cantidad de barriles
    def clean(self):
        litros = 0
        for barril in self.cleaned_data['barril']:
            litros += barril.litros
        self.cleaned_data['litros'] = litros
        return self.cleaned_data

class FermentacionInlineForm(forms.ModelForm):
    class Meta:
        model = fermentacion_x_madurador
        fields = "__all__"

    # Reemplazo el queryset original para tener solo las fermentaciones no maduradas
    def __init__(self, *args, **kwargs):
        super(FermentacionInlineForm, self).__init__(*args, **kwargs)
        self.fields["fermentacion"].queryset = Fermentacion.objects.filter(madurado=False)
