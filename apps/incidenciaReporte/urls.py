from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.incidenciaReporte.views import *
urlpatterns=[
url(r'^$', index),
url(r'^ginci/', generarincidencia, name="ginci"),
url(r'^gpro', gestionarproductos, name="gpro"),
url(r'^gpla', gestplanes, name="gpla"),
url(r'^mosin', mostrarincidencia, name="mosin"),
url(r'^verinv', verinventario, name="verinv"),
]