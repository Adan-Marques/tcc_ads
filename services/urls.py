from django.urls import path
from services import views

urlpatterns = [
    path('cadastrar-ticket/', views.cadastroTicket, name='ticket'),
]
