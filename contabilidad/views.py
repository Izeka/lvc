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

class CompraInline( InlineFormSet):
    model = CompraItem
    fields="__all__"
    extra=1

class Nueva_compra(LoginRequiredMixin, CreateWithInlinesView):
    model = Compra
    fields='__all__'
    login_url = "/login/"
    inlines = [CompraInline,]
    template_name ="contabilidad/compras_nueva.html"

class Compra_insumoss(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    template_name="contabilidad/ingrediente_nuevo.html"
    form_class = InsumoForm
