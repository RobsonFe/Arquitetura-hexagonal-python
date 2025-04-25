from core.ports.inputs import DeletarProdutoUseCase


class DeletarProdutoController:
    def __init__(self, use_case: DeletarProdutoUseCase):
        self.use_case = use_case

    def execute(self, produto_id):
        self.use_case.delete(produto_id)
