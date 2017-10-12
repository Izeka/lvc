from django.shortcuts import render
from django.views.generic import ListView
from .models import Compra
# Create your views here.

class Compras(ListView):
    model = Compra
    template_name = "contabilidad/compras.html"
    context_object_name = 'compras'


