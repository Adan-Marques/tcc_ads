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




