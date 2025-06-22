from model.domains.produto import Produto, db

class ProdutoRepository:
    @staticmethod
    def find_all():
        return Produto.query.all()

    @staticmethod
    def find_by_id(produto_id):
        return Produto.query.get(produto_id)

    @staticmethod
    def find_by_nome(nome):
        return Produto.query.filter(Produto.nome.ilike(f'%{nome}%')).all()

    @staticmethod
    def save(produto):
        db.session.add(produto)
        db.session.commit()
        return produto

    @staticmethod
    def delete(produto):
        db.session.delete(produto)
        db.session.commit()

    @staticmethod
    def count():
        return Produto.query.count()