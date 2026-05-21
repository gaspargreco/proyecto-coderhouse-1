from django.db import models
from django.contrib.auth.models import User

class InformacionExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    altura = models.DecimalField(decimal_places=2, max_digits=5)
    fecha_nacimiento = models.DateField()
# Create your models here.
