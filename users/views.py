from django.shortcuts import render
from .models import User
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def logout_view(request):
    print("passou pelo logout_view")
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
        user.endereco = request.POST.get('endereco')
        senha = request.POST.get('password')
        user.type_user = request.POST.get('type')
        if senha:
            user.set_password(senha)
        user.save()

    return render(request, 'cadastro.html')

@login_required
def ticket(request):
    if request.user.type_user == 'P':
        #TODO refactor
        return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'ticket.html')


@login_required
def ticketUsuario(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'ticketUsuario.html')

def ticketPrestador(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'ticketPrestador.html')

def detalhesPedido(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'detalhesPedido.html')

