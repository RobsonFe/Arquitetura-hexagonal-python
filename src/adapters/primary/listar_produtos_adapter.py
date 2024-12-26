from core.usecases import listar_produtos_service


class ListarProdutosController:
    def __init__(self, use_case: listar_produtos_service):
        self.use_case = use_case

    def handle(self):
        return self.use_case.ListarProdutos()