from django.shortcuts import render
from .models import TicketServico
from users.models import Endereco

def cadastroTicket(request):
    ticket = TicketServico()
    endereco = Endereco()
    # TODO: corrigir isso
    from users.models import User
    print(type(request.user))
    print(type(User.objects.all()[0]))
    if request.method == 'POST':
        

        endereco.cep = request.POST.get('cep')
        endereco.logradouro = request.POST.get('logradouro')
        endereco.numero = request.POST.get('numero')
        endereco.complemento = request.POST.get('complemento')
        endereco.bairro = request.POST.get('bairro')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        endereco.referencia = "NA"
        endereco.pais = "BRASIL"
        endereco.tipo = "NA"
        endereco.save()

        ticket.status = "A"
        ticket.solicitante = request.user
        ticket.categoria = request.POST.get('categoria')
        ticket.descricao = request.POST.get('descricao')
        ticket.endereco = endereco
        ticket.save()
    return render(request, 'ticket.html')










