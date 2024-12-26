from core.ports.inputs import DeletarProdutoUseCase


class DeletarProdutoController:
    def __init__(self, use_case: DeletarProdutoUseCase):
        self.use_case = use_case

    def deletar_produto(self, produto_id):
        self.produto_repository.deletar_produto(produto_id)