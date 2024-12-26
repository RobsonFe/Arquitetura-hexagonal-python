from core.exceptions.exceptions import ProdutoError
from core.ports.inputs import DeletarProdutoUseCase
from core.ports.output import EstoqueRepository


class DeletarProdutoService(DeletarProdutoUseCase):
    
    def __init__(self, repository:EstoqueRepository):
        self.repository = repository
    
    def remover_produto(self, produto_id:str) -> dict:
        
        if not produto_id:
            raise ProdutoError(produto_id)
        
        return self.repository.remover_produto(produto_id)