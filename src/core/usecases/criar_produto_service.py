from core.exceptions.exceptions import PrecoError, QuantidadeError
from core.ports.inputs import CriarProdutoUseCase
from core.ports.output import EstoqueRepository


class CriarProdutoService(CriarProdutoUseCase):

    def __init__(self, repository: EstoqueRepository):
        self.repository = repository

    def create(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:

        if preco <= 0:
            raise PrecoError(preco)

        if quantidade <= 0:
            raise QuantidadeError(quantidade)

        return self.repository.save(produto_uuid, nome, preco, quantidade)
