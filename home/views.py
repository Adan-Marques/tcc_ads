from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import logout_then_login
from users.models import User

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    return logout_then_login(request)

def cadastro(request):
    user = User()
    
    if request.method == 'POST':
        user.cpf = request.POST.get('cpf')
        user.first_name = request.POST.get('nome')
        user.last_name = request.POST.get('sobrenome')
        user.telefone = request.POST.get('telefone')
        user.endereco = request.POST.get('endereco')
        user.password = request.POST.get('senha')
        user.set_password(user.password)
        user.save()

    return render(request, 'cadastro.html')
