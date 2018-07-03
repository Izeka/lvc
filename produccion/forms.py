# -*- coding: utf-8 -*-
from django import forms
from django.db.models import F
from produccion.models import *


class EmbarriladoForm(forms.ModelForm):
    class Meta:
        model = Embarrilado
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmbarriladoForm, self).__init__(*args, **kwargs)
        self.fields["barril"].queryset = Barril.objects.filter(lleno=False)
        self.fields["lote"].queryset = Maduracion.objects.filter(
            litros__gt=F('embarrilados'))

    # antes de guardar el form, cualculo la cantidad de litros segun la cantidad de barriles
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
        self.fields["fermentacion"].queryset = Fermentacion.objects.filter(
            madurado=False)


maltaFormSet = forms.inlineformset_factory(
    Coccion, Malta_x_Coccion, fields="__all__")
lupuloFormSet = forms.inlineformset_factory(
    Coccion, Lupulo_x_Coccion, fields="__all__")
levaduraFormSet = forms.inlineformset_factory(
    Coccion, Levadura_x_Coccion, fields="__all__")
agregadoFormSet = forms.inlineformset_factory(
    Coccion, Agregado_x_Coccion, fields="__all__")
