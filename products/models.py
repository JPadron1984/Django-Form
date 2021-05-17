from django.db import models

# Create your models here.


class Product(models.Model):
    codigo = models.CharField(max_length=15)
    descripcion = models.TextField(blank=True, null=True)
    proveedor = models.CharField(max_length=15)
    precio = models.DecimalField(decimal_places=2, max_digits=10000)
