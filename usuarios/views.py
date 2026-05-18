from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        
        if formulario.is_valid():
            
            user = formulario.get_user()
            
            login(request, user)
            
        
    else:
        formulario = ...()    
