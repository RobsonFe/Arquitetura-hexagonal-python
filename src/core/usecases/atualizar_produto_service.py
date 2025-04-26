from core.ports.inputs import AtualizarProdutoUseCase
from core.ports.output import EstoqueRepository
from core.domain.entities.produto import Produto
from core.domain.value_objects.preco import Preco
from core.domain.value_objects.quantidade import Quantidade


class AtualizarProdutoService(AtualizarProdutoUseCase):

    def __init__(self, produto_repository: EstoqueRepository):
        self.produto_repository = produto_repository

    def update(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        preco_obj = Preco(preco)
        quantidade_obj = Quantidade(quantidade)

        produto = Produto(produto_uuid, nome, preco_obj, quantidade_obj)
        produto.validar()

        return self.produto_repository.update(
            produto_uuid=produto_uuid,
            nome=nome,
            preco=preco_obj.valor,
            quantidade=quantidade_obj.valor
        )
