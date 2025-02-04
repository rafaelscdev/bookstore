# Bookstore API

Este projeto consiste em uma API RESTful para uma livraria, construída com Django, Django REST Framework e outras ferramentas.

## Funcionalidades

*   **Gerenciamento de livros:**
    *   Listar todos os livros
    *   Buscar livros por título, autor ou gênero
    *   Cadastrar novos livros
    *   Atualizar informações de livros existentes
    *   Remover livros
*   **Gerenciamento de autores:**
    *   Listar todos os autores
    *   Buscar autores por nome
    *   Cadastrar novos autores
    *   Atualizar informações de autores existentes
    *   Remover autores
*   **Gerenciamento de clientes:**
    *   Listar todos os clientes
    *   Buscar clientes por nome ou email
    *   Cadastrar novos clientes
    *   Atualizar informações de clientes existentes
    *   Remover clientes
*   **Gerenciamento de pedidos:**
    *   Listar todos os pedidos
    *   Buscar pedidos por cliente ou data
    *   Cadastrar novos pedidos
    *   Atualizar informações de pedidos existentes
    *   Remover pedidos

## Tecnologias utilizadas

*   **Python:** Linguagem de programação principal
*   **Django:** Framework web de alto nível
*   **Django REST Framework:** Ferramenta para criação de APIs RESTful
*   **PostgreSQL:** Banco de dados
*   **Gunicorn:** Servidor WSGI HTTP para produção
*   **Outras:** Dependências listadas no arquivo `pyproject.toml`

## Como executar

1.  **Clone o repositório:**
    ```bash
    git clone https://[https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    ```

2.  **Crie um ambiente virtual:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Ativa o ambiente virtual
    ```

3.  **Instale as dependências:**
    ```bash
    poetry install
    ```

4.  **Execute as migrações do Django:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

## Como executar com Docker

1.  **Construa a imagem Docker:**
    ```bash
    docker build -t bookstore:latest .
    ```

2.  **Execute o container Docker:**
    ```bash
    docker run -p 8000:8000 bookstore:latest
    ```

## Contribuição

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está sob a licença [Nome da sua licença].