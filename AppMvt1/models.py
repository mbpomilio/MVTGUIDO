from django.db import models
from datetime import datetime


class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=20)
    edad = models.IntegerField()
    #nac = models.DateField()
