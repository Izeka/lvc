from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.forms import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django_addanother.views import CreatePopupMixin
from django.core.files.uploadedfile import InMemoryUploadedFile

import json
from .models import *
from .forms import *

# Create your views here.


class Ingredientes(LoginRequiredMixin, ListView):
    model = Insumo
    login_url = "/login/"
    template_name = "inventario/ingredientes.html"

    def get_context_data(self, **kwargs):
        context = super(Ingredientes, self).get_context_data(**kwargs)
        context['lupulos'] = Lupulo.objects.all()
        context['maltas'] = Malta.objects.all()
        context['levaduras'] = Levadura.objects.all()
        context['agregados'] = Agregado.objects.all()
        return context


class Equipamiento(LoginRequiredMixin, ListView):
    model = Barril
    login_url = "/login/"
    template_name = "inventario/equipamiento.html"

    def get_context_data(self, **kwargs):
        context = super(Equipamiento, self).get_context_data(**kwargs)
        context['barriles'] = Barril.objects.all()
        context['fermentadores'] = Fermentador.objects.all()
        context['pallet'] = Pallet.objects.all()
        context['varios'] = Insumo.objects.filter(tipo="EQUIPAMIENTO")

        return context


class Insumos(LoginRequiredMixin, ListView):
    model = Insumo
    login_url = "/login/"
    template_name = "inventario/insumos.html"
    context_object_name = 'insumos'

    def get_context_data(self, **kwargs):
        context = super(Insumos, self).get_context_data(**kwargs)
        context['acidos'] = Acido.objects.all()
        context['clarificantes'] = Clarificante.objects.all()
        context['accesorios'] = Accesorio.objects.all()
        context['varios'] = Insumo.objects.filter(tipo="INSUMO")

        return context


class Editar_Barril(LoginRequiredMixin, UpdateView):
    model = Barril
    login_url = "/login/"
    fields = '__all__'
    template_name = "inventario/insumo_form.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/equipamiento")

    def get_context_data(self, **kwargs):
        context = super(Editar_Barril, self).get_context_data(**kwargs)
        context['no_fields'] = ["compra"]
        return context


class Editar_Fermentador(LoginRequiredMixin, UpdateView):
    model = Fermentador
    login_url = "/login/"
    fields = '__all__'
    template_name = "inventario/insumo_form.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/equipamiento")

    def get_context_data(self, **kwargs):
        context = super(Editar_Fermentador, self).get_context_data(**kwargs)
        context['no_fields'] = ["compra"]
        return context


class Editar_Pallet(LoginRequiredMixin, UpdateView):
    model = Pallet
    login_url = "/login/"
    fields = '__all__'
    template_name = "inventario/insumo_form.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/equipamiento")


class Editar_insumo(LoginRequiredMixin, UpdateView):
    model = Insumo
    login_url = "/login/"
    fields = '__all__'
    template_name = "inventario/insumo_form.html"
    form_class = {
        Lupulo: LupuloForm,
        Malta: MaltaForm,
        Levadura: LevaduraForm,
        Agregado: AgregadoForm,
        Insumo: InsumoForm
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
        return HttpResponseRedirect("/ingredientes/")

    def form_invalid(self, form, insumo):
        message = "form invalid"
        return HttpResponseRedirect("/insumos/nuevo/" + insumo)


class Nuevo_insumo(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    template_name = "inventario/insumo_nuevo.html"
    form_class = InsumoForm

    def form_valid(self, form, insumo, url):
        message = "form valid"
        form.save()
        return HttpResponseRedirect("/"+url)

    def form_invalid(self, form, insumo):
        message = "form invalid"
        return HttpResponseRedirect("/insumos/nuevo/" + insumo)

    def post(self, request, *args, **kwargs):
        insumo = request.POST["insumo"]
        if insumo == "lupulo":
            form_class = LupuloForm
            url="ingrediente"
        elif insumo == "malta":
            form_class = MaltaForm
            url="ingrediente"
        elif insumo == "levadura":
            form_class = LevaduraForm
            url="ingrediente"
        elif insumo == "agregado":
            form_class = AgregadoForm
            url="ingrediente"
        elif insumo == "fermentador":
            form_class = FermentadorForm
            url="equipamiento"
        elif insumo == "barril":
            form_class = BarrilForm
            url="equipamiento"
        elif insumo == "pallet":
            form_class = PalletForm
            url="equipamiento"
        else:
            form_class = InsumoForm
            url="insumo"
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, insumo, url)
        else:
            return self.form_invalid(form, insumo)

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
        elif insumo == "pallet":
            context["form"] = modelform_factory(Pallet, fields="__all__")
        else:
            context["form"] = modelform_factory(Insumo, fields="__all__")
        return context
