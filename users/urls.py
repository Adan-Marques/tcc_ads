from django.urls import path, include
from users import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('detalhesPedido/', views.detalhesPedido, name='detalhesPedido'),
    path('meu-perfil/', views.meuPerfil, name='meu-perfil'),
    path('page_not_found/', views.page_not_found, name='page_not_found'),
]

