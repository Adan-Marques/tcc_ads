from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')


# corrigir
def login(request):
    if request.method == 'GET':
        print("entrou em get")
    if request.method == 'POST':
        print("entrou em post")
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
                request,
                username = username,
                password = password
                )
        if usuario is not None:
            auth.login(request, usuario)
            print("logado")
        else:
            print("algo deu errado")
            print(username)
            print(password)

    return render(request, 'login.html')

def esqueci(request):
    return render(request, 'esqueci.html')
