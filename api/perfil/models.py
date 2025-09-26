import uuid

from django.db import models
from django.utils import timezone

TIPO_USER = [
    ("GERENTE", "Gerente"),
    ("PROFESSOR", "Professor"),
    ("ALUNO", "Aluno"),
]


class Perfil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=30, unique=True, editable=False)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_USER, default="ALUNO")
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    ativo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            ano = timezone.now().year
            count = Perfil.objects.filter(codigo__startswith=f"MAT.{ano}.").count() + 1
            self.codigo = f"MAT.{ano}.{count}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
