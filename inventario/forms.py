from django import forms
from .models import *

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
