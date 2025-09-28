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

---

ATENA é uma aplicação web para gerenciamento de **Cursos, Disciplinas e Perfis de Usuários**, construída com **Django REST Framework** no backend e frontend em **Django Templates/Bootstrap**.  
O projeto utiliza **Docker** para facilitar o setup de ambiente com containers isolados para **API, banco de dados e frontend**.

### Configuração

**1. Clone o repositório:**

```bash
git clone <REPO_URL>
cd atena
cd api/frontend
cp .env.example .env
cd ..
docker compose up --build
```

**2. Outras Informações**

**As migrações e a criação do superuser (na API)** já foram criados direto no Dockerfile com um script shell

**3. Endpoints**

- API: http://localhost:8001/api
- Frontend: http://localhost:8000/
