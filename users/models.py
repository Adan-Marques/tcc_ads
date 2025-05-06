from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE_CHOICE =  [
        ("C", "Cliente"),
        ("P", "Profissional"),
        ]
        

class User(AbstractUser):
    type_user = models.CharField(max_length=1, choices=TYPE_CHOICE, default="C")
    cpf = models.CharField(max_length=12)
    telefone = models.CharField(max_length=12)


class Endereco(models.Model):
    numero = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

