import os

import requests
from django.contrib import messages
from django.shortcuts import redirect, render
from requests.exceptions import JSONDecodeError, RequestException

API_URL = os.getenv("API_URL")
API_URL_TOKEN = os.getenv("API_URL_TOKEN")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        resp = requests.post(
            f"{API_URL_TOKEN}/auth/token/",
            data={
                "username": username,
                "password": password,
            },
        )

        if resp.status_code == 200:
            tokens = resp.json()
            request.session["access"] = tokens["access"]
            request.session["refresh"] = tokens["refresh"]
            return redirect("dashboard")
        else:
            print(resp)
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "core/login.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")


def dashboard_view(request):
    access = request.session.get("access")
    headers = {"Authorization": f"Bearer {access}"} if access else {}

    cursos = []
    disciplinas = []

    try:
        resp_cursos = requests.get(
            f"{API_URL}/cursos/?ativo=true", headers=headers, timeout=5
        )
        if resp_cursos.status_code == 200:
            cursos = resp_cursos.json()
        else:
            messages.error(request, f"Erro ao buscar cursos: {resp_cursos.status_code}")

        resp_disciplinas = requests.get(
            f"{API_URL}/disciplinas/?ativo=true", headers=headers, timeout=5
        )
        if resp_disciplinas.status_code == 200:
            disciplinas = resp_disciplinas.json()
        else:
            messages.error(
                request, f"Erro ao buscar disciplinas: {resp_disciplinas.status_code}"
            )

    except (RequestException, JSONDecodeError) as e:
        messages.error(request, f"Não foi possível conectar à API: {e}")

    context = {
        "cursos_count": len(cursos),
        "disciplinas_count": len(disciplinas),
    }
    return render(request, "core/dashboard.html", context)
