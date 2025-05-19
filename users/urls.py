from django.urls import path, include
from users import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket/', views.ticket, name='ticket'),
    path('ticketUsuario/', views.ticketUsuario, name='ticketUsuario'),
    path('ticketPrestador/', views.ticketPrestador, name='ticketPrestador'),
    path('detalhesPedido/', views.detalhesPedido, name='detalhesPedido'),
]

