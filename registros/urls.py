from django.urls import path
from registros.views import lista_registros, lista_basicos, lista_dias, lista_peso, registrar_basicos, registrar_dia_ejercicios, registrar_peso, ActualizarRegistroBasicos, EliminarRegistroBasicos, EliminarRegistroDia, EliminarRegistroPeso

app_name = "registros"

urlpatterns = [
    path("", lista_registros, name = "listado"),
    path("crear/", registrar_peso, name = "registrar_peso" ),
    path("actualizar/<int:pk>/", ActualizarRegistroBasicos.as_view(), name = "actualizar_registro"),
    path("crear_dia_ejercicios/", registrar_dia_ejercicios, name = "registrar_dia_ejercicios" ),
    path("crear_registro_basicos/", registrar_basicos, name = "registrar_basicos" ),
    path("listado_peso/", lista_peso, name = "listado_peso"),
    path("listado_dia/", lista_dias, name = "listado_dia"),
    path("listado_basicos/", lista_basicos, name = "listado_basicos"),
    path("eliminar_registro_basicos/<int:pk>/", EliminarRegistroBasicos.as_view(), name = "eliminar_registro_basicos"),
    path("eliminar_registro_dia_ejercicios/<int:pk>/", EliminarRegistroDia.as_view(), name = "eliminar_registro_dia_ejercicios"),
    path("eliminar_registro_peso/<int:pk>/", EliminarRegistroPeso.as_view(), name = "eliminar_registro_peso"),
]
