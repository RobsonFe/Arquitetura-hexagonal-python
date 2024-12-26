from abc import ABC, abstractmethod

from core.entity.produto import Produto

class CriarProdutoUseCase(ABC):
    
    @abstractmethod
    def criar_produto(self, produto_uuid:str, nome:str, preco:float, quantidade: int ) -> dict:
        pass
    
class AtualizarProdutoUseCase(ABC):
    
    @abstractmethod
    def atualizar_produto(self, produto_uuid:str, produto:Produto) -> dict:
        pass
    
class ListarProdutosUseCase(ABC):
    
    @abstractmethod
    def listar_produtos(self) -> list:
        pass
    
class DeletarProdutoUseCase(ABC):
    
    @abstractmethod
    def remover_produto(self, produto_uuid:str) -> dict:
        pass
    
class BuscarProdutoUseCase(ABC):
    
    @abstractmethod
    def buscar_produto(self, produto_uuid:str) -> dict:
        pass
    