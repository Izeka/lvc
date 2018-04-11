# -*- coding: utf-8 -*-
from django import forms
from inventario.models import Barril
from .models import Compra


BarrilFormSet = forms.inlineformset_factory(Compra, Barril, fields="__all__",extra=0)
