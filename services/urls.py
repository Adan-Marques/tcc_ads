from django.urls import path
from service import views

urlpatterns = [
    path('cadastroticket/', views.cadastroTicket, name='cadastroticket'),
]
