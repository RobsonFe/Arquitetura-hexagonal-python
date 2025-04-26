from core.domain.entities.produto import Produto
from core.domain.value_objects.preco import Preco
from core.domain.value_objects.quantidade import Quantidade
from core.ports.inputs import CriarProdutoUseCase
from core.ports.output import EstoqueRepository


class CriarProdutoService(CriarProdutoUseCase):
    def __init__(self, repository: EstoqueRepository):
        self.repository = repository

    def create(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        preco_obj = Preco(preco)
        quantidade_obj = Quantidade(quantidade)

        produto = Produto(produto_uuid, nome, preco_obj, quantidade_obj)
        produto.validar()

        return self.repository.save(
            produto_uuid=produto_uuid,
            nome=nome,
            preco=preco_obj.valor,
            quantidade=quantidade_obj.valor
        )
