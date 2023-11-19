# models.py

from django.db import models

class ItemListaCompra(models.Model):
    item = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=1)
