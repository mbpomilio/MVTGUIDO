from django import http
from django.shortcuts import render
from AppMvt1.models import Familia
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader 


def familia(request):

    pariente1 = Familia(nombre="Belen", parentezco="Hermana", fe_nac='1991-10-11')
    pariente1.save()
    texto1 = f"Pariente agregado: {pariente1.nombre}"

    
    pariente2 = Familia(nombre="Carlos", parentezco="Hermano", fe_nac='1989-12-15')
    pariente2.save()
    texto2 = f"Pariente agregado: {pariente2.nombre} "

    
    pariente3 = Familia(nombre="Pepe", parentezco="Tio", fe_nac='1966-11-25')
    pariente3.save()
    texto3 = f"Pariente agregado: {pariente3.nombre}"

    return HttpResponse(texto1 + " - " + texto2 + " - " + texto3)
    
def inicio(request):

    return render(request, "AppMvt1/inicio.html")

def familiar(request):
    return render(request, "AppMvt1/familia.html")
