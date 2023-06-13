from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from datetime import datetime as dt
from .models import Products
from .forms import *

def inicio(request):
    return render(request, "delivery_app/index.html")

def formulario(request):

    if request.method == 'POST':
        producto = Products(title = request.POST['title'], price  = request.POST['price'])
        producto.save()
        return render(request,  "delivery_app/index.html")
    
    return render(request, "delivery_app/formulario.html")

def product_form(request):

    if request.method == 'POST':
             
        form = ProductForm(request.POST)

        if form.is_valid():
            infoForm = form.cleaned_data
            producto = Products(title = infoForm["title"], price = infoForm["price"])
            producto.save()
            return render(request, "delivery_app/index.html")
    
    else:
        form = ProductForm()

    return render(request, "delivery_app/form_api.html", {"form": form})

def product_search(request):
    if request.method =="POST":
         buscar_productos = ProductSearch(request.POST)

         if buscar_productos.is_valid():
             info = buscar_productos.cleaned_data
             productos = Products.objects.filter(title__icontains = info["title"])
             return render(request, "delivery_app/lista_productos.html", {"productos": productos})
    else:
        buscar_productos = ProductSearch()
        return render(request, "delivery_app/buscar_productos.html", {"form": buscar_productos})