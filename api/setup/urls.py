from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .routers import urlpatterns as router
from .swagger import swagger

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router)),
    path("swagger/", swagger.with_ui("swagger", cache_timeout=0)),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
