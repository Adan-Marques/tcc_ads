from django.shortcuts import render
from .models import TicketServico

# Fazer o cadastro de ticket

def cadastroTicket(request):
    ticket = TicketServico()
    # TODO: corrigir isso
    from users.models import Endereco
    from users.models import User

    if request.method == 'POST':
        ticket.status = "A"
        ticket.solicitante = User.objects.all()[0]
        ticket.categoria = "VI"
        ticket.descricao = request.POST.get('descricao')
        ticket.endereco = Endereco.objects.all()[0]
        ticket.save()
    return render(request, 'ticket.html')
