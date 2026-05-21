from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class Iniciosesion(AuthenticationForm):
    username = forms.CharField(label = "Nombre de Usuario")
    password = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)

class FormularioCreacion(UserCreationForm):
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nombre de Usuario",
            "email": "Correo Electrónico"  
        }
        help_texts = {
            "username": ""
        }


class EditarPerfil(UserChangeForm):
    password = None
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'fecha_nacimiento']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }


class FormularioCambioContraseña(PasswordChangeForm ):
    old_password = forms.CharField(label='Contraseña Vieja', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contraseña Nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contraseña Nueva', widget=forms.PasswordInput)