from django.shortcuts import render
from django.views.generic import ListView, CreateView
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet
from .models import *
from .forms import *
# Create your views here.


class MaltaInline(InlineFormSet):
    model = Malta_x_Receta
    fields="__all__"
    extra=1

class LupuloInline(InlineFormSet):
    model = Lupulo_x_Receta
    fields = "__all__"
    extra=1

class Recetas(ListView):
    model = Receta
    template_name = "produccion/recetas.html"
    context_object_name = 'recetas'

class Nueva_receta(CreateWithInlinesView):
    model = Receta
    inlines = [MaltaInline, LupuloInline]
    fields = "__all__"
    success_url = "/recetas"

class Update_receta(UpdateWithInlinesView):
    model = Receta
    inlines = [MaltaInline, LupuloInline]
    fields = "__all__"
    success_url = "/recetas"


class Malta_Receta(ListView):
    model = Malta_x_Receta
    template_name = "inventario/insumos.html"
    context_object_name = 'malta'
