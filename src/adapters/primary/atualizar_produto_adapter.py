from core.usecases import atualizar_produto_service


class AtualizarProdutoController:
    def __init__(self, use_case:atualizar_produto_service):
        self.use_case = use_case
        
    def handle_atualizar_produto(self, produto_uuid:str, nome:str, preco:float, quantidade: int ) -> dict:
        
        if not produto_uuid or not nome:
            raise ValueError("UUID do produto e nome são obrigatórios.")
        
        produto = self.use_case.atualizar_produto(
            produto_uuid=produto_uuid,
            nome=nome,
            preco=preco,
            quantidade=quantidade
        )
        
        return produto
        