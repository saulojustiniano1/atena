#!/bin/sh

echo "Rodando migrations..."
python manage.py migrate --noinput

echo "Iniciando o servidor..."
exec "$@"
