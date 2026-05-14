from django.db import models


class RegistroPeso(models.Model):
    fecha = models.DateField(auto_now_add = True)
    valor = models.DecimalField(max_digits=5, decimal_places=1)
    