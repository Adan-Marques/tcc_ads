from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import TicketServico, Orcamento, Service
from users.models import Endereco
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages
from .utils import user_is


@login_required
@user_is('C')
def cadastroTicket(request):
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
@user_is('C')
def ticketUser(request):
    # TODO: Estudar maneira de apresentar tickets na tela
    ticket_user = TicketServico.objects.filter(solicitante = request.user, status='A').order_by('-dataCriacao')
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


@user_is('P')
def ticketOrcamento(request, pk):
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

@user_is('P')
def ticketPrestador(request):
    tickets = TicketServico.objects.filter(status='A').order_by('-dataCriacao')
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


@user_is('C')
def detalhesPedido(request, pk):
    ticket = TicketServico.objects.get(pk=pk)
    orcamentos = Orcamento.objects.filter(ticket=ticket, status="E")
    context = {
            'orcamentos': orcamentos,
            'ticket': ticket,
            }

    return render(request, 'cliente/detalhesPedido.html', context)


@user_is('C')
def aceitarOrcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, id=pk)
    ticket = orcamento.ticket


    if Service.objects.filter(ticket=ticket).exists():
        messages.error(request, "Este ticket já possui um serviço contratado.")
        return redirect('detalhes-pedido', pk=ticket.id)

    service =  Service.objects.create(
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
    orcamento.status="A"
    orcamento.save()

    messages.success(request, "Serviço contratado com sucesso!")

    context = {
            'service': service,
            }

    return render(request, 'cliente/aceitarOrcamento.html', context)

@user_is('C')
@login_required
def excluirTicket(request, pk):
    ticket = get_object_or_404(TicketServico, pk=pk, solicitante=request.user)
    ticket.delete()
    return redirect('ticket-user')

@user_is('C')
@login_required
def recusarOrcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    ticket_id = orcamento.ticket.id
    orcamento.status="R"
    orcamento.save()
    return redirect('detalhes-pedido', pk=ticket_id)

def avaliar_ticket(request):
    
    return render(request, 'cliente/avaliarTicket.html', )

@user_is('C')
@login_required
def minhas_avaliacoes(request):
    
    return render(request, 'cliente/minhasAvaliacoes.html', )

def gerenciarTicketPrestador(request):
    
    return render(request, 'prestador/gerenciarTicketPrestador.html', )

def avaliacoesPrestador(request):
    
    return render(request, 'prestador/avaliacoesPrestador.html', )

def gerenciarTicketCliente(request):
    
    return render(request, 'cliente/gerenciarTicketCliente.html', )
