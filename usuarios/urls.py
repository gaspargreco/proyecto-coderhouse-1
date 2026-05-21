from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import iniciar_sesion, registrar_usuario, perfil_usuario, editar_perfil, CambiarContraseña

app_name = "usuarios"

urlpatterns = [
    path("iniciar_sesion/", iniciar_sesion, name = "iniciar_sesion"),
    path("registrar_usuario/", registrar_usuario, name = "registrar_usuario"),
    path("perfil/", perfil_usuario, name = "perfil"),
    path("editar_perfil/", editar_perfil, name = "editar_perfil"),
    path("cambiar_contraseña/", CambiarContraseña.as_view(), name = "cambiar_contraseña"),
    path("cerrar_sesion/", LogoutView.as_view(template_name = "usuarios/cerrar_sesion.html"), name = "cerrar_sesion"),
    
]
