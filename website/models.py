from io import TextIOWrapper
from django.db import models

# Create your models here.
class produtos(models.Model):

    modelo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    estoque = models.IntegerField()
    estoque_minimo = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.modelo

class Movimentacoes(models.Model):

    class Meta:
        ordering = ['-created_at']

    STATUS = (
        ('entrada','Entrada'),
        ('saida','Saida')
    )

    produto = models.ForeignKey(produtos,on_delete=models.CASCADE)
    clientes = models.ManyToManyField("Clientes")
    tipo_mov = models.CharField(max_length=7,choices=STATUS)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    numero_nf = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        descricao = str(self.id) + " - " + str(self.numero_nf) + " - " + str(self.data)
        return descricao

class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14,blank=True,null=True)
    telefone = models.IntegerField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome