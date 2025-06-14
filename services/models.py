from django.db import models
from users.models import User, Endereco
from django.utils import timezone


STATUS_TICKET = [
        ("A", "Aberto"),
        ("F", "Fechado"),
        ("C", "Cancelado")
        ]

STATUS_ORCAMENTO = [
        ("A", "Aceito"),
        ("R", "Recusado"),
        ("E", "Em análise")
        ]

STATUS_SERVICE = [
        ("P", "Pendente"),
        ("F", "Finalizado"),
        ("E", "Em andamento")
        ]

CATEGORY_CHOICE = [
        ("ES", "Escoamento"),
        ("PI", "Pintura"),
        ("RE", "Reforma"),
        ("CO", "Construção"),
        ("VI", "Vidracaria"),
        ("MA", "Marcenaria"),
        ("FR", "Freteiro"),
        ("MO", "Montagem"),
        ("EL", "Elétrica")
        ]

class TicketServico(models.Model):
    status = models.CharField(max_length=1, choices=STATUS_TICKET, default="C")
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default="RE")
    dataCriacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(blank=True, null=True)

class Orcamento(models.Model):
    status = models.CharField(max_length=1, choices=STATUS_ORCAMENTO, default="E")
    ticket = models.ForeignKey(TicketServico, on_delete=models.SET_NULL, null=True, related_name='orcamentos')
    prestador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    dataCriacao = models.DateTimeField(default=timezone.now)
    prazo = models.DateField()

class Service(models.Model):
    ticket = models.ForeignKey(TicketServico, on_delete=models.SET_NULL, null=True)
    orcamento = models.ForeignKey(Orcamento, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=STATUS_SERVICE, default="E")
    dataInicio = models.DateField()
    dataConclusao = models.DateField()


