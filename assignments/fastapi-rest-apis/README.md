# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Crie uma API REST com FastAPI para cadastrar e consultar livros. Você praticará rotas HTTP, modelos de dados, operações CRUD e respostas de erro.

## 📝 Tasks

### 🛠️ Executar a API e Explorar as Rotas

#### Descrição
Prepare o ambiente, execute o código inicial e explore os endpoints básicos da API usando a documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Instalar `fastapi` e `uvicorn` com `python -m pip install fastapi uvicorn`.
- Iniciar a aplicação com `python starter-code.py`.
- Disponibilizar `GET /` com uma mensagem de boas-vindas e `GET /health` com o status da aplicação.
- Permitir que as rotas sejam exploradas em `http://127.0.0.1:8000/docs`.

### 🛠️ Criar e Consultar Livros

#### Descrição
Implemente endpoints para adicionar livros à coleção em memória e consultar a coleção ou um livro específico. Use os modelos Pydantic fornecidos no código inicial para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para retornar todos os livros.
- Implementar `POST /books` para criar um livro com título, autor e ano de publicação, atribuindo um ID único.
- Responder à criação com o status HTTP `201` e os dados do livro criado.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID ou responder com status `404` quando ele não existir.

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete as operações CRUD implementando a atualização e a remoção de livros existentes. Trate IDs inexistentes sem interromper a aplicação.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar título, autor e ano de publicação de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com status HTTP `204`.
- Responder com status HTTP `404` ao tentar atualizar ou remover um ID inexistente.
- Manter os dados em memória e permitir testar as operações pela documentação interativa em `/docs`.