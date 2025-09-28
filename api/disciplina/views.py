from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Disciplina
from .serializers import DisciplinaSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        curso_id = self.request.query_params.get("curso")
        ativo = self.request.query_params.get("ativo")
        search = self.request.query_params.get("search")

        if curso_id:
            qs = qs.filter(curso_id=curso_id)
        if ativo is not None:
            qs = qs.filter(ativo=ativo.lower() == "true")
        if search:
            qs = qs.filter(nome__icontains=search)

        return qs

    @action(detail=True, methods=["patch"], url_path="inativar")
    def inativar(self, request, pk=None):
        disciplina = self.get_object()
        disciplina.ativo = False
        disciplina.save()
        return Response({"status": "disciplina inativada"})

    @action(detail=True, methods=["patch"], url_path="ativar")
    def ativar(self, request, pk=None):
        disciplina = self.get_object()
        disciplina.ativo = True
        disciplina.save()
        return Response({"status": "disciplina ativada"})

    @action(detail=True, methods=["delete"], url_path="deletar")
    def deletar(self, request, pk=None):
        disciplina = self.get_object()
        disciplina.delete()
        return Response(
            {"status": "disciplina deletada"}, status=status.HTTP_204_NO_CONTENT
        )
