from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Perfil
from .serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

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
        perfil = self.get_object()
        perfil.ativo = False
        perfil.save()
        return Response({"status": "perfil inativado"})

    @action(detail=True, methods=["patch"], url_path="ativar")
    def ativar(self, request, pk=None):
        perfil = self.get_object()
        perfil.ativo = True
        perfil.save()
        return Response({"status": "perfil ativado"})

    @action(detail=True, methods=["delete"], url_path="deletar")
    def deletar(self, request, pk=None):
        perfil = self.get_object()
        perfil.delete()
        return Response(
            {"status": "perfil deletado"}, status=status.HTTP_204_NO_CONTENT
        )
