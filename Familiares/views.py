from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def familiares(request):
    
    familiar1=FamiliaPrimaria(nombre="Ana",parentezco="Madre",edad=66,cumpleaños="1956-05-12",email="ana10002@hotmail.com")
    familiar2=FamiliaPrimaria(nombre="Juan",parentezco="Padre",edad=68,cumpleaños="1954-08-02",email="juancho30006@hotmail.com")
    familiar3=OtrosFamiliares(nombre="Augusto",parentezco="Primo",hay_relacion=False)
    
    familiar1.save()
    familiar2.save()
    familiar3.save()

    diccionario={"FamiliaPrimaria":[familiar1,familiar2],"OtrosFamiliares":[familiar3]}
    template=loader.get_template("template.html")
    documento=template.render(diccionario)
    return HttpResponse(documento)

     