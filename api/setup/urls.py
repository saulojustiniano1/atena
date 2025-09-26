from django.contrib import admin
from django.urls import include, path

from .routers import urlpatterns as router
from .swagger import swagger

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router)),
    path("swagger/", swagger.with_ui("swagger", cache_timeout=0)),
]
