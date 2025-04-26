from abc import ABC, abstractmethod
from core.domain.entities.produto import Produto


class CriarProdutoUseCase(ABC):

    @abstractmethod
    def create(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        pass


class AtualizarProdutoUseCase(ABC):

    @abstractmethod
    def update(self, produto_uuid: str, produto: Produto) -> dict:
        pass


class ListarProdutosUseCase(ABC):

    @abstractmethod
    def list(self) -> list:
        pass


class DeletarProdutoUseCase(ABC):

    @abstractmethod
    def delete(self, produto_uuid: str) -> dict:
        pass


class BuscarProdutoUseCase(ABC):

    @abstractmethod
    def find(self, produto_uuid: str) -> dict:
        pass
