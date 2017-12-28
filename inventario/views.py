# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.forms import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# Create your views here.
class Ingredientes(LoginRequiredMixin, ListView):
    model = Insumo
    login_url = "/login/"
    template_name = "inventario/ingredientes.html"

    def get_context_data(self, **kwargs):
        context = super(Ingredientes, self).get_context_data(**kwargs)
        context['lupulos'] = Insumo.objects.all().filter(lupulo__Tipo=2)
        context['maltas'] = Insumo.objects.all().filter(malta__Tipo=2)
        context['levaduras'] = Insumo.objects.all().filter(levadura__Tipo=2)
        context['agregados'] = Insumo.objects.all().filter(agregado__Tipo=2)
        return context

class Equipamiento(ListView):
    model = Insumo
    template_name = "inventario/equipamiento.html"

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

class Editar_insumo(UpdateView):
    model = Insumo
    fields= '__all__'
    template_name="inventario/insumo_form.html"
    form_class = {
        Lupulo: LupuloForm,
        Malta: MaltaForm,
        Levadura: LevaduraForm,
        Agregado: AgregadoForm,
        Fermentador: FermentadorForm,
        Barril : BarrilForm,
        Botella : BotellaForm,

    }

    def get_form_class(self):
       return self.form_class[self.object.__class__]

    def get_queryset(self):
      return self.model.objects.select_subclasses()

    def get_context_data(self, **kwargs):
        context = super(Editar_insumo, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect("")

class Nuevo_insumo(CreateView):
    model= Insumo
    fields= '__all__'
    template_name="inventario/insumo_nuevo.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/ingredientes')

    def get_context_data(self, **kwargs):
       context = super(Nuevo_insumo, self).get_context_data(**kwargs)
       insumo = self.kwargs['insumo']
       context["insumo"] = insumo
       if insumo == "lupulo":
           context["form"] = modelform_factory(Lupulo, fields="__all__")
       elif insumo == "malta":
           context["form"] = modelform_factory(Malta, fields="__all__")
       elif insumo == "levadura":
           context["form"] = modelform_factory(Levadura, fields="__all__")
       elif insumo == "agregado":
           context["form"] = modelform_factory(Agregado, fields="__all__")
       elif insumo == "fermentador":
           context["form"] = modelform_factory(Fermentador, fields="__all__")
       elif insumo == "barril":
           context["form"] = modelform_factory(Barril, fields="__all__")
       elif insumo == "botella":
           context["form"] = modelform_factory(Botella, fields="__all__")
       else:
           context["form"] = modelform_factory(Insumo, fields="__all__")

       return context
