from django import forms
from registros.models import RegistroPeso, RegistroDiaGimnasio, RegistroEjerciciosBasicos


class RegistroPesoForm(forms.Form):
    
    valor = forms.DecimalField(max_digits=3,decimal_places=1)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
class RegistroDiaEjerciciosForm(forms.Form):
    
    musculos1 = forms.CharField(max_length=30)
    musculos2 = forms.CharField(max_length=30)
    musculos3 = forms.CharField(max_length=30)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
class RegistroBasicosForm(forms.Form):
    
    press_banca = forms.DecimalField(max_digits=4, decimal_places=1)
    sentadilla = forms.DecimalField(max_digits=4, decimal_places=1)
    peso_muerto = forms.DecimalField(max_digits=4, decimal_places=1)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))