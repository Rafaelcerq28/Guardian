from django.db import models
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import produtos, Movimentacoes, Clientes
from .forms import produtoForm, movimentacoesForm, editForm, movimentacoesCadForm, clientesForm, editCliForm
from django.core.paginator import Paginator
from django.contrib import messages
import datetime
from .metodos import Diversos

#Metodos que redirecionam para as páginas

#--- METODO DA PAGINA INICIAL ---
@login_required
def index(request):
    #Criacao do dashboard
    #Pega movimentações criadas e saidas nos ultimos 30 dias 
    entrada_ult_30d = Movimentacoes.objects.filter(tipo_mov='entrada', created_at__gte=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    saida_ult_30d = Movimentacoes.objects.filter(tipo_mov='saida',created_at__gte=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    #Pega produtos com estoque minimo e zerado
    estoque_min = produtos.objects.extra(where=["estoque <= estoque_minimo and estoque > 0"]).count()
    estoque_zerado = produtos.objects.filter(estoque__lte=0).count()
    #pega o umtimo produto cadastrado
    ultimo_cadastro = produtos.objects.all().last()#.order_by('-created_at')[0]    
    #pega a ultima movimentacao
    #variavel auxiliar que armazena o id do produto da ultima movimentacao
    aux = Movimentacoes.objects.filter(tipo_mov='saida').first()#.order_by('-id')[0]
        #pega o ultimo produto vendido
    ultima_saida = get_object_or_404(produtos,pk=aux.produto_id)
    
    #Manda os dados para a view
    return render(request,'website/index.html',{'entrada_ult_30d':entrada_ult_30d,'saida_ult_30d':saida_ult_30d,
    'estoque_min':estoque_min,'estoque_zerado':estoque_zerado,'ultimo_cadastro':ultimo_cadastro,'ultima_saida':ultima_saida})
    

#--- MÉTODO QUE REALIZA O CADASTRO DOS PRODUTOS ---
@login_required
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
            prod.estoque_minimo = abs(prod.estoque_minimo)
            prod.estoque = 0
            #Grava no banco
            prod.save()
            #Mensagem de retorno para o usuario
            messages.info(request,'Produto inserido com sucesso')
            #Redireciona para a listagem de produtos
            return redirect('/movimentacaoCad/'+ str(prod.id))
        else:
            messages.warning(request,"Parece que você inseriu uma informação inválida, tente novamente.")
            form = produtoForm()
            return render(request,'website/cadprodutos.html',{'form':form})
    #Caso não seja um POST, armazena o formulario no objeto form e redireciona ele para a tela de cadastro
    form = produtoForm()
    return render(request,'website/cadprodutos.html',{'form':form})


#--- MÉTODO PARA LISTAGEM DE PRODUTOS---
@login_required
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
@login_required
def exibeproduto(request,id):
    last_page = request.GET.get('page')
    #Busca o objeto no banco pelo ID, se não encontrar redireciona para um 404
    prod = get_object_or_404(produtos,pk=id)
    #Pega as movimentações
    movs = Movimentacoes.objects.all().filter(produto_id = prod.id)
    return render(request,'website/exibeproduto.html',{'prod':prod,'last_page':last_page,'movs':movs})


#--- MÉTODO PARA EDITAR OS PRODUTOS ---
@login_required
def editaproduto(request,id):
    #Pegao produto do banco e salva no objeto
    prod = get_object_or_404(produtos,pk=id)
    #cria um formulario do objeto retirado do banco
    form = editForm(instance=prod)
    #Verifica se a requisição é um POST
    if request.method == 'POST':
        #armazena os dados da requisição em um formulario instanciando o objeto produto
        form = editForm(request.POST,instance=prod)
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
@login_required
def deletaproduto(request,id):
    #Procura o usuario no banoc
    prod = get_object_or_404(produtos,pk=id)
    #Deleta o usuario do banco
    prod.delete()
    #Retorna uma mensagem para o usuario
    messages.info(request,"Produto deletado com sucesso")
    return redirect('/listaprodutos')

#--- Método para acessar as movimentações
@login_required
def movimentacao(request,id,idcli):
    #cria o formulario
    form = movimentacoesForm()
    #pega o produto no banco
    cliente = get_object_or_404(Clientes,pk=idcli)
    prod = get_object_or_404(produtos,pk=id)
    #Verifica se é um post
    if request.method == 'POST':    
        form = movimentacoesForm(request.POST)
        #Verifica se o form é válido e insere o id do produto na tabela movimentação
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.quantidade = abs(movimentacao.quantidade)
            movimentacao.produto = prod
            
            movimentacao.save()
            movimentacao.clientes.add(cliente)
            #corrige valores do estoque
            if movimentacao.tipo_mov == 'entrada':
                prod.estoque += abs(movimentacao.quantidade)
            else:
                prod.estoque -= abs(movimentacao.quantidade)
            #Salva o produto
            prod.save()

            #Manda uma mensagem para a tela
            messages.info(request,'Movimentação realizada com sucesso')
            return redirect('/exibeproduto/' + str(prod.id))
        else:
            messages.warning(request,'Uma ou mais informações incorretas, verifique os dados inseridos e tente novamente')
            return render(request,'website/movimentacao.html',{'form':form,'prod':prod,'cliente':cliente})
            
    #Envia o formulario para a tela
    return render(request,'website/movimentacao.html',{'form':form,'prod':prod,'cliente':cliente})


#--- Método para acessar as movimentações a partir do cadastro
@login_required
def movimentacaoCad(request,id):
    #cria o formulario
    form = movimentacoesCadForm()
    #pega o produto no banco
    prod = get_object_or_404(produtos,pk=id)
    #Verifica se é um post
    if request.method == 'POST':    
        form = movimentacoesCadForm(request.POST)
        #Verifica se o form é válido e insere o id do produto na tabela movimentação
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.quantidade = abs(movimentacao.quantidade)
            movimentacao.produto = prod
            movimentacao.tipo_mov = 'entrada'
            movimentacao.save()

            #corrige valores do estoque
            if movimentacao.tipo_mov == 'entrada':
                prod.estoque += abs(movimentacao.quantidade)
            else:
                prod.estoque -= abs(movimentacao.quantidade)
            #Salva o produto
            prod.save()

            #Manda uma mensagem para a tela
            messages.info(request,'Movimentação realizada com sucesso')
            return redirect('/exibeproduto/' + str(prod.id))
        else:
            messages.warning(request,'Uma ou mais informações incorretas, verifique os dados inseridos e tente novamente')
            return render(request,'website/movimentacaoCad.html',{'form':form,'prod':prod})
            
    #Envia o formulario para a tela
    return render(request,'website/movimentacaoCad.html',{'form':form,'prod':prod})

#Listagem de clientes
@login_required
def listaclientes(request):
    search = request.GET.get('search')
    if search:
        clientes = Clientes.objects.filter(nome__icontains=search)
    else:
        cli_list = Clientes.objects.all().order_by('nome')
        paginator = Paginator(cli_list,10)
        page = request.GET.get('page')
        clientes = paginator.get_page(page)

    return render(request,'website/listaclientes.html',{'clientes':clientes})

#Cadastro de clientes
@login_required
def cadclientes(request):
    if request.method == 'POST':
        form = clientesForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.nome = cliente.nome.upper()
            cliente.save()
            
            messages.info(request,'Cliente cadastrado com sucesso!')
            return redirect('/listaclientes')
        else:
            messages.warning(request,'Parece que você você digitou alguma informação inválida')
            form = clientesForm()
            return render(request,'website/cadclientes.html',{'form':form})
    form = clientesForm()
    return render(request,'website/cadclientes.html',{'form':form})

#Método que retorna para a lista onde há clientes em uma lista e um form para cadastrar um novo
@login_required
def cadlistcliente(request, id):

    prod = get_object_or_404(produtos,pk=id)

    #Lista
    search = request.GET.get('search')
    if search:
        clientes = Clientes.objects.filter(nome__icontains=search)
    else:
        cli_list = Clientes.objects.all().order_by('nome')
        paginator = Paginator(cli_list,5)
        page = request.GET.get('page')
        clientes = paginator.get_page(page)
    
    #Form
    if request.method == 'POST':
        form = clientesForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.nome = cliente.nome.upper()
            cliente.save()
            
            messages.info(request,'Cliente cadastrado com sucesso!')
            return redirect('/movimentacao/'+str(prod.id)+'/'+str(cliente.id))
        else:
            messages.warning(request,'Parece que você você digitou alguma informação inválida')
            form = clientesForm()
            return render(request,'website/cadlistcliente.html',{'form':form})

    form = clientesForm()
    return render(request,'website/cadlistcliente.html',{'form':form,'clientes':clientes,'prod':prod})

#Tela de exibição do cliente
@login_required
def exibecliente(request,id):
    cliente = get_object_or_404(Clientes,pk=id)
    last_page = request.GET.get('page')
    #mask cnpj
    cliente.cnpj = Diversos.mask_cnpj(cliente.cnpj)

    movimentacao = Movimentacoes.objects.filter(clientes=cliente)

    return render(request,'website/exibecliente.html',{'cliente':cliente,'last_page':last_page,'movimentacao':movimentacao})

def editacliente(request,id):
    cliente = get_object_or_404(Clientes,pk=id)

    form = editCliForm(instance=cliente)

    if request.method == 'POST':
        form = editCliForm(request.POST,instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.nome = cliente.nome.upper()
            cliente.save()

            messages.info(request,'Cliente alterado com Sucesso!')
            redireciona = '/exibecliente/' + str(cliente.id)
            return redirect(redireciona)
        else:
            return render(request,'website/editacliente.html',{'form':form,'cliente':cliente})
    return render(request,'website/editacliente.html',{'form':form,'cliente':cliente})
