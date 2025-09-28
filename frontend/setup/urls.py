from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("perfis/", include("perfis.urls")),
    path("cursos/", include("cursos.urls")),
    path("disciplinas/", include("disciplinas.urls")),
]
