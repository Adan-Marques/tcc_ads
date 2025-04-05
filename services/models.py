from django.db import models
from users.models import User

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
        ("MO","Montagem"),
        ("EL", "Eletrica")
        ]

class TicketServico(models.Model):
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="C")
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default="RE")
    dataCriacao = models.DateField()
    descricao = models.TextField()




