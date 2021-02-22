from io import TextIOWrapper
from django.db import models

# Create your models here.
class produtos(models.Model):

    modelo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    estoque = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.modelo