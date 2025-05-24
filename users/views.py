from django.shortcuts import render
from .models import User
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from .models import Endereco
from django.http import HttpResponse

def logout_view(request):
    return logout_then_login(request)

def cadastro(request):
    user = User()

    if request.method == 'POST':
        user.cpf = request.POST.get('cpf')
        user.first_name = request.POST.get('nome')
        user.username = request.POST.get('nome')
        user.email = request.POST.get('email')
        user.last_name = request.POST.get('sobrenome')
        user.telefone = request.POST.get('telefone')
        senha = request.POST.get('password')
        user.type_user = request.POST.get('type')
        if senha:
            user.set_password(senha)
        user.save()
        if not user.cpf or not user.username or not user.email or not senha:
            return HttpResponse("Por favor, preencha todos os campos obrigatórios.")
        if len(senha) < 8:
            return HttpResponse("A senha deve ter no mínimo 8 caracteres.")
        endereco = Endereco()
        endereco.user = user
        endereco.logradouro = request.POST.get('logradouro')
        endereco.numero = request.POST.get('numero')
        endereco.bairro = request.POST.get('bairro')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        endereco.cep = request.POST.get('cep')
        endereco.pais = request.POST.get('pais')
        endereco.complemento = request.POST.get('complemento')
        endereco.tipo = request.POST.get('tipo')
        endereco.save()

        return HttpResponse("Cadastro realizado com sucesso.")


    return render(request, 'cadastro.html')



@login_required
def ticketUsuario(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'cliente/ticketUsuario.html')

def ticketPrestador(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'prestador/ticketPrestador.html')

def detalhesPedido(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'cliente/detalhesPedido.html')



