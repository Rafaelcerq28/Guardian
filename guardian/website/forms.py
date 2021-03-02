from django import forms
from django.forms import widgets
from .models import produtos, Movimentacoes

class produtoForm(forms.ModelForm):

    class Meta:
        model = produtos
        fields = ('modelo','tipo','fabricante','estoque')

        #Inserindo CSS no formulario
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control col-md-3'}),
        }

class movimentacoesForm(forms.ModelForm):

    CHOICES = (
    ('entrada','Entrada'),
    ('saida','Saida')
    )

    class Meta:
        model= Movimentacoes
        fields = ('tipo_mov','quantidade','numero_nf')

