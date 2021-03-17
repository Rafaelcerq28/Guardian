from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

#url a ser digitada na barra de navegação e caminho para o método correspondente a ela na view

urlpatterns = [
    #path('',views.login),
    path('',views.index),
    path('cadprodutos',views.cadprodutos),
    path('listaprodutos',views.listaprodutos),
    path('exibeproduto/<int:id>',views.exibeproduto),
    path('editaproduto/<int:id>',views.editaproduto),
    path('deletaproduto/<int:id>',views.deletaproduto),
    path('movimentacao/<int:id>/<int:idcli>',views.movimentacao),
    path('movimentacaoCad/<int:id>',views.movimentacaoCad),
    path('cadclientes',views.cadclientes),
    path('listaclientes',views.listaclientes),
    path('exibecliente/<int:id>',views.exibecliente),
    path('editacliente/<int:id>',views.editacliente),
    path('movcliente/<int:id>',views.cadlistcliente),
]

 