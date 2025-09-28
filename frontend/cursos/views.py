import os

import requests
from core.decorators import login_required_session
from django.contrib import messages
from django.shortcuts import redirect, render

API_URL = os.getenv("API_URL", "http://api:8001/api")


@login_required_session
def lista_cursos(request):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}
    try:
        resp = requests.get(f"{API_URL}/cursos/", headers=headers, timeout=5)
        resp.raise_for_status()
        cursos = resp.json()
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar cursos: {e}")
        cursos = []

    return render(request, "cursos/lista.html", {"cursos": cursos})


@login_required_session
def criar_curso(request):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    if request.method == "POST":
        ativo = request.POST.get("ativo") == "true"

        data = {
            "codigo": request.POST.get("codigo", "").strip(),
            "nome": request.POST.get("nome", "").strip(),
            "descricao": request.POST.get("descricao", "").strip(),
            "ativo": ativo,
            "carga_horaria_total": int(request.POST.get("carga_horaria_total") or 0),
        }

        try:
            resp = requests.post(
                f"{API_URL}/cursos/", json=data, headers=headers, timeout=5
            )
            resp.raise_for_status()
            messages.success(request, "Curso criado com sucesso!")
            return redirect("cursos_lista")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao criar curso: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return render(request, "cursos/form.html")


@login_required_session
def editar_curso(request, curso_id):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    curso = {}
    try:
        resp = requests.get(f"{API_URL}/cursos/{curso_id}/", headers=headers, timeout=5)
        resp.raise_for_status()
        curso = resp.json()
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar o curso: {e}")
        return redirect("cursos_lista")

    if request.method == "POST":
        ativo = request.POST.get("ativo") == "true" or request.POST.get("ativo") == "on"

        data = {
            "codigo": request.POST.get("codigo", "").strip(),
            "nome": request.POST.get("nome", "").strip(),
            "carga_horaria_total": int(request.POST.get("carga_horaria_total") or 0),
            "ativo": ativo,
        }

        try:
            resp = requests.put(
                f"{API_URL}/cursos/{curso_id}/", json=data, headers=headers, timeout=5
            )
            resp.raise_for_status()
            messages.success(request, "Curso atualizado com sucesso!")
            return redirect("cursos_lista")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao atualizar curso: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return render(request, "cursos/form.html", {"curso": curso})


@login_required_session
def deletar_curso(request, curso_id):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    if request.method == "POST":
        try:
            resp = requests.delete(
                f"{API_URL}/cursos/{curso_id}/", headers=headers, timeout=5
            )
            resp.raise_for_status()
            messages.success(request, "Curso excluído com sucesso!")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao excluir curso: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return redirect("cursos_lista")
