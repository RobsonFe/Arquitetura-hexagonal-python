from abc import ABC, abstractmethod

class EstoqueRepository(ABC):
    
    """
    Camada da Aplicação que define os métodos de interação com o banco de dados
    """
    
    @abstractmethod
    def salvar_produto(self, produto_uuid:str, nome:str, preco:float, quantidade: int ) -> dict:
        pass
    
    @abstractmethod
    def buscar_produto_pelo_id(self, produto_uuid: str) -> dict:
        pass
    
    @abstractmethod
    def atualizar_produto(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        pass
    
    @abstractmethod
    def deletar_produto(self, produto_uuid: str) -> dict:
        pass
    
    @abstractmethod
    def listar_produtos(self) -> list:
        pass