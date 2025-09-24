# Imagem base com Python
FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y build-essential libfreetype6-dev libpng-dev libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Coleta arquivos estáticos
# RUN python manage.py collectstatic --noinput

# Expõe porta
EXPOSE 8334

# Comando de produção com Gunicorn
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8334"]