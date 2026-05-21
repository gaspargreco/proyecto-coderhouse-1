from django.urls import path
from inicio.views import inicio, gaspar

app_name = "inicio"

urlpatterns = [
    path("", inicio, name ="inicio"),
    path("sobre_mi", gaspar, name ="gaspar"),
]
