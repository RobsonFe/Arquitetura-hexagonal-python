from core.exceptions.exceptions import PrecoError, QuantidadeError
from core.ports.inputs import AtualizarProdutoUseCase
from core.ports.output import EstoqueRepository


class AtualizarProdutoService(AtualizarProdutoUseCase):
    
    def __init__(self, produto_repository: EstoqueRepository):
        self.produto_repository = produto_repository

    def update(self, produto_uuid:str, nome:str, preco:float, quantidade: int ) -> dict:
        
        if preco <= 0:
            raise PrecoError(preco)
        
        if quantidade <= 0:
            raise QuantidadeError(quantidade)
        
        return self.produto_repository.update(produto_uuid, nome, preco, quantidade)