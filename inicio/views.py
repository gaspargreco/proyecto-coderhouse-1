from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "inicio/inicio.html")

def gaspetita(request):
    return render(request, "inicio/gaspetita.html")
