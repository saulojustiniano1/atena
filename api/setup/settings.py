from pathlib import Path

from decouple import Csv, config
from dj_database_url import config as db_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("APP_SECRET_KEY")
DEBUG = config("APP_DEBUG", cast=bool, default=False)

ALLOWED_HOSTS = config("APP_ALLOWED_HOSTS", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("APP_CSRF_TRUSTED_ORIGINS", cast=Csv())

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
]

MY_APPS = [
    "perfil.apps.PerfilConfig",
    "curso.apps.CursoConfig",
    "disciplina.apps.DisciplinaConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Banco de Produção - PostgreSQL
DATABASES = {
    "default": db_url(
        default=config("APP_DATABASE_URL"),
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = config("APP_LANGUAGE_CODE")

TIME_ZONE = config("APP_TIMEZONE")

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
