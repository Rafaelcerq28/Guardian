from django.shortcuts import redirect, render
from .models import produtos
from .forms import produtoForm

#Metodos que redirecionam para as páginas

def index(request):
    return render(request,'website/index.html')

def login(request):
    return render(request,'website/login.html')

def cadprodutos(request):
    if request.method == 'POST':
        form = produtoForm(request.POST)
        
        if form.is_valid():
            prod = form.save(commit=False)
            prod.modelo = prod.modelo.upper()
            prod.fabricante = prod.modelo.upper()
            prod.tipo = prod.modelo.upper()
            prod.save()
            return redirect('/')
    form = produtoForm()
    return render(request,'website/cadprodutos.html',{'form':form})

def listaprodutos(request):
    return render(request,'website/listaprodutos.html')

def exibeproduto(request):
    return render(request,'website/exibeproduto.html')

def editaproduto(request):
    return render(request,'website/editaproduto.html')