# Desafio Final - API RESTful MVC

## Sobre o Projeto
Este projeto é uma API RESTful desenvolvida como parte do desafio final da disciplina de Arquitetura de Software na Faculdade XP. A API segue o padrão MVC (Model-View-Controller) e utiliza Flask com SQLite para gerenciar produtos. O objetivo é aplicar conceitos de arquitetura de software de forma prática e eficiente.

- **Tecnologias**: Python, Flask, Flask-SQLAlchemy, SQLite.
- **Funcionalidades**: CRUD completo para produtos (criar, ler, atualizar e deletar).

## Como Instalar e Executar
1. **Pré-requisitos**:
   - Python 3.7 ou superior.
   - Git instalado.
2. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/DesafioFinalArqSoftware.git
   cd DesafioFinalArqSoftware
   ```
3. **Instalar Dependências**:
   ```bash
   pip install flask flask-sqlalchemy
   ```
4. **Executar a Aplicação**:
   ```bash
   python app.py
   ```
   A API estará disponível em `http://127.0.0.1:5000`.

## Uso da API
- **Listar Todos os Produtos**: `GET /v1/produto`
- **Criar um Produto**: `POST /v1/produto` (exemplo de JSON: `{"nome": "Smartphone", "preco": 1999.99, "quantidade": 10, "codigo": "123456"}`)
- **Buscar por ID**: `GET /v1/produto/<id>`
- **Deletar por ID**: `DELETE /v1/produto/<id>`
- **Contar Produtos**: `GET /v1/produto/contar`

Teste com ferramentas como `curl`, Postman ou qualquer cliente HTTP.


