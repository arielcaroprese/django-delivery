from django.http import HttpResponse
from datetime import datetime as dt

def saludo(request):
    dia = dt.now()
    return HttpResponse(dia)

def nombre(request, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)
