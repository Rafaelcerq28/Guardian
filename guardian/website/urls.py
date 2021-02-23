from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

#url a ser digitada na barra de navegação e caminho para o método correspondente a ela na view

urlpatterns = [
    path('',views.login),
    path('index',views.index),
    path('cadprodutos',views.cadprodutos),
    path('listaprodutos',views.listaprodutos),
    path('exibeproduto/<int:id>',views.exibeproduto),
    path('editaproduto/<int:id>',views.editaproduto),
    path('deletaproduto/<int:id>',views.deletaproduto),
]