from model.repositories.produto_repository import ProdutoRepository
from model.domains.produto import Produto

class ProdutoService:
    @staticmethod
    def listar_todos():
        return [produto.to_dict() for produto in ProdutoRepository.find_all()]

    @staticmethod
    def buscar_por_id(produto_id):
        produto = ProdutoRepository.find_by_id(produto_id)
        return produto.to_dict() if produto else None

    @staticmethod
    def buscar_por_nome(nome):
        return [produto.to_dict() for produto in ProdutoRepository.find_by_nome(nome)]

    @staticmethod
    def gravar(dados):
        produto = Produto(
            id=dados.get('id'),  # None se não informado
            nome=dados['nome'],
            descricao=dados.get('descricao', ''),
            preco=dados['preco'],
            quantidade=dados['quantidade'],
            codigo=dados['codigo']
        )
        return ProdutoRepository.save(produto).to_dict()

    @staticmethod
    def remover(produto_id):
        produto = ProdutoRepository.find_by_id(produto_id)
        if produto:
            ProdutoRepository.delete(produto)
            return True
        return False

    @staticmethod
    def contar():
        return ProdutoRepository.count()