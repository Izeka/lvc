from django.views.generic import ListView, UpdateView, CreateView
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, ModelFormSetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from .models import *
from .forms import *
from datetime import date
# Create your views here.


class MaltaInline(InlineFormSet):
    model = Malta_x_Receta
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class LevaduraInline(InlineFormSet):
    model = Levadura_x_Receta
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class LupuloInline(InlineFormSet):
    model = Lupulo_x_Receta
    fields = "__all__"
    factory_kwargs = {'extra': 1, 'max_num': 10}


class AgregadoInline(InlineFormSet):
    model = Agregado_x_Receta
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class Recetas(LoginRequiredMixin, ListView):
    model = Receta
    template_name = "produccion/recetas.html"
    context_object_name = 'recetas'


class Nueva_receta(LoginRequiredMixin, CreateWithInlinesView):
    model = Receta
    login_url = "/login/"
    inlines = [MaltaInline, LupuloInline, LevaduraInline, AgregadoInline]
    fields = "__all__"
    success_url = "/recetas"


class Editar_receta(LoginRequiredMixin, UpdateWithInlinesView):
    model = Receta
    login_url = "/login/"
    inlines = [MaltaInline,  LupuloInline, LevaduraInline, AgregadoInline]
    fields = "__all__"
    success_url = "/recetas"


class Ver_receta(LoginRequiredMixin, UpdateView):
    model = Receta
    login_url = "/login/"
    template_name = "produccion/ver_receta.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(View_receta, self).get_context_data(**kwargs)
        context['lupulos'] = Lupulo_x_Receta.objects.filter(
            receta=self.kwargs['pk'])
        context['maltas'] = Malta_x_Receta.objects.filter(
            receta=self.kwargs['pk'])
        context['agregados'] = Agregado_x_Receta.objects.filter(
            receta=self.kwargs['pk'])
        return context


class MaltaCoccionInline(InlineFormSet):
    model = Malta_x_Coccion
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class LevaduraCoccionInline(InlineFormSet):
    model = Levadura_x_Coccion
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class LupuloCoccionInline(InlineFormSet):
    model = Lupulo_x_Coccion
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class AgregadoCoccionInline(InlineFormSet):
    model = Agregado_x_Coccion
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class Cocciones(LoginRequiredMixin, ListView):
    model = Coccion
    login_url = "/login/"
    template_name = "produccion/cocciones.html"
    context_object_name = 'cocciones'


"""
def get_receta(request, receta_id):
    receta = Receta.objects.get(ID=receta_id)
    maltas = maltaFormSet(queryset=Malta_x_Receta.objects.filter(
        receta=receta), prefix="malta_x_coccion_set")
    lupulos = lupuloFormSet(queryset=Lupulo_x_Receta.objects.filter(
        receta=receta), prefix="lupulo_x_coccion_set")
    levaduras = levaduraFormSet(queryset=Levadura_x_Receta.objects.filter(
        receta=receta), prefix="levadura_x_coccion_set")
    agregados = agregadoFormSet(queryset=Agregado_x_Receta.objects.filter(
        receta=receta), prefix="agregado_x_coccion_set")
    return render(request, 'produccion/ingredientes.html', {'receta':receta, 'maltas': maltas, 'levaduras': levaduras, 'lupulos': lupulos,'agregados': agregados})
"""


class Nueva_coccion(LoginRequiredMixin, CreateWithInlinesView):
    model = Coccion
    login_url = "/login/"
    inlines = [MaltaCoccionInline, LupuloCoccionInline,
               LevaduraCoccionInline, AgregadoCoccionInline]
    fields = "__all__"
    success_url = "/cocciones"

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect("/cocciones")

    def form_invalid(self, form):
        message = "form invalid"
        return HttpResponseRedirect("/cocciones/nueva/", form)

    def get_context_data(self, **kwargs):
        context = super(Nueva_coccion, self).get_context_data(**kwargs)
        # obtengo el valor de la receta seleccionada
        receta = self.request.POST.get("receta", None)
        # obtengo el valor de la fecha actual
        context['hoy'] = date.today()
        # obtengo las ultimas cinco cocciones
        context['ultimas'] = Coccion.objects.all().order_by('fecha')[:5]
        try:
            # otengo el valor de la ultima coccion
            lote = Coccion.objects.latest('fecha')
            # asigno a lote los digitos del valor de la coccion
            context['lote'] = ''.join(n for n in lote if n.isdigit())
        except:
            # si no existe ninguna coccion, genero el valor 001
            context['lote'] = "0001"
        if receta:
            """si ya tengo el valor de la receta, obtengo los valores de cada ingrediente
            y genero los formsets para cada uno"""
            context['receta'] = Receta.objects.get(ID=receta)
            context['maltas'] = maltaFormSet(queryset=Malta_x_Receta.objects.filter(
                receta=receta), prefix="malta_x_coccion_set")
            context['lupulos'] = lupuloFormSet(queryset=Lupulo_x_Receta.objects.filter(
                receta=receta), prefix="lupulo_x_coccion_set")
            context['levaduras'] = levaduraFormSet(queryset=Levadura_x_Receta.objects.filter(
                receta=receta), prefix="levadura_x_coccion_set")
            context['agregados'] = agregadoFormSet(queryset=Agregado_x_Receta.objects.filter(
                receta=receta), prefix="agregado_x_coccion_set")
        return context


class Editar_coccion(LoginRequiredMixin, UpdateWithInlinesView):
    model = Coccion
    login_url = "/login/"
    inlines = [MaltaCoccionInline, LupuloCoccionInline,
               LevaduraCoccionInline, AgregadoCoccionInline]
    fields = ["lote", "fecha", "DF", "litros", "observaciones"]
    success_url = "/cocciones"


class Ver_coccion(LoginRequiredMixin, UpdateView):
    model = Coccion
    login_url = "/login/"
    template_name = "produccion/view_coccion.html"
    fields = "__all__"


class Fermentaciones(LoginRequiredMixin, ListView):
    model = Fermentacion
    login_url = "/login/"
    template_name = "produccion/fermentaciones.html"
    context_object_name = 'fermentaciones'


class Nueva_fermentacion(LoginRequiredMixin, CreateView):
    model = Fermentacion
    login_url = "/login/"
    template_name = "produccion/fermentacion_form.html"
    fields = "__all__"
    success_url = "/fermentaciones"

    def get_context_data(self, **kwargs):
        context = super(Nueva_fermentacion, self).get_context_data(**kwargs)
        #obtengo solo las cocciones que no estan fermentadas
        context['form'].fields['coccion'].queryset = Coccion.objects.filter(
            fermentado=False)
        #obtengo solo los fermentadores vacios
        context['form'].fields['fermentador'].queryset = Fermentador.objects.filter(
            lleno=False)
        return context


class Maduraciones(LoginRequiredMixin, ListView):
    model = Maduracion
    login_url = "/login/"
    template_name = "produccion/maduraciones.html"
    context_object_name = 'maduraciones'


class FermentacionInline(InlineFormSet):
    model = fermentacion_x_madurador
    #especifico el form personalizado en form.py
    form_class = FermentacionInlineForm
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class Nueva_maduracion(LoginRequiredMixin, CreateWithInlinesView):
    model = Maduracion
    login_url = "/login/"
    inlines = [FermentacionInline, ]
    fields = "__all__"
    success_url = "/maduraciones"

    def get_context_data(self, **kwargs):
        context = super(Nueva_maduracion, self).get_context_data(**kwargs)
        try:
            #obtengo el valor de la ultima Fermentacion
            ultima_fermentacion = Fermentacion.objects.filter(madurado=False).latest('fecha_inicio')
            #asigno a lote los primeros siete valores de la ultima Fermentacion
            context['lote'] = ultima_fermentacion.lote[:7]
        except:
            #si no hay fermentaciones paso
            pass
        #fields que no quiero mostrar en el template
        context['no_fields'] = ["Id", "Eliminar", "Maduracion"]
        return context


class Embarrilados(LoginRequiredMixin, ListView):
    model = Embarrilado
    login_url = "/login/"
    template_name = "produccion/embarrilados.html"
    context_object_name = 'embarrilados'


class Nuevo_embarrilado(LoginRequiredMixin, CreateView):
    form_class = EmbarriladoForm
    template_name = 'produccion/embarrilado_form.html'
    login_url = "/login/"
    success_url = "/embarrilados"

    def form_valid(self, form):
        self.object = form.save()
        for b in form.cleaned_data['barril']:
            barril= Barril.objects.get(numero_serie=b.numero_serie)
            barril.lleno=True
            barril.save()
        return HttpResponseRedirect("/embarrilados")
