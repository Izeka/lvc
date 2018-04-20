from django.views.generic import ListView, UpdateView
from django.forms import modelformset_factory
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, ModelFormSetView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from datetime import date
# Create your views here.

class MaltaInline(InlineFormSet):
    model = Malta_x_Receta
    fields="__all__"
    extra=1

class LupuloInline(InlineFormSet):
    model = Lupulo_x_Receta
    fields = "__all__"
    extra=1

class AgregadosInline(InlineFormSet):
    model = Agregados_x_Receta
    fields = "__all__"
    extra=1

class Recetas(LoginRequiredMixin, ListView):
    model = Receta
    template_name = "produccion/recetas.html"
    context_object_name = 'recetas'

class Nueva_receta(LoginRequiredMixin, CreateWithInlinesView):
    model = Receta
    login_url = "/login/"
    inlines = [MaltaInline, LupuloInline, AgregadosInline]
    fields = "__all__"
    success_url = "/recetas"

class Editar_receta(LoginRequiredMixin, UpdateWithInlinesView):
    model = Receta
    login_url = "/login/"
    inlines = [MaltaInline, LupuloInline, AgregadosInline]
    fields = "__all__"
    success_url = "/recetas"

class Ver_receta(LoginRequiredMixin, UpdateView):
    model = Receta
    login_url = "/login/"
    template_name = "produccion/ver_receta.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(View_receta, self).get_context_data(**kwargs)
        context['lupulos'] = Lupulo_x_Receta.objects.filter(Receta=self.kwargs['pk'])
        context['maltas'] = Malta_x_Receta.objects.filter(Receta=self.kwargs['pk'])
        context['agregados'] = Agregados_x_Receta.objects.filter(Receta=self.kwargs['pk'])
        return context

class MaltaCoccionInline(InlineFormSet):
    model = Malta_x_Coccion
    fields="__all__"
    extra=1

class LupuloCoccionInline(InlineFormSet):
    model = Lupulo_x_Coccion
    fields = "__all__"
    extra=1

class AgregadosCoccionInline(InlineFormSet):
    model = Agregados_x_Coccion
    fields = "__all__"
    extra=1

class Cocciones(LoginRequiredMixin, ListView):
    model = Coccion
    login_url = "/login/"
    template_name = "produccion/cocciones.html"
    context_object_name = 'cocciones'

class Nueva_coccion(LoginRequiredMixin, CreateWithInlinesView):
    model = Coccion
    login_url = "/login/"
    inlines = [MaltaCoccionInline, LupuloCoccionInline, AgregadosCoccionInline]
    fields = "__all__"
    success_url = "/cocciones"

    def get_context_data(self, **kwargs):
        context = super(Nueva_coccion, self).get_context_data(**kwargs)
        receta= self.request.POST.get('Receta',False)
        context['hoy'] = date.today()
        if receta:
           context['receta'] = Receta.objects.get(pk=receta)
           context['maltas']= MaltaCoccionInline(queryset=Malta_x_Receta.objects.filter(Receta=receta))
           context['lupulos']= maltasFormset(queryset=Lupulo_x_Receta.objects.filter(Receta=receta))
           context['agregados']= maltasFormset(queryset=Agregados_x_Receta.objects.filter(Receta=receta))
        return context

class Editar_coccion(LoginRequiredMixin, UpdateWithInlinesView):
    model = Coccion
    login_url = "/login/"
    inlines = [MaltaCoccionInline, LupuloCoccionInline, AgregadosCoccionInline]
    fields = "__all__"
    success_url = "/cocciones"

class Ver_coccion(LoginRequiredMixin, UpdateView):
    model = Coccion
    login_url = "/login/"
    template_name = "produccion/view_coccion.html"
    fields = "__all__"
