from django.db import models
from django.db.models.fields import CharField

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome
