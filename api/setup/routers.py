from curso.views import CursoViewSet
from disciplina.views import DisciplinaViewSet
from perfil.views import PerfilViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"perfis", PerfilViewSet, basename="perfis")
router.register(r"cursos", CursoViewSet, basename="cursos")
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplinas")

urlpatterns = router.urls
