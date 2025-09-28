FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements.txt da raiz do projeto
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar apenas a pasta api (onde está o manage.py)
COPY api/ .

EXPOSE 8001

# Comando para rodar o Django (dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
