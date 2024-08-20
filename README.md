# **Favoritos API**

## **Descrição**

Este projeto consiste em uma API RESTful desenvolvida em Django para gerenciar clientes e suas listas de produtos favoritos. A API permite criar, atualizar, visualizar e remover clientes, assim como gerenciar a lista de produtos favoritos de cada cliente.


## **Funcionalidades**

### **Clientes:**
- Criar, visualizar, atualizar e remover clientes.
- Cada cliente possui um nome, e um endereço de e-mail único.

### **Produtos Favoritos:**
- Adicionar produtos à lista de favoritos de um cliente.
- Visualizar a lista de produtos favoritos de um cliente específico.
- Remover produtos da lista de favoritos de um cliente.

## **Tecnologias Utilizadas:**
- Linguagem: Python 3.x
- Framework: Django, Django REST Framework
- Banco de Dados: db.sqlite3

## **Pré-requisitos:**
- Python 3.x
- venv para gerenciar ambientes virtuais
- db.sqlite3 ou qualquer outro banco de dados compatível
- Postman (para testar a API)

## **Instalação:**

### **Clone este repositório:**
``git clone https://github.com/seu-usuario/magalu-favoritos-api.git``
``cd magalu-favoritos-api``

### **Crie e ative o ambiente virtual:**
``python -m venv venv``
``venv\Scripts\activate``

## **Instale as dependências:**
``pip install -r requirements.txt``

## **Aplique as migrações para criar as tabelas no banco de dados:**
``python manage.py migrate``

## **Crie um superusuário para acessar o painel administrativo:**
``python manage.py createsuperuser``

## **Inicie o servidor de desenvolvimento:**
``python manage.py runserver``

# **Uso:**

## **Testando com Postman:**

## **Clientes:**

- GET /api/clientes/ - Listar todos os clientes.
- POST /api/clientes/ - Criar um novo cliente.
- PUT /api/clientes/{id}/ - Atualizar um cliente existente.
- DELETE /api/clientes/{id}/ - Remover um cliente.

## **Produtos Favoritos:**

- GET /api/produtos_favoritos/?cliente_id={cliente_id} - Listar produtos favoritos de um cliente.
- POST /api/produtos_favoritos/ - Adicionar um produto à lista de favoritos de um cliente.
- DELETE /produtos_favoritos/{cliente_id}/{produto_id}/ - Remover um produto dos favoritos.
