from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_perfis, name="perfis_lista"),
    path("novo/", views.criar_perfil, name="perfis_novo"),
    path("<uuid:perfil_id>/editar/", views.editar_perfil, name="perfil_editar"),
    path("<uuid:perfil_id>/deletar/", views.deletar_perfil, name="perfil_deletar"),
]
