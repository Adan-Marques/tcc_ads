from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from .models import Endereco
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def logout_view(request):
    return logout_then_login(request)

def cadastro(request):
    user = User()
    endereco = Endereco()
    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('confirm-password'):
            messages.error(request, "As senhas não coincidem!")
            return redirect('cadastro')
        user.cpf = request.POST.get('cpf')
        user.first_name = request.POST.get('nome')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.last_name = request.POST.get('sobrenome')
        user.telefone = request.POST.get('telefone')
        senha = request.POST.get('password')
        user.type_user = request.POST.get('type')
        if senha:
            user.set_password(senha)
        endereco.cep = request.POST.get('cep')
        endereco.logradouro = request.POST.get('logradouro')
        endereco.numero = request.POST.get('numero')
        endereco.complemento = request.POST.get('complemento')
        endereco.bairro = request.POST.get('bairro')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        endereco.referencia = request.POST.get('referencia')
        endereco.tipo = request.POST.get('tipo_end')
        endereco.save()
        user.endereco = endereco
        user.save()
        messages.success(request, "Cadastro realizado com sucesso!")
    return render(request, 'cadastro.html')

@login_required
def meuPerfil(request):
    user_info = request.user
    aba = request.POST.get('aba')

    if request.method == 'POST':
        if aba == 'pessoal':
            user_info.first_name = request.POST.get('nome')
            user_info.last_name = request.POST.get('sobrenome')
            user_info.email = request.POST.get('email')
            user_info.telefone = request.POST.get('telefone')
            user_info.save()
            messages.success(request, 'Dados pessoais atualizados com sucesso!')

        elif aba == 'senha':
            senha = request.POST.get('password')
            confirmar = request.POST.get('confirm-password')

            if senha and senha == confirmar:
                user_info.set_password(senha)
                user_info.save()
                update_session_auth_hash(request, user_info)
                messages.success(request, 'Senha atualizada com sucesso!')
            else:
                messages.error(request, 'As senhas não coincidem ou estão vazias.')

        elif aba == 'endereco':
            endereco = user_info.endereco
            if not endereco:
                endereco = Endereco.objects.create(
                    cep='',
                    bairro='',
                    cidade='',
                    estado='',
                    logradouro='',
                    numero='',
                    tipo='Residencial'
                )
                user_info.endereco = endereco
                user_info.save()

            endereco.cep = request.POST.get('cep')
            endereco.logradouro = request.POST.get('logradouro')
            endereco.numero = request.POST.get('numero')
            endereco.complemento = request.POST.get('complemento')
            endereco.bairro = request.POST.get('bairro')
            endereco.cidade = request.POST.get('cidade')
            endereco.estado = request.POST.get('estado')
            endereco.referencia = request.POST.get('referencia')
            endereco.tipo = request.POST.get('tipo_end')
            endereco.save()

            messages.success(request, 'Endereço atualizado com sucesso!')

        return redirect('meu-perfil')
    context = { 'user_info': user_info }
    return render(request, 'meuPerfil.html', context)

def page_not_found(request):
    # Render the 404 page
    return render(request, 'page_not_found.html')




