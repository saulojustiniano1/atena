import uuid

from curso.models import Curso
from django.db import models


class Disciplina(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name="disciplinas"
    )
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
