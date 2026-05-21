from django.contrib import admin
from registros.models import RegistroEjerciciosBasicos, RegistroDiaGimnasio, RegistroPeso

admin.site.register(RegistroEjerciciosBasicos)
admin.site.register(RegistroDiaGimnasio)    
admin.site.register(RegistroPeso)

# Register your models here.
