from core.ports.inputs import BuscarProdutoUseCase
from core.ports.output import EstoqueRepository


class BuscarPorIdService(BuscarProdutoUseCase):
    def __init__(self, repository: EstoqueRepository):
        self.repository = repository

    def buscar(self, produto_uuid: str) -> dict:
        return self.repository.find(produto_uuid)
