from django.urls import path, include
from users import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
]

