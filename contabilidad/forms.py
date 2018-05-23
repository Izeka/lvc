# -*- coding: utf-8 -*-
from django import forms
from inventario.models import *
from .models import Compra, Servicio

BarrilFormSet = forms.inlineformset_factory(Compra, Barril, fields="__all__",extra=0)
PalletFormSet = forms.inlineformset_factory(Compra, Pallet, fields="__all__",extra=0)
InsumoFormSet = forms.inlineformset_factory(Compra,CompraInsumo, fields="__all__",extra=0)
ServicioFormSet = forms.inlineformset_factory(Compra, Servicio, fields="__all__",extra=0)
FermentadorFormSet = forms.inlineformset_factory(Compra, Fermentador, fields="__all__",extra=0)
