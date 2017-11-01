# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import *

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
        context['agregados'] = Insumo.objects.all().filter(agregado__Tipo=2)
        return context

class Editar_ingrediente(UpdateView):
    model = Insumo
    fields= '__all__'
    template_name="inventario/ingrediente_form.html"
    form_class = {
        Lupulo: LupuloForm,
        Malta: MaltaForm,
        Levadura: LevaduraForm,
        Agregado: AgregadoForm,
    }

    def get_form_class(self):
       return self.form_class[self.object.__class__]

    def get_queryset(self):
      return self.model.objects.select_subclasses()

    def get_context_data(self, **kwargs):
        context = super(Editar_ingrediente, self).get_context_data(**kwargs)
        context['insumo'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect('/ingredientes')

class Nuevo_lupulo(CreateView):
    model= Lupulo
    fields= '__all__'
    template_name="inventario/ingrediente_nuevo.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/ingredientes')

class Nueva_malta(CreateView):
    model = Malta
    fields= '__all__'
    template_name="inventario/ingrediente_nuevo.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/ingredientes')

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
    model = Proveedor
    template_name = "inventario/proveedores.html"
    context_object_name = 'proveedores'

class Clientes(ListView):
    model = Cliente
    template_name = "inventario/clientes.html"
    context_object_name = 'clientes'
