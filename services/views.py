from django.shortcuts import render
from .models import TicketServico
from users.models import Endereco
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def cadastroTicket(request):
    if request.user.type_user == 'P':
        return HttpResponse("Montar página 404")

    ticket = TicketServico()
    endereco = Endereco()
    if request.method == 'POST':
        
        endereco.cep = request.POST.get('cep')
        endereco.logradouro = request.POST.get('logradouro')
        endereco.numero = request.POST.get('numero')
        endereco.complemento = request.POST.get('complemento')
        endereco.bairro = request.POST.get('bairro')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        endereco.referencia = request.POST.get('referencia')
        endereco.tipo = request.POST.get('tipo')
        endereco.save()

        ticket.status = "A"
        ticket.solicitante = request.user
        ticket.categoria = request.POST.get('categoria')
        ticket.descricao = request.POST.get('descricao')
        ticket.endereco = endereco
        ticket.imagem = request.FILES.get('imagem')
        ticket.save()
    return render(request, 'cliente/ticket.html')


@login_required
def ticketUser(request):
    if request.user.type_user == 'P':
        return HttpResponse('*Fazer uma paǵina 404*')
    ticket_user = TicketServico.objects.filter(solicitante = request.user)
    tickets_abertos = TicketServico.objects.filter(solicitante=request.user, status='A').count()
    tickets_fechados = TicketServico.objects.filter(solicitante=request.user, status='F').count()
    tickets_cancelados = TicketServico.objects.filter(solicitante=request.user, status='C').count()
    context = { 
            'ticket_user': ticket_user,
            'tickets_abertos': tickets_abertos,
            'tickets_fechados': tickets_fechados,
            'tickets_cancelados': tickets_cancelados,
            }
    return render(request, 'cliente/ticketUsuario.html', context)





