from django.urls import path
from registros.views import lista_registro, registrar_basicos, registrar_dia_ejercicios, registrar_peso, ActualizarRegistroBasicos

app_name = "registros"

urlpatterns = [
    path("", lista_registro, name = "listado"),
    path("crear/", registrar_peso, name = "registrar_peso" ),
    path("actualizar/<int:pk>/", ActualizarRegistroBasicos.as_view(), name = "actualizar_registro"),
    path("crear_dia_ejercicios/", registrar_dia_ejercicios, name = "registrar_dia_ejercicios" ),
    path("crear_registro_basicos/", registrar_basicos, name = "registrar_basicos" ),
]
