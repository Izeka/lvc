from django.views.generic import ListView, UpdateView
from django.forms import modelformset_factory
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, ModelFormSetView
from extra_views.generic import GenericInlineFormSet
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

class Recetas(ListView):
    model = Receta
    template_name = "produccion/recetas.html"
    context_object_name = 'recetas'

class Nueva_receta(CreateWithInlinesView):
    model = Receta
    inlines = [MaltaInline, LupuloInline, AgregadosInline]
    fields = "__all__"
    success_url = "/recetas"

class Update_receta(UpdateWithInlinesView):
    model = Receta
    inlines = [MaltaInline, LupuloInline, AgregadosInline]
    fields = "__all__"
    success_url = "/recetas"


class View_receta(UpdateView):
    model = Receta
    template_name = "produccion/view_receta.html"
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


class Cocciones(ListView):
    model = Coccion
    template_name = "produccion/cocciones.html"
    context_object_name = 'cocciones'

class Nueva_coccion(CreateWithInlinesView):
    model = Coccion
    inlines = [MaltaCoccionInline, LupuloCoccionInline, AgregadosCoccionInline]
    fields = "__all__"
    success_url = "/cocciones"

    def get_context_data(self, **kwargs):
        context = super(Nueva_coccion, self).get_context_data(**kwargs)
        receta= self.request.POST.get('Receta',False)
        if receta:
           context['receta'] = Receta.objects.get(pk=receta)
           maltasFormset = modelformset_factory(Malta_x_Receta, fields="__all__")
           context['maltas']= maltasFormset(queryset=Malta_x_Receta.objects.filter(Receta=receta))
        context['hoy'] = date.today()
        return context


class Update_coccion(UpdateWithInlinesView):
    model = Coccion
    inlines = [MaltaCoccionInline, LupuloCoccionInline, AgregadosCoccionInline]
    fields = "__all__"
    success_url = "/cocciones"

class View_coccion(UpdateView):
    model = Coccion
    template_name = "produccion/view_coccion.html"
    fields = "__all__"
