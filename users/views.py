from django.shortcuts import render
from .models import User
from django.contrib.auth import logout

def login(request):
    print("entrou em login")
    if request.method == 'POST':
        email = request.POST.get('emailLogin')
        senha = request.POST.get('senhaLogin')

        usuario = auth.authenticate(
                request,
                username = "teste",
                email = email,
                password = senha
                )
        auth.login(request, usuario)
        print("logado")
    
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return render(request, 'login.html')

'''
def cadastrar(resquest):
    user = User()
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    '''

