#!/bin/sh

echo "Rodando migrations..."
python manage.py migrate --noinput

echo "Criando superusuário..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists(): \
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

echo "Iniciando o servidor..."
exec "$@"
