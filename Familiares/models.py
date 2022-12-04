from django.db import models

# Create your models here.
class FamiliaPrimaria(models.Model):
    nombre=models.CharField(max_length=30)
    parentezco=models.CharField(max_length=30)
    edad=models.IntegerField()
    cumpleaños=models.DateField()
    email=models.EmailField()

class OtrosFamiliares(models.Model):
    nombre=models.CharField(max_length=30)
    parentezco=models.CharField(max_length=30)
    hay_relacion=models.BooleanField()