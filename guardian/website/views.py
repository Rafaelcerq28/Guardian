from django.shortcuts import render

#Metodos que redirecionam para as páginas

def index(request):
    return render(request,'website/index.html')

def login(request):
    return render(request,'website/login.html')

def cadprodutos(request):
    return render(request,'website/cadprodutos.html')

def listaprodutos(request):
    return render(request,'website/listaprodutos.html')

def exibeproduto(request):
    return render(request,'website/exibeproduto.html')

def editaproduto(request):
    return render(request,'website/editaproduto.html')