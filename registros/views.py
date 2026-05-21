from django.shortcuts import render, redirect
from registros.models import RegistroEjerciciosBasicos, RegistroDiaGimnasio, RegistroPeso
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from registros.forms import RegistroPesoForm, RegistroDiaEjerciciosForm, RegistroBasicosForm

def lista_registros(request):
    return render(request, "registros/listado.html")

def lista_peso(request):

    lista_pesos = RegistroPeso.objects.all()
    return render(request,"registros/listado_peso.html", {"pesos": lista_pesos})

def lista_basicos(request):
    
    lista_basicos = RegistroEjerciciosBasicos.objects.all()
    return render(request, "registros/listado_basicos.html", {"basicos": lista_basicos})

def lista_dias(request):
    
    lista_dia = RegistroDiaGimnasio.objects.all()
    return render(request, "registros/listado_dia.html", {"dias": lista_dia})



@login_required
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

@login_required
def registrar_dia_ejercicios(request):
    
    if request.method == "POST":
        formulario = RegistroDiaEjerciciosForm(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            registro_dia_ejercicios = RegistroDiaGimnasio(fecha= info.get("fecha"), musculos1 = info.get("musculos1"), musculos2 = info.get("musculos2"), musculos3 = info.get("musculos3"))
            registro_dia_ejercicios.save()
            return redirect("registros:listado")
    else:
        formulario = RegistroDiaEjerciciosForm()
    return render(request, "registros/crear_registro_dia_ejercicios.html", {"formulario": formulario})

@login_required
def registrar_basicos(request):
    if request.method == "POST":
        formulario = RegistroBasicosForm(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            registro_basicos = RegistroEjerciciosBasicos(fecha= info.get("fecha"), press_banca = info.get("press_banca"), sentadilla = info.get("sentadilla"), peso_muerto = info.get("peso_muerto"))
            registro_basicos.save()
            return redirect("registros:listado")
    else:
        formulario = RegistroBasicosForm()
    return render(request, "registros/crear_registro_basicos.html", {"formulario": formulario})

class ActualizarRegistroBasicos(LoginRequiredMixin, UpdateView):
    model = RegistroEjerciciosBasicos
    fields = ["fecha", "press_banca", "sentadilla", "peso_muerto"]
    template_name = "registros/actualizar_registro_ejercicios.html"
    success_url = reverse_lazy("registros:listado_basicos")

class EliminarRegistroBasicos(LoginRequiredMixin, DeleteView):
    model = RegistroEjerciciosBasicos
    template_name = "registros/eliminar_registro_basico.html"
    success_url = reverse_lazy("registros:listado_basicos")

class EliminarRegistroPeso(LoginRequiredMixin, DeleteView):
    model = RegistroPeso
    template_name = "registros/eliminar_registro_peso.html"
    success_url = reverse_lazy("registros:listado_peso")

class EliminarRegistroDia(LoginRequiredMixin, DeleteView):
    model = RegistroDiaGimnasio
    template_name = "registros/eliminar_registro_dia.html"
    success_url = reverse_lazy("registros:listado_dia")