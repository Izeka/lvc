# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.forms import modelform_factory
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, ModelFormSetView
from django_addanother.views import CreatePopupMixin
from inventario.models import *
from .models import *
from .forms import *
from inventario.forms import *

# Create your views here.

class Compras(LoginRequiredMixin, ListView):
    model = Compra
    login_url = "/login/"
    template_name = "contabilidad/compras.html"
    context_object_name = 'compras'

class InsumoInline( InlineFormSet):
    model = CompraInsumo
    fields="__all__"
    extra=1

class BarrilInline( InlineFormSet):
    model = Barril
    fields="__all__"
    extra=1

class Compra_insumos(LoginRequiredMixin, CreateWithInlinesView):
    model = Compra
    fields='__all__'
    login_url = "/login/"
    inlines = [InsumoInline]
    success_url = "/compras"
    template_name ="contabilidad/compra_insumos.html"

class Compra_equipamiento(LoginRequiredMixin, CreateWithInlinesView):
    model = Compra
    fields='__all__'
    login_url = "/login/"
    inlines = [BarrilInline]
    success_url = "/compras"
    template_name ="contabilidad/compra_equipamiento.html"

    def get_context_data(self, **kwargs):
        context = super(Compra_equipamiento, self).get_context_data(**kwargs)
        context['no_fields'] = ["Ubicacion","Id","Compra", "Lleno","Carbonatado", "Observaciones","Eliminar"]
        return context
