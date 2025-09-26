from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Curso
from .serializers import CursoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        ativo = self.request.query_params.get("ativo")
        codigo = self.request.query_params.get("codigo")
        search = self.request.query_params.get("search")

        if ativo is not None:
            qs = qs.filter(ativo=ativo.lower() == "true")
        if codigo:
            qs = qs.filter(codigo=codigo)
        if search:
            qs = qs.filter(nome__icontains=search)

        return qs

    @action(detail=True, methods=["patch"], url_path="inativar")
    def inativar(self, request, pk=None):
        curso = self.get_object()
        curso.ativo = False
        curso.save()
        return Response({"status": "curso inativado"})

    @action(detail=True, methods=["patch"], url_path="ativar")
    def ativar(self, request, pk=None):
        curso = self.get_object()
        curso.ativo = True
        curso.save()
        return Response({"status": "curso ativado"})
