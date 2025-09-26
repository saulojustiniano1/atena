import uuid

from django.db import models


class Curso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    carga_horaria_total = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
