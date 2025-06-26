from django.urls import path
from services import views

urlpatterns = [
    path('cadastrar-ticket/', views.cadastroTicket, name='ticket'),
    path('ticket-user/', views.ticketUser, name='ticket-user'),
    path('ticket-orcamento/<int:pk>/', views.ticketOrcamento, name='ticket-orcamento'),
    path('ticket-prestador/', views.ticketPrestador, name='ticket-prestador'),
    # NÃO ESTÁ SENDO UTILIZADO
    path('ticket-prestador-detalhes/', views.ticketPrestadorDetalhes, name='ticket-prestador-detalhes'),
    path('detalhes-pedido/<int:pk>/', views.detalhesPedido, name='detalhes-pedido'),
    path('orcamento/<int:pk>/aceitar/', views.aceitarOrcamento, name='aceitar-orcamento'),
    path('orcamento/<int:pk>/recusar/', views.recusarOrcamento, name='recusar-orcamento'),
    path('excluir-ticket/<int:pk>/', views.excluirTicket, name='excluir-ticket'),
    path('avaliar-servico/', views.avaliar_servico, name='avaliar-servico'),
    path('minhas-avaliacoes/', views.minhas_avaliacoes, name='minhas-avaliacoes'),
    path('gerenciar-tickets-prestador/', views.gerenciarTicketPrestador, name='gerenciar-tickets-prestador'),
    path('avaliacoes-prestador/', views.avaliacoesPrestador, name='avaliacoes-prestador'),
    path('gerenciar-tickets-cliente/', views.gerenciarTicketCliente, name='gerenciar-tickets-cliente'),
    path('servico/<int:servico_id>/atualizar/', views.atualizar_servico, name='atualizar-servico'),
]

