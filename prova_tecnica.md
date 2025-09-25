# Prova Técnica:

# Catálogo de Cursos & Disciplina

## Objetivo

Construir uma **API REST** para gerenciar **Cursos** e **Disciplinas** , com **Swagger/OpenAPI** ,
usando **Django + DRF + PostgreSQL** e empacotando tudo com **Docker/Docker Compose**.
Além disso, construir um **sistema em Django (frontend server-side)** que acessa a **API via
views** e fornece **páginas HTML** para uso humano.

## Entregáveis

1. Repositório (Git) contendo **dois projetos Django** :
   ○ api/ — projeto DRF.
   ○ frontend/ — projeto Django (templates/views) que **consome a API**.
2. README.md com:
   ○ Setup com Docker/Compose.
   ○ Variáveis de ambiente.
3. docker-compose.yml, Dockerfile de cada serviço, .env.example.
4. Migrações do Django.
5. **Swagger/OpenAPI** publicado em /swagger/ no serviço da API.

## Modelagem mínima (API)

### Perfil (USER)

```
● id (UUID/Auto)
● codigo (string curta, único ativo, sequencial e automática.
padrão(‘MAT.{ano}.{n_sequencial}’) ex.: MAT.2025.1, MAT.2025.2, ..
MAT.2025.1242)
● nome (string)
● tipo(‘Gerente’, ‘Professor’...)
● email (user)
● senha (user)
● ativo (bool, default=True)
```

### Curso

```
● id (UUID/Auto)
● codigo (string curta, único ativo, ex.: ADS2025)
● nome (string)
● descricao (text, opcional)
● ativo (bool, default=True)
● carga_horaria_total (int)
```

### Disciplina

```
● id (UUID/Auto)
● codigo ( único ativo, ex.: BD101)
● nome (string)
● carga_horaria (int)
● curso (FK → Curso)
```

```
● ativo (bool, default=True)
```

### Regras de negócio

```
● Não pode haver 2 perfis ativos/inativos com o mesmo codigo.
● Não adicionar disciplina a curso inativado.
● Não pode haver 2 cursos ativos com o mesmo codigo.
● Não pode haver 2 disciplinas ativas com o mesmo codigo.
● A soma das cargas horárias das disciplinas do curso não pode ultrapassar
carga_horaria_total.
```

## Autenticação e Autorização (API)

```
● JWT (ex.: djangorestframework-simplejwt).
● Perfil Gerente : CRUD completo (Cursos/Disciplinas).
● Endpoints de auth:
○ POST /auth/token/
○ POST /auth/token/refresh/
```

## Endpoints (API)

### Perfil

```
● GET /perfis/?ativo=true&codigo=...&search=...
● POST /perfis/
● GET /perfis/{id}/
```

```
● PUT/PATCH /perfis/{id}/
● PUT/PATCH /perfis/inativar/{id}/
● PUT/PATCH /perfis/ativar/{id}/
```

### Cursos

```
● GET /cursos/?ativo=true&codigo=...&search=...
● POST /cursos/
● GET /cursos/{id}/
● PUT/PATCH /cursos/{id}/
● PUT/PATCH /cursos/inativar/{id}/
● PUT/PATCH /cursos/ativar/{id}/
● CRUD padrão (restrito a Gerente )
```

### Disciplinas

```
● GET /disciplinas/?curso={curso_id}&ativo=true&search=bd
● POST /cursos/
● GET /cursos/{id}/
● PUT/PATCH /cursos/{id}/
● PUT/PATCH /cursos/inativar/{id}/
● PUT/PATCH /cursos/ativar/{id}/
● CRUD padrão (restrito a Gerente )
```

### Extras úteis

```
● GET /cursos/{id}/resumo/ → retornar:
○ total de disciplinas ativas
○ soma das cargas horárias ativas do curso
```

### Documentação

```
● GET /swagger/ → listar todos os endpoints e schemas.
```

## Requisitos Técnicos (API)

```
● Django 4+, DRF 3.14+, PostgreSQL 13+.
● Paginação DRF (default 10/20); Ordering & Filters (django-filter).
● Validações com mensagens claras.
● Swagger/OpenAPI (drf-spectacular ou drf-yasg).
```

## Frontend Django — Server-Side Rendering

### Objetivo do frontend

Aplicação Django **independente** que **consome a API** nas _views_ e renderiza **templates
HTML** para operação por um usuário Gerente.

### Tecnologias & restrições

```
● Django 4+;.
● Templates Django + CSS (pode usar Bootstrap).
● As views do frontend devem chamar a API.
● Armazenar o JWT da API na sessão do usuário do frontend (ex.:
request.session['api_access']).
```

### Fluxo de autenticação (frontend)

1. **Página de login** (/login/):
   ○ Formulário: usuário/senha **da API**.
   ○ A view chama POST /auth/token/ na API
   ○ Se falha: mostrar erro amigável.
2. **Logout** (/logout/):
   ○ Limpar sessão e redirecionar para /login/.

### Páginas obrigatórias (frontend)

```
● Home / Dashboard (/):
○ Cards com totais: cursos ativos, disciplinas ativas.
○ Link rápido para “Novo Curso” e “Nova Disciplina”.
● Perfis — Listagem (/perfis/):
○ Tabela com paginação, busca (search), filtro ativo, filtro tipo
○ Ações por linha: ver , editar , inativar/ativar.
● Perfis — Criar/Edit (/perfis/novo, /perfis/{id}/editar):
○ Formulário na submissão, a view envia POST/PUT para a API.
○ Exibir mensagens de validação da API no formulário.
● Cursos — Listagem (/cursos/):
○ Tabela com paginação, busca (search), filtro ativo.
○ Ações por linha: ver , editar , inativar/ativar.
● Cursos — Criar/Editar (/cursos/novo, /cursos/{id}/editar):
○ Formulário na submissão, a view envia POST/PUT para a API.
```

```
○ Exibir mensagens de validação da API no formulário.
● Cursos — Detalhe (/cursos/{id}/):
○ Metadados do curso.
○ Resumo (consumir GET /cursos/{id}/resumo/).
○ Lista de disciplinas do curso com links.
○ Botões Inativar/Ativar (chamar endpoints da API).
● Disciplinas — Listagem (/disciplinas/):
○ Tabela com busca, filtros por curso/ativo.
● Disciplinas — Criar/Editar (/disciplinas/novo,
/disciplinas/{id}/editar).
```

### Tratamento de erros (frontend)

```
● Se a API responder 401/403 → redirecionar para login com aviso.
● Validar e exibir erros de negócio vindos da AP.
● Exibir toasts/alerts para sucesso/erro (Bootstrap).
```

### Segurança

```
● CSRF ativo para formulários do frontend (POST ao próprio frontend).
● Requisições do frontend para a API usam Bearer JWT.
```

## Docker / Compose (ambos os serviços)

```
● Serviços:
○ db: PostgreSQL
```

```
○ api: Django + DRF
○ frontend: Django templates/SSR
● Variáveis:
○ API_BASE_URL=http://api:8000 (usada pelo frontend ).
● Volumes: dados do Postgres.
```

### Exemplos de comandos no README

cp .env.example .env
docker compose up --build

# migrações e superuser (na API)

docker compose exec api python manage.py migrate
docker compose exec api python manage.py createsuperuser

# abrir: API em [http://localhost:8000/](http://localhost:8000/) (Swagger em /swagger/)

# abrir: Frontend em [http://localhost:8000/](http://localhost:8000/)

_(Sugestão de portas: api:8001, frontend:8000.)_
