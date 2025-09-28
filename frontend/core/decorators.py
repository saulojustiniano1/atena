from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def login_required_session(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get("access"):
            messages.warning(
                request, "Você precisa estar logado para acessar esta página."
            )
            return redirect("login")
        return view_func(request, *args, **kwargs)

    return _wrapped_view
