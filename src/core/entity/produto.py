class Produto:
    def __init__(self, produto_uuid: str, nome: str, preco: float, quantidade: int):
        self.produto_uuid = produto_uuid
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
