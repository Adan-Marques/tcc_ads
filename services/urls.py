from django.urls import path
from services import views

urlpatterns = [
    path('cadastrar-ticket/', views.cadastroTicket, name='ticket'),
    path('ticket-user/', views.ticketUser, name='ticket-user'),
]
