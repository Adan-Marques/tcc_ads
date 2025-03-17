from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import logout_then_login

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    return logout_then_login(request)

def esqueci(request):
    return render(request, 'esqueci.html')
