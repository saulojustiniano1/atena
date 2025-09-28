from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_disciplinas, name="disciplinas_lista"),
    path("novo/", views.criar_disciplina, name="disciplina_novo"),
    path(
        "<uuid:disciplina_id>/editar/",
        views.editar_disciplina,
        name="disciplina_editar",
    ),
]
