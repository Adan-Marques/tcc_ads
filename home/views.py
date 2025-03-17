from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import logout_then_login
#from django.contrib.auth.tokens.PasswordResetTokenGenerator import default_token_generator

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    return logout_then_login(request)

def esqueci(request):
    #default_token_generator
    return render(request, 'esqueci.html')
