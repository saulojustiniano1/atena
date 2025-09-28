import requests
from django.contrib import messages
from django.shortcuts import redirect, render

API_URL = "http://localhost:8001/api"
API_URL_TOKEN = "http://localhost:8001"


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
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "core/login.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")


def dashboard_view(request):
    access = request.session.get("access")
    headers = {"Authorization": f"Bearer {access}"} if access else {}

    cursos = requests.get(f"{API_URL}/cursos/?ativo=true", headers=headers).json()
    disciplinas = requests.get(
        f"{API_URL}/disciplinas/?ativo=true", headers=headers
    ).json()

    context = {
        "cursos_count": len(cursos),
        "disciplinas_count": len(disciplinas),
    }
    return render(request, "core/dashboard.html", context)
