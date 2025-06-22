from flask import Blueprint, jsonify, request
from model.services.produto_service import ProdutoService

produto_bp = Blueprint('produto', __name__, url_prefix='/v1/produto')

@produto_bp.route('/', methods=['GET'])
def listar_todos():
    return jsonify(ProdutoService.listar_todos()), 200

@produto_bp.route('/<int:id>', methods=['GET'])
def buscar_por_id(id):
    produto = ProdutoService.buscar_por_id(id)
    return jsonify(produto), 200 if produto else 404

@produto_bp.route('/nome/<string:nome>', methods=['GET'])
def buscar_por_nome(nome):
    return jsonify(ProdutoService.buscar_por_nome(nome)), 200

@produto_bp.route('/', methods=['POST'])
def gravar():
    dados = request.get_json()
    try:
        produto = ProdutoService.gravar(dados)
        return jsonify(produto), 201
    except KeyError as e:
        return jsonify({'error': f'Campo obrigatório ausente: {str(e)}'}), 400

@produto_bp.route('/<int:id>', methods=['DELETE'])
def remover(id):
    if ProdutoService.remover(id):
        return '', 204
    return jsonify({'error': 'Produto não encontrado'}), 404

@produto_bp.route('/contar', methods=['GET'])
def contar():
    return jsonify({'total': ProdutoService.contar()}), 200