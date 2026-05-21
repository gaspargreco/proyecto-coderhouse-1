from django.db import models


class RegistroPeso(models.Model):
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=3, decimal_places=1)

class RegistroDiaGimnasio(models.Model):
    fecha = models.DateField()
    musculos1 = models.CharField(max_length= 30)
    musculos2 = models.CharField(max_length=30)
    musculos3 = models.CharField(max_length =30, blank=True, null=True)

class RegistroEjerciciosBasicos(models.Model):
    fecha = models.DateField()
    press_banca = models.DecimalField(max_digits=4, decimal_places=1)
    peso_muerto = models.DecimalField(max_digits=4, decimal_places=1)
    sentadilla = models.DecimalField(max_digits=4, decimal_places=1)
    

