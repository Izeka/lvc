from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
# Create your views here.

class Proveedores(LoginRequiredMixin, ListView):
    model = Proveedor
    login_url = "/login/"
    template_name = "agenda/proveedores.html"
    context_object_name = 'proveedores'

class Clientes(LoginRequiredMixin, ListView):
    model = Cliente
    login_url = "/login/"
    template_name = "agenda/clientes.html"
    context_object_name = 'clientes'
