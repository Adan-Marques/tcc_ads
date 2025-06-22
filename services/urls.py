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
    path('excluit-ticket/<int:pk>/', views.excluirTicket, name='excluir-ticket'),
    path('avaliar-ticket/', views.avaliar_ticket, name='avaliar-ticket'),
    path('minhas-avaliacoes/', views.minhas_avaliacoes, name='minhas-avaliacoes'),
]

