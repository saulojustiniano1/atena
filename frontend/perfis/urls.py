from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_perfis, name="perfis_lista"),
    path("novo/", views.criar_perfil, name="perfis_novo"),
]
