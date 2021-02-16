from django.shortcuts import render

def index(request):
    return render(request,'website/index.html')

def login(request):
    return render(request,'website/login.html')

def cadprodutos(request):
    return render(request,'website/cadprodutos.html')