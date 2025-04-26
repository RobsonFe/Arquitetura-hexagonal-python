from abc import ABC, abstractmethod


class EstoqueRepository(ABC):

    """
    Camada da Aplicação que define os métodos de interação com o banco de dados
    """

    @abstractmethod
    def save(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        pass

    @abstractmethod
    def find(self, produto_uuid: str) -> dict:
        pass

    @abstractmethod
    def update(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        pass

    @abstractmethod
    def delete(self, produto_uuid: str) -> dict:
        pass

    @abstractmethod
    def list(self) -> list:
        pass
