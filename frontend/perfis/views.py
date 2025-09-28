import os

import requests
from django.contrib import messages
from django.shortcuts import redirect, render

API_URL = os.getenv("API_URL", "http://api:8001/api")


def lista_perfis(request):
    headers = {"Authorization": f"Bearer {request.session.get('access')}"}
    resp = requests.get(f"{API_URL}/perfis/", headers=headers)
    perfis = resp.json() if resp.status_code == 200 else []
    return render(request, "perfis/lista.html", {"perfis": perfis})


def criar_perfil(request):
    headers = {"Authorization": f"Bearer {request.session.get('access')}"}
    if request.method == "POST":
        data = {
            "nome": request.POST.get("nome"),
            "codigo": request.POST.get("codigo"),
            "tipo": request.POST.get("tipo"),
        }
        resp = requests.post(f"{API_URL}/perfis/", json=data, headers=headers)
        if resp.status_code == 201:
            messages.success(request, "Perfil criado!")
            return redirect("perfis_lista")
        else:
            messages.error(request, resp.text)
    return render(request, "perfis/form.html")
