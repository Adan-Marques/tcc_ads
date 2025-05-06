from django.shortcuts import render
from .models import Ticket

# Fazer o cadastro de ticket

def cadastroTicket(request):
    ticket = Ticket()
    
    if request.method == 'POST':
        ticket.status = "A"
        ticket.solicitante = request.POST.get()
        ticket.categoria = request.POST.get()
        ticket.descricao = request.POST.get()
        ticket.save()
    return render(request, 'ticket.html')
