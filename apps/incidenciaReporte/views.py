# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'principal/index.html',{})

def generarincidencia(request):
	return render(request,'principal/generarIncidencia.html',{})

def gestionarproductos(request):
	return render(request,'principal/gestionarProductos.html',{})

def gestplanes(request):
	return render(request,'principal/gestplanes.html',{})

def mostrarincidencia(request):
	return render(request,'principal/mostrarIncidencia.html',{})

def verinventario(request):
	return render(request,'principal/verInventario.html',{})