from typing import Sequence
from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from .models import produtos, Movimentacoes,Clientes

class produtoForm(forms.ModelForm):

    class Meta:
        model = produtos
        fields = ('modelo','tipo','fabricante','estoque_minimo')

        #Altera a label no formulario
        labels ={
            'estoque_minimo': _('Estoque Mínimo')
        }

        #Inserindo CSS no formulario
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'estoque_minimo': forms.NumberInput(attrs={'class': 'form-control col-md-3'}),
        }

class editForm(forms.ModelForm):

    class Meta:
        model = produtos
        fields = ('modelo','tipo','fabricante','estoque','estoque_minimo')

        #Altera a label no formulario
        labels ={
            'estoque_minimo': _('Estoque Mínimo'),
        }
        #Inserindo CSS no formulario
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control col-md-3'}),
            'estoque_minimo': forms.NumberInput(attrs={'class': 'form-control col-md-3'}),
        }

class movimentacoesForm(forms.ModelForm):

    CHOICES = (
    ('entrada','Entrada'),
    ('saida','Saida')
    )

    class Meta:
        model= Movimentacoes
        fields = ('tipo_mov','quantidade','numero_nf')
        
        labels ={
            'numero_nf': _('Numero NF ou outras informações'),
        }
        
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control col-md-3'}),
        }

class movimentacoesCadForm(forms.ModelForm):

    class Meta:
        model= Movimentacoes
        fields = ('quantidade','numero_nf')

        labels ={
            'numero_nf': _('Numero NF ou outras informações'),
        }
        
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control col-md-3'}),
        }

class clientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('nome','cnpj','telefone')

        labels = {
            'nome': _('Razão Social'),
            'cnpj': _('CNPJ')
        }

        widgets = {
            'cnpj': forms.NumberInput(attrs={'class': 'form-control col-md-5'}),
            'telefone': forms.NumberInput(attrs={'class': 'form-control col-md-4'}),
        }

class editCliForm(forms.ModelForm):
 
    class Meta:
        model = Clientes
        fields = {'nome','cnpj','telefone'}

        labels = {
            'nome': _('Razão Social'),
            'cnpj': _('CNPJ')
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-8 mb-4'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control col-md-8 mb-4'}),
            'telefone': forms.NumberInput(attrs={'class': 'form-control col-md-6'}),
        }