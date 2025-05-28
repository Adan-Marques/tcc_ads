from django.db import models
from users.models import User, Endereco
from django.utils import timezone


STATUS_CHOICE = [
        ("A", "Aberto"),
        ("F", "Fechado"),
        ("C", "Cancelado")
        ]

CATEGORY_CHOICE = [
        ("ES", "Escoamento"),
        ("PI", "Pintura"),
        ("RE", "Reforma"),
        ("CO", "Construcao"),
        ("VI", "Vidracaria"),
        ("MA", "Marcenaria"),
        ("FR", "Freteiro"),
        ("MO", "Montagem"),
        ("EL", "Eletrica")
        ]

class TicketServico(models.Model):
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="C")
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default="RE")
    dataCriacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(upload_to="media", null=True)

class Service(models.Model):
    pass


class Orcamento(models.Model):
    pass
