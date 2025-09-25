import uuid

from django.db import models

TIPO_USER = [("GERENTE", "Gerente"), ("PROFESSOR", "Professor"), ("ALUNO", "Aluno")]


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_USER, default="ALUNO")
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)


class Curso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)
    carga_horaria_total = models.IntegerField()


class Disciplina(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
