from django.shortcuts import render, redirect
from registros.models import RegistroBasicos, RegistroDiaEjercicios, RegistroPeso
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from registros.forms import RegistroPesoForm, RegistroDiaEjerciciosForm, RegistroBasicosForm


def lista_registro(request):
    
    
    registros_peso = RegistroPeso.objects.all()
    registros_dia_ejercicios = RegistroDiaEjercicios.objects.all()
    registros_basicos = RegistroBasicos.objects.all()
    
    return render(request,"registros/listado.html", {"registros": registros_peso, "registros_dia_ejercicios": registros_dia_ejercicios, "registros_basicos": registros_basicos})


def registrar_peso(request):
    
    if request.method == "POST":
        formulario = RegistroPesoForm(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            registro_peso = RegistroPeso(fecha= info.get("fecha"), valor = info.get("valor"))
            registro_peso.save()
            return redirect("registros:listado")
    else:
        formulario = RegistroPesoForm()
    return render(request, "registros/crear_registro_peso.html", {"formulario": formulario})

def registrar_dia_ejercicios(request):
    
    if request.method == "POST":
        formulario = RegistroDiaEjerciciosForm(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            registro_dia_ejercicios = RegistroDiaEjercicios(fecha= info.get("fecha"), musculos1 = info.get("musculos1"), musculos2 = info.get("musculos2"), musculos3 = info.get("musculos3"))
            registro_dia_ejercicios.save()
            return redirect("registros:listado")
    else:
        formulario = RegistroDiaEjerciciosForm()
    return render(request, "registros/crear_registro_dia_ejercicios.html", {"formulario": formulario})


def registrar_basicos(request):
    if request.method == "POST":
        formulario = RegistroBasicosForm(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            registro_basicos = RegistroBasicos(fecha= info.get("fecha"), press_banca = info.get("press_banca"), sentadilla = info.get("sentadilla"), peso_muerto = info.get("peso_muerto"))
            registro_basicos.save()
            return redirect("registros:listado")
    else:
        formulario = RegistroBasicosForm()
    return render(request, "registros/crear_registro_basicos.html", {"formulario": formulario})

class ActualizarRegistroBasicos(UpdateView):
    model = RegistroBasicos
    fields = ["fecha", "press_banca", "sentadilla", "peso_muerto"]
    template_name = "registros/actualizar_registro_ejercicios.html"
    success_url = reverse_lazy("registros:listado")
    
