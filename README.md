<h1 align="center">
  Atena - Sistema Acadêmico
</h1>

<div align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/saulojustiniano1/atena.svg" />
  
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/saulojustiniano1/atena.svg" />
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/saulojustiniano1/atena.svg" />

  <a href="https://github.com/saulojustiniano1/atena/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/saulojustiniano1/atena.svg" />
  </a>
  
  <a href="https://github.com/saulojustiniano1/atena/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/saulojustiniano1/atena.svg" />
  </a>
</div>

# Atena - Sistema Acadêmico

Sistema para gerenciamento de cursos, disciplinas e perfis de usuários, composto por uma API REST em Django REST Framework e um frontend em Django com templates HTML.

## Tecnologias

- Django 4.2+
- Django REST Framework 3.14+
- PostgreSQL 16
- Docker & Docker Compose
- JWT para autenticação

## Estrutura do Projeto

- `api/` - API REST com Django REST Framework
- `frontend/` - Aplicação Django que consome a API
- `docker-compose.yaml` - Configuração dos containers

## Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Git

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd atena
```

### 2. Executar com Docker Compose

```bash
docker compose up --build -d
```

O comando irá:

- Construir as imagens Docker
- Criar e iniciar os containers
- Executar migrações do banco de dados
- Criar um superusuário automaticamente na API

### 3. Acessar a aplicação

- **Frontend**: http://localhost:8000
- **API**: http://localhost:8001/api
- **Documentação Swagger**: http://localhost:8001/swagger/

### Credenciais padrão

- **Usuário**: admin
- **Senha**: admin

## Funcionalidades

### API REST

- **Perfis**: CRUD de usuários com tipos (Gerente, Professor)
- **Cursos**: Gerenciamento de cursos com carga horária total
- **Disciplinas**: Gerenciamento de disciplinas vinculadas a cursos
- Autenticação JWT
- Documentação Swagger/OpenAPI

### Frontend

- Interface web para gerenciamento de perfis, cursos e disciplinas
- Autenticação integrada com a API
- Templates HTML com Bootstrap
- Validação de formulários

## Endpoints da API

### Autenticação

- `POST /auth/token/` - Obter token JWT
- `POST /auth/token/refresh/` - Renovar token

### Perfis

- `GET /perfis/` - Listar perfis
- `POST /perfis/` - Criar perfil
- `GET /perfis/{id}/` - Detalhes do perfil
- `PUT /perfis/{id}/` - Atualizar perfil
- `PATCH /perfis/inativar/{id}/` - Inativar perfil
- `PATCH /perfis/ativar/{id}/` - Ativar perfil

### Cursos

- `GET /cursos/` - Listar cursos
- `POST /cursos/` - Criar curso
- `GET /cursos/{id}/` - Detalhes do curso
- `PUT /cursos/{id}/` - Atualizar curso
- `PATCH /cursos/inativar/{id}/` - Inativar curso
- `PATCH /cursos/ativar/{id}/` - Ativar curso

### Disciplinas

- `GET /disciplinas/` - Listar disciplinas
- `POST /disciplinas/` - Criar disciplina
- `GET /disciplinas/{id}/` - Detalhes da disciplina
- `PUT /disciplinas/{id}/` - Atualizar disciplina
- `PATCH /disciplinas/inativar/{id}/` - Inativar disciplina
- `PATCH /disciplinas/ativar/{id}/` - Ativar disciplina

## Regras de Negócio

- Perfis têm códigos únicos sequenciais no formato MAT.{ano}.{sequencial}
- Não podem existir dois perfis ativos com o mesmo código
- Cursos têm códigos únicos entre cursos ativos
- Disciplinas têm códigos únicos entre disciplinas ativas
- Disciplinas só podem ser adicionadas a cursos ativos
- A soma das cargas horárias das disciplinas não pode ultrapassar a carga horária total do curso
