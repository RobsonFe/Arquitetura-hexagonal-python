
from core.exceptions.exceptions import ProdutoSemEstoqueError
from core.ports.inputs import ListarProdutosUseCase
from core.ports.output import EstoqueRepository


class ListarProdutos(ListarProdutosUseCase):
    
    def __init__(self, repository: EstoqueRepository):
        self.repository = repository

    def list(self) -> list:
        
        if not self.repository:
            raise ProdutoSemEstoqueError()
        
        return self.repository.list()