from django.urls import path, include
from users import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('ticketUsuario/', views.ticketUsuario, name='ticketUsuario'),
    path('ticketPrestador/', views.ticketPrestador, name='ticketPrestador'),
    path('detalhesPedido/', views.detalhesPedido, name='detalhesPedido'),
    path('meu-perfil/', views.meuPerfil, name='meu-perfil'),
    path('ticketOrcamento/', views.ticketOrcamento, name='ticketOrcamento'),
]

