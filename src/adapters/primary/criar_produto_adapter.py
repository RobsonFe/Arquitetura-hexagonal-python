from core.usecases import criar_produto_service


class CriarProdutoController:
    def __init__(self, use_case:criar_produto_service):
        self.use_case = use_case

    def execute(self, produto_uuid:str, nome:str, preco:float, quantidade: int ) -> dict:
        
        if not produto_uuid or not nome:
            raise ValueError("UUID do produto e nome são obrigatórios.")
        
        produto = self.use_case.create(
            produto_uuid=produto_uuid,
            nome=nome,
            preco=preco,
            quantidade=quantidade
        )
        
        return produto