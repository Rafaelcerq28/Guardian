from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

#url a ser digitada na barra de navegação e caminho para o método correspondente a ela na view

urlpatterns = [
    path('register/',views.SignUp.as_view(), name='signup'),
]

 