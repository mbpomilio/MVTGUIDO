from django import http
from django.shortcuts import render
from AppMvt1.models import Familia
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader 


def familia(request):

    pariente1 = Familia(nombre="Belen", parentezco="Hermana", edad="31")
    pariente1.save()
    texto1 = f"Pariente agregado: {pariente1.nombre}"

    
    pariente2 = Familia(nombre="Carlos", parentezco="Papa", edad="65")
    pariente2.save()
    texto2 = f"Pariente agregado: {pariente2.nombre} "

    
    pariente3 = Familia(nombre="Pepe", parentezco="Tio", edad="55")
    pariente3.save()
    texto3 = f"Pariente agregado: {pariente3.nombre}"

    return HttpResponse(texto1 + "-" + texto2 + "-" + texto3)
    
def inicio(request):

    return render(request, "AppMvt1/inicio.html")

def familiar(request):
    return render(request, "AppMvt1/familia.html")
