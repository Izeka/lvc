from django import forms
from .models import *

class InsumoForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Insumo

class LupuloForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Lupulo

class MaltaForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Malta

class LevaduraForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Levadura

class AgregadoForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Agregado

class FermentadorForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Fermentador

class BotellasForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Botellas

class BarrilForm(forms.ModelForm):
     class Meta:
        fields = "__all__"
        model = Barril
