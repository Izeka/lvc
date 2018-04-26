# -*- coding: utf-8 -*-
from django import forms
from inventario.models import *

maltaFormSet = forms.modelformset_factory(Malta, fields ="__all__")
lupuloFormSet = forms.modelformset_factory(Lupulo, fields ="__all__")
agregadoFormSet = forms.modelformset_factory(Agregado, fields ="__all__")
