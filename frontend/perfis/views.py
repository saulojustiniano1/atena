import os

import requests
from core.decorators import login_required_session
from django.contrib import messages
from django.shortcuts import redirect, render

API_URL = os.getenv("API_URL", "http://api:8001/api")


@login_required_session
def lista_perfis(request):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}
    perfis = []

    try:
        resp = requests.get(f"{API_URL}/perfis/", headers=headers, timeout=5)
        resp.raise_for_status()
        perfis = resp.json()
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar perfis: {e}")

    return render(request, "perfis/lista.html", {"perfis": perfis})


@login_required_session
def criar_perfil(request):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    if request.method == "POST":
        ativo = request.POST.get("ativo") == "true" or request.POST.get("ativo") == "on"
        data = {
            "nome": request.POST.get("nome", "").strip(),
            "tipo": request.POST.get("tipo", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "senha": request.POST.get("senha", "").strip(),
            "ativo": ativo,
        }

        try:
            resp = requests.post(
                f"{API_URL}/perfis/", json=data, headers=headers, timeout=5
            )
            resp.raise_for_status()
            messages.success(request, "Perfil criado com sucesso!")
            return redirect("perfis_lista")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao criar perfil: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return render(request, "perfis/form.html")


@login_required_session
def editar_perfil(request, perfil_id):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    perfil = {}
    try:
        resp = requests.get(
            f"{API_URL}/perfis/{perfil_id}/", headers=headers, timeout=5
        )
        resp.raise_for_status()
        perfil = resp.json()
    except requests.RequestException as e:
        messages.error(request, f"Erro ao buscar perfil: {e}")
        return redirect("perfis_lista")

    if request.method == "POST":
        ativo = request.POST.get("ativo") == "true" or request.POST.get("ativo") == "on"
        data = {
            "nome": request.POST.get("nome"),
            "tipo": request.POST.get("tipo"),
            "email": request.POST.get("email"),
            "ativo": request.POST.get("ativo") == "true",
            "senha": request.POST.get("senha") or None,
        }

        try:
            resp = requests.put(
                f"{API_URL}/perfis/{perfil_id}/", json=data, headers=headers, timeout=5
            )
            resp.raise_for_status()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("perfis_lista")
        except requests.RequestException as e:
            messages.error(
                request,
                f"Erro ao atualizar perfil: {e}\n{resp.text if 'resp' in locals() else ''}",
            )

    return render(request, "perfis/form.html", {"perfil": perfil})


@login_required_session
def deletar_perfil(request, perfil_id):
    access_token = request.session.get("access")
    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}

    if request.method == "POST":
        try:
            resp = requests.delete(
                f"{API_URL}/perfis/{perfil_id}/", headers=headers, timeout=5
            )
            if resp.status_code in [200, 204]:
                messages.success(request, "Perfil excluído com sucesso!")
            else:
                messages.error(
                    request, f"Erro ao excluir perfil: {resp.status_code} - {resp.text}"
                )
        except requests.RequestException as e:
            messages.error(
                request, f"Não foi possível conectar à API para excluir o perfil: {e}"
            )
    else:
        messages.warning(request, "Método inválido para excluir perfil.")

    return redirect("perfis_lista")
