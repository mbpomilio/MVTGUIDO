from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=20)
    fe_nac = models.DateField()
