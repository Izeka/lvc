from django.views.generic import ListView, UpdateView
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, ModelFormSetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import JsonResponse

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

def get_receta(request):
    receta = request.GET.get('receta', None)
    data = Receta.objects.get(pk=receta)
    return JsonResponse(model_to_dict(data), safe=False)

class Nueva_coccion(LoginRequiredMixin, CreateWithInlinesView):
    model = Coccion
    login_url = "/login/"
    inlines = [MaltaCoccionInline, LupuloCoccionInline, AgregadosCoccionInline]
    fields = "__all__"
    success_url = "/cocciones"

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect("/cocciones")

    def get_context_data(self, **kwargs):
        context = super(Nueva_coccion, self).get_context_data(**kwargs)
        receta_id = self.request.POST.get('Receta',False)
        context['hoy'] = date.today()
        if receta_id:
           receta = Receta.objects.get(id=receta_id)
           context['maltas'] = maltaFormSet(queryset=Malta_x_Receta.objects.filter(Receta=receta),prefix="malta_x_coccion_set")
           context['lupulos']  = lupuloFormSet(queryset=Lupulo_x_Receta.objects.filter(Receta=receta),prefix="lupulo_x_coccion_set")
           context['agregados'] = agregadoFormSet(queryset=Agregados_x_Receta.objects.filter(Receta=receta),prefix="agregado_x_coccion_set")
           context['receta'] = receta
    #       context['inlines'] = list([maltas, lupulos, agregados])
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
