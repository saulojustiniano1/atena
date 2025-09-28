#!/bin/sh

wait_for_db() {
    echo "Aguardando banco de dados..."
    while ! nc -z db 5432; do
        sleep 1
    done
    echo "Banco de dados está disponível!"
}

wait_for_db

echo "Rodando migrations..."
python manage.py migrate --noinput

echo "Criando superusuÃ¡rio..."
python create_superuser.py

echo "Iniciando o servidor..."
exec "$@"