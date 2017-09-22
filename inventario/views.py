# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from .models import Insumo, Proveedor, Cliente

# Create your views here.
class Ingredientes(ListView):
    model = Insumo
    template_name = "inventario/ingredientes.html"
    context_object_name = 'lupulos'

    def get_queryset(self):
        queryset=Insumo.objects.all().filter(lupulo__Tipo=2)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Ingredientes, self).get_context_data(**kwargs)
        context['maltas'] = Insumo.objects.all().filter(malta__Tipo=2)
        context['levaduras'] = Insumo.objects.all().filter(levadura__Tipo=2)
        context['clarificantes'] = Insumo.objects.all().filter(clarificante__Tipo=2)
        return context

class Equipamiento(ListView):
    model = Insumo
    template_name = "inventario/equipamiento.html"
    context_object_name = 'equipamiento'

    def get_queryset(self):
        queryset=Insumo.objects.all().filter(Tipo=1)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Equipamiento, self).get_context_data(**kwargs)
        context['barriles'] = Insumo.objects.all().filter(barril__Tipo=1)
        context['fermentadores'] = Insumo.objects.all().filter(fermentador__Tipo=1)
        context['botellas'] = Insumo.objects.all().filter(botella__Tipo=1)
        context['varios']= Insumo.objects.all().exclude(barril__Tipo=1).filter(fermentador__Tipo=1).filter(botella__Tipo=1)

        return context


class Insumos(ListView):
    model = Insumo
    template_name = "inventario/insumos.html"
    context_object_name = 'insumos'

    def get_queryset(self):
        queryset=Insumo.objects.all().filter(Tipo=3)
        return queryset

class Proveedores(ListView):
    model = Insumo
    template_name = "inventario/proveedores.html"
    context_object_name = 'proveedores'

    def get_queryset(self):
        queryset=Proveedor.objects.all()
        return queryset

class Clientes(ListView):
    model = Insumo
    template_name = "inventario/clientes.html"
    context_object_name = 'clientes'

    def get_queryset(self):
        queryset=Cliente.objects.all()
        return queryset

