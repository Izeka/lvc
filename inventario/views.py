from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.forms import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django_addanother.views import CreatePopupMixin
from django.core.files.uploadedfile import InMemoryUploadedFile

import  json
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
        context['botellas'] = Botellas.objects.all()
        context['varios'] = Insumo.objects.filter(Tipo="EQ")

        return context

class Insumos(LoginRequiredMixin, ListView):
    model = Insumo
    login_url = "/login/"
    template_name = "inventario/insumos.html"
    context_object_name = 'insumos'

    def get_queryset(self):
        queryset=Insumo.objects.all().filter(Tipo=3)
        return queryset

class Editar_Barril(LoginRequiredMixin, UpdateView):
    model = Barril
    login_url = "/login/"
    fields= '__all__'
    template_name="inventario/insumo_form.html"

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect("/equipamiento")

    def get_context_data(self, **kwargs):
        context = super(Editar_Barril, self).get_context_data(**kwargs)
        context['no_fields'] = ["Compra"]
        return context

class Editar_Fermentador(LoginRequiredMixin, UpdateView):
    model = Fermentador
    login_url = "/login/"
    fields= '__all__'
    template_name="inventario/insumo_form.html"

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect("/equipamiento")

    def get_context_data(self, **kwargs):
        context = super(Editar_Fermentador, self).get_context_data(**kwargs)
        context['no_fields'] = ["Compra"]
        return context

class Editar_Botellas(LoginRequiredMixin, UpdateView):
    model = Botellas
    login_url = "/login/"
    fields= '__all__'
    template_name="inventario/insumo_form.html"

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect("/equipamiento")

class Editar_insumo(LoginRequiredMixin, UpdateView):
    model = Insumo
    login_url = "/login/"
    fields= '__all__'
    template_name="inventario/insumo_form.html"
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
        context = super(Editar_insumo, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect("")

class Nuevo_insumo(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    template_name="inventario/insumo_nuevo.html"
    form_class = InsumoForm

    def form_valid(self, form, insumo):
        message = "form valid"
        form.save()
        return HttpResponse(json.dumps({'message': message}))

    def form_invalid(self, form, insumo):
        message = "form invalid"
        return HttpResponseRedirect("/insumos/nuevo/"+insumo)

    def post(self, request, *args, **kwargs):
        insumo = request.POST["insumo"]
        if insumo == "lupulo":
            form_class = LupuloForm
        elif insumo == "malta":
            form_class = MaltaForm
        elif insumo == "levadura":
            form_class = LevaduraForm
        elif insumo == "agregado":
            form_class = AgregadoForm
        elif insumo == "fermentador":
            form_class = FermentadorForm
        elif insumo == "barril":
            form_class = BarrilForm
        elif insumo == "botellas":
            form_class = BotellasForm
        else:
            form_class = InsumoForm
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form,insumo)
        else:
            return self.form_invalid(form,insumo)

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
       elif insumo == "botellas":
           context["form"] = modelform_factory(Botellas, fields="__all__")
       else:
           context["form"] = modelform_factory(Insumo, fields="__all__")
       return context
