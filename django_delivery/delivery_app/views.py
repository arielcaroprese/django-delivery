from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from datetime import datetime as dt

def inicio(request):
    return render(request, "delivery_app/index.html")

def nosotros(request):
    return render(request, "delivery_app/nosotros.html")

def servicios(request):
    return render(request, "delivery_app/servicios.html")

def productos(request):
    return render(request, "delivery_app/productos.html")

def contacto(request):
    return render(request, "delivery_app/contacto.html")
