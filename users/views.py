from django.shortcuts import render
from .models import User
from django.contrib.auth.views import logout_then_login

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
        type_user = request.POST.get('type')
        if senha:
            user.set_password(senha)
        user.save()

    return render(request, 'cadastro.html')

def ticket(request):
    return render(request, 'ticket.html')
