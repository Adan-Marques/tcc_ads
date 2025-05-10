from django.urls import path
from services import views

urlpatterns = [
    path('cadastroticket/', views.cadastroTicket, name='cadastroticket'),
]
