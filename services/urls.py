from django.urls import path
from services import views

urlpatterns = [
    path('cadastrar-ticket/', views.cadastroTicket, name='ticket'),
    path('ticket-user/', views.ticketUser, name='ticket-user'),
    path('ticket-orcamento/<int:pk>/', views.ticketOrcamento, name='ticket-orcamento'),
    path('ticket-prestador/', views.ticketPrestador, name='ticket-prestador'),
    path('ticket-prestador-detalhes/', views.ticketPrestadorDetalhes, name='ticket-prestador-detalhes'),
    path('page_not_found/', views.page_not_found, name='page_not_found'),
    path('detalhes-pedido/<int:pk>/', views.detalhesPedido, name='detalhes-pedido'),
    path('orcamento/<int:pk>/aceitar/', views.aceitarOrcamento, name='aceitar-orcamento'),

]

