import os

import requests
from django.contrib import messages
from django.shortcuts import redirect, render

API_URL = os.getenv("API_URL", "http://api:8001/api")


def lista_disciplinas(request):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}
    try:
        resp = requests.get(f"{API_URL}/disciplinas/", headers=headers, timeout=5)
        resp.raise_for_status()
        disciplinas = resp.json()
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar disciplinas: {e}")
        disciplinas = []

    return render(request, "disciplinas/lista.html", {"disciplinas": disciplinas})


def criar_disciplina(request):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    cursos = []
    try:
        resp_cursos = requests.get(f"{API_URL}/cursos/", headers=headers, timeout=5)
        resp_cursos.raise_for_status()
        cursos = resp_cursos.json()
    except requests.RequestException:
        messages.error(request, "Erro ao buscar cursos para cadastro de disciplina.")

    if request.method == "POST":
        ativo = request.POST.get("ativo") == "true"

        data = {
            "codigo": request.POST.get("codigo", "").strip(),
            "nome": request.POST.get("nome", "").strip(),
            "carga_horaria": int(request.POST.get("carga_horaria") or 0),
            "curso": request.POST.get("curso"),
            "ativo": ativo,
        }

        try:
            resp = requests.post(
                f"{API_URL}/disciplinas/", json=data, headers=headers, timeout=5
            )
            resp.raise_for_status()
            messages.success(request, "Disciplina criada com sucesso!")
            return redirect("disciplinas_lista")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao criar disciplina: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return render(request, "disciplinas/form.html", {"cursos": cursos})


def editar_disciplina(request, disciplina_id):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    disciplina = {}
    try:
        resp = requests.get(
            f"{API_URL}/disciplinas/{disciplina_id}/", headers=headers, timeout=5
        )
        resp.raise_for_status()
        disciplina = resp.json()
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar a disciplina: {e}")
        return redirect("disciplinas_lista")

    cursos = []
    try:
        resp_cursos = requests.get(f"{API_URL}/cursos/", headers=headers, timeout=5)
        resp_cursos.raise_for_status()
        cursos_data = resp_cursos.json()
        cursos = (
            cursos_data.get("results", [])
            if isinstance(cursos_data, dict)
            else cursos_data
        )
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar cursos: {e}")

    if request.method == "POST":
        ativo = request.POST.get("ativo") == "true" or request.POST.get("ativo") == "on"

        data = {
            "codigo": request.POST.get("codigo", "").strip(),
            "nome": request.POST.get("nome", "").strip(),
            "carga_horaria": int(request.POST.get("carga_horaria") or 0),
            "curso": request.POST.get("curso"),
            "ativo": ativo,
        }

        try:
            resp = requests.put(
                f"{API_URL}/disciplinas/{disciplina_id}/",
                json=data,
                headers=headers,
                timeout=5,
            )
            resp.raise_for_status()
            messages.success(request, "Disciplina atualizada com sucesso!")
            return redirect("disciplinas_lista")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao atualizar disciplina: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return render(
        request, "disciplinas/form.html", {"disciplina": disciplina, "cursos": cursos}
    )
