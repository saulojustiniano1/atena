from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_cursos, name="cursos_lista"),
    path("novo/", views.criar_curso, name="cursos_novo"),
    path("<uuid:curso_id>/editar/", views.editar_curso, name="curso_editar"),
]
