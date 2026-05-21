from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.forms import EditarPerfil, FormularioCambioContraseña, FormularioCreacion, Iniciosesion, FormularioCambioContraseña
from usuarios.models import InformacionExtra

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = Iniciosesion(request, data = request.POST)
        
        if formulario.is_valid():
            
            user = formulario.get_user()
            
            login(request, user)
            
            InformacionExtra.objects.get_or_create(user = user) 
            
            return redirect("inicio:inicio")
        
    
        
    else:
        formulario = Iniciosesion()
    
    return render(request, "usuarios/iniciar_sesion.html", {"formulario": formulario})

def registrar_usuario(request):
    
    if request.method == "POST":
        formulario = FormularioCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('usuarios:iniciar_sesion')
    else:
        formulario = FormularioCreacion()
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def perfil_usuario(request):
    return render(request, "usuarios/perfil.html")

def editar_perfil(request):
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('fecha_nacimiento'):
                request.user.infoextra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
                request.user.infoextra.save()
            
            formulario.save()
            return redirect('usuarios:perfil')
    else:
        formulario = EditarPerfil(instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class CambiarContraseña(PasswordChangeView):
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url = reverse_lazy('usuarios:perfil')
    form_class = FormularioCambioContraseña