from django.shortcuts import redirect, render,get_object_or_404
from .models import produtos, Movimentacoes
from .forms import produtoForm, movimentacoesForm
from django.core.paginator import Paginator
from django.contrib import messages

#Metodos que redirecionam para as páginas

def index(request):
    return render(request,'website/index.html')

def login(request):
    return render(request,'website/login.html')


#--- MÉTODO QUE REALIZA O CADASTRO DOS PRODUTOS ---
def cadprodutos(request):
    #Verifica se o método que está recebendo é um POST
    if request.method == 'POST':
        #Armazena o formulario no objeto form
        form = produtoForm(request.POST)
        #Verifica se os dados do formulario são válidos
        if form.is_valid():
            #Armazena os dados do formulario no objeto correspondente, salva e não faz commit
            prod = form.save(commit=False)
            #Apenas para salvar os dados com caixa alta
            prod.modelo = prod.modelo.upper()
            prod.fabricante = prod.fabricante.upper()
            prod.tipo = prod.tipo.upper()
            #Grava no banco
            prod.save()
            #Mensagem de retorno para o usuario
            messages.info(request,'Produto inserido com sucesso')
            #Redireciona para a listagem de produtos
            return redirect('/listaprodutos')
        else:
            messages.warning(request,"Parece que você inseriu uma informação inválida, tente novamente.")
            form = produtoForm()
            return render(request,'website/cadprodutos.html',{'form':form})
    #Caso não seja um POST, armazena o formulario no objeto form e redireciona ele para a tela de cadastro
    form = produtoForm()
    return render(request,'website/cadprodutos.html',{'form':form})


#--- MÉTODO PARA LISTAGEM DE PRODUTOS---
def listaprodutos(request):
    #armazena a palavra a ser pesquisada
    search = request.GET.get('search')
    #verifica se tem palava no filtro, senão passa para a proxima opcao
    if search:
        prods = produtos.objects.filter(modelo__icontains=search)
    else:
        #Seleciona os produtos do banco ordenados pelo modelo e armazena no objeto prods
        prods_list = produtos.objects.all().order_by('modelo')
        #salva a lista com os produtos no paginador e passa a quantidade de produtos a ser exibido por página
        paginator = Paginator(prods_list,10)
        #salva a pagina atual obtida pelo get
        page = request.GET.get('page')
        #salva a pagina no paginador
        prods = paginator.get_page(page)

    #envia o objeto para a tela de listagem
    return render(request,'website/listaprodutos.html',{'prods':prods})


#--- MÉTODO PARA EXIBIR O PRODUTO ---
def exibeproduto(request,id):
    last_page = request.GET.get('page')
    #Busca o objeto no banco pelo ID, se não encontrar redireciona para um 404
    prod = get_object_or_404(produtos,pk=id)
    return render(request,'website/exibeproduto.html',{'prod':prod,'last_page':last_page})


#--- MÉTODO PARA EDITAR OS PRODUTOS ---
def editaproduto(request,id):
    #Pegao produto do banco e salva no objeto
    prod = get_object_or_404(produtos,pk=id)
    #cria um formulario do objeto retirado do banco
    form = produtoForm(instance=prod)
    #Verifica se a requisição é um POST
    if request.method == 'POST':
        #armazena os dados da requisição em um formulario instanciando o objeto produto
        form = produtoForm(request.POST,instance=prod)
        #Veridica se o formulario é valido
        if form.is_valid():
            #Salva mas ainda não faz commit
            prod = form.save(commit=False)
            #Altera as variaveis
            prod.modelo = prod.modelo.upper()
            prod.fabricante = prod.fabricante.upper()
            prod.tipo = prod.tipo.upper()
            #Grava as variaveis alteradas no banco
            prod.save()
            #Redireciona para a pagina de exibição

            messages.info(request,"Produto altetado com sucesso!")
            redireciona = '/exibeproduto/' +str(prod.id)
            return redirect(redireciona)
        else:
    #Redireciona para a pagina do formulario
            return render(request,'website/editaproduto.html',{'form':form, 'prod':prod})
    return render(request,'website/editaproduto.html',{'form':form, 'prod':prod})

#--- MÉTODO PARA DELETAR OS PRODUTOS ---
def deletaproduto(request,id):
    #Procura o usuario no banoc
    prod = get_object_or_404(produtos,pk=id)
    #Deleta o usuario do banco
    prod.delete()
    #Retorna uma mensagem para o usuario
    messages.info(request,"Produto deletado com sucesso")
    return redirect('/listaprodutos')

#--- Método para acessar as movimentações
def movimentacao(request,id):
    if request.method == 'POST':
        form = movimentacoesForm(request.POST)
        if form.is_valid():
            movimentaco = form.save(commit=False)

            messages.info(request,'Movimentação')
            return redirect('/listaprodutos')

    prod = get_object_or_404(produtos,pk=id)
    form = movimentacoesForm()
    return render(request,'website/movimentacao.html',{'form':form})


