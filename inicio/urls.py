from django.urls import path
from inicio.views import inicio, gaspetita

app_name = "inicio"

urlpatterns = [
    path("", inicio, name ="inicio"),
    path("gaspetita/", gaspetita, name ="gaspetita"),
]
