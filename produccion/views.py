from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Receta
from .forms import RecetaForm
# Create your views here.

class Recetas(ListView):
    model = Receta
    template_name = "produccion/recetas.html"
    context_object_name = 'recetas'

class Nueva_receta(CreateView):
    model = Receta
    form_class = RecetaForm
    success_url='/recetas'


