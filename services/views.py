from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import TicketServico, Orcamento, Service
from users.models import Endereco
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages


@login_required
def cadastroTicket(request):
    if request.user.type_user == 'P':
        #return HttpResponse("Montar página 404")
        return HttpResponseForbidden("Você não tem permissão para acessar essa página")

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
        messages.success(request, "Chamado enviado com sucesso!")
    return render(request, 'cliente/ticket.html')


@login_required
def ticketUser(request):
    if request.user.type_user == 'P':
        return HttpResponse('page_not_found.html')
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


def ticketOrcamento(request, pk):

    if request.user.type_user == 'C':
        return HttpResponse('page_not_found.html')

    ticket = TicketServico.objects.get(pk=pk)

    if request.method == 'POST':
        orcamento = Orcamento()
        orcamento.ticket = ticket
        orcamento.prestador = request.user
        orcamento.valor = request.POST.get('valor')
        orcamento.dataInicio = request.POST.get('dataInicio')
        orcamento.prazo = request.POST.get('prazo')
        orcamento.descricao = request.POST.get('mensagem')
        orcamento.save()
        messages.success(request, "Orçamento enviado com sucesso!")

    context = {
            'ticket': ticket,
            }
    return render(request, 'prestador/ticketOrcamento.html', context)

def ticketPrestador(request):
    if request.user.type_user == 'C':
        return HttpResponse('page_not_found.html')

    tickets = TicketServico.objects.all()
    context = {
            'tickets': tickets,
            }
    return render(request, 'prestador/ticketPrestador.html', context)

#NÃO ESTÁ SENDO UTILIZADO
def ticketPrestadorDetalhes(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'prestador/ticketPrestadorDetalhes.html')


def detalhesPedido(request, pk):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    ticket = TicketServico.objects.get(pk=pk)
    orcamentos = Orcamento.objects.filter(ticket=ticket)
    context = {
            'orcamentos': orcamentos,
            'ticket': ticket,
            }

    return render(request, 'cliente/detalhesPedido.html', context)


def aceitarOrcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, id=pk)
    ticket = orcamento.ticket


    if Service.objects.filter(ticket=ticket).exists():
        messages.error(request, "Este ticket já possui um serviço contratado.")
        return redirect('detalhes-pedido', pk=ticket.id)

    Service.objects.create(
        ticket=ticket,
        orcamento=orcamento,
        cliente = request.user,
        prestador=orcamento.prestador,
        dataInicio = orcamento.dataInicio,
        dataConclusao = orcamento.prazo,
    )
    
    ticket.status = "F"
    ticket.save()

    Orcamento.objects.filter(ticket=ticket).exclude(id=orcamento.id).update(status='R')

    messages.success(request, "Serviço contratado com sucesso!")
   #return redirect('detalhes-pedido', pk=ticket.id)
   #TODO: fazer página de serviço
    return HttpResponse("aba de serviço")

#def teste(request):
    # Função de teste para aceitar orçamento
    return render(request, 'teste.html')
