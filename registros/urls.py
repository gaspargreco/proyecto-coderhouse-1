from django.urls import path
from registros.views import listado

app_name = "registros"

urlpatterns = [
    path("", listado, name= "listado" )
]
