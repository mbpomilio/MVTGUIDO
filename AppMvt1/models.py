from django.db import models
from datetime import datetime


class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=20)
    fe_nac = models.DateField()
    #fe_nac = fe_nac.strftime('YYYY-MM-DD')
