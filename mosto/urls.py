"""mosto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:fsdf
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth.views import login, logout

from agenda.views import *
from inventario.views import *
from contabilidad.views import *
#from produccion.views import get_receta
from produccion.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, {'template_name':'login.html'},),
    url(r'^logout/', logout,{'template_name':'logout.html'},),
    url(r'^$', RedirectView.as_view(permanent=False, url='/ingredientes/')),

    url(r'^ingredientes/$', Ingredientes.as_view()),
    url(r'^ingredientes/nuevo/(?P<insumo>\w+)/$', Nuevo_insumo.as_view(),name='add_ingrediente'),
    url(r'^ingredientes/editar/(?P<pk>\d+)/$', Editar_insumo.as_view(),),

    url(r'^equipamiento/$', Equipamiento.as_view()),
    url(r'^equipamiento/nuevo/(?P<insumo>\w+)/$', Nuevo_insumo.as_view(),name='add_equipamiento'),
    url(r'^equipamiento/editar/(?P<pk>\d+)/$', Editar_insumo.as_view(),),
    url(r'^equipamiento/editar/barril/(?P<pk>\w+)/$', Editar_Barril.as_view(),),
    url(r'^equipamiento/editar/pallet/(?P<pk>\d+)/$', Editar_Pallet.as_view(),),
    url(r'^equipamiento/editar/fermentador/(?P<pk>\w+)/$', Editar_Fermentador.as_view(),),

    url(r'^insumos/$', Insumos.as_view()),
    url(r'^insumos/nuevo/(?P<insumo>\w+)/$', Nuevo_insumo.as_view(), ),
    url(r'^insumos/editar/(?P<pk>\d+)/$', Editar_insumo.as_view(),),

    url(r'^proveedores/$', Proveedores.as_view()),
    url(r'^proveedores/nuevo/$', Nuevo_proveedor.as_view()),
    url(r'^clientes/$', Clientes.as_view()),
#    url(r'^clientes/nuevo/$', Nuevo_cliente.as_view()),

    url(r'^compras/$', Compras.as_view()),
    url(r'^compras/insumo/$', Compra_insumos.as_view(),name='add_compra'),
    url(r'^compras/servicio/$', Compra_servicio.as_view(),name='add_servicio'),
    url(r'^compras/equipamiento/(?P<equipamiento>\w+)$', Compra_equipamiento.as_view(),name='add_equipamiento'),
    url(r'^compras/editar/(?P<pk>\d+)$', Compra_editar.as_view(),name='editar_compra'),

    url(r'^recetas/$', Recetas.as_view()),
    url(r'^recetas/editar/(?P<pk>\d+)/$', Editar_receta.as_view()),
    url(r'^recetas/ver/(?P<pk>\d+)/$', Ver_receta.as_view()),
    url(r'^recetas/nueva$', Nueva_receta.as_view(),name='add_receta'),

    url(r'^cocciones/$', Cocciones.as_view()),
    url(r'^cocciones/editar/(?P<pk>\d+)/$', Editar_coccion.as_view()),
    url(r'^cocciones/ver/(?P<pk>\d+)/$', Ver_coccion.as_view()),
    url(r'^cocciones/nueva$', Nueva_coccion.as_view(),name='add_coccion'),
#    url(r'^ajax/get_receta/$', get_receta, name='get_receta'),

    url(r'^fermentaciones/$', Fermentaciones.as_view()),

]
