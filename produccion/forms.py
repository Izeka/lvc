# -*- coding: utf-8 -*-
from django import forms
from produccion.models import *

maltaFormSet = forms.modelformset_factory(Malta_x_Receta, fields ="__all__")
lupuloFormSet = forms.modelformset_factory(Lupulo_x_Receta, fields ="__all__")
agregadoFormSet = forms.modelformset_factory(Agregados_x_Receta, fields ="__all__")
