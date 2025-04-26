from core.domain.value_objects.preco import Preco
from core.domain.value_objects.quantidade import Quantidade


class Produto:
    def __init__(self, produto_uuid: str, nome: str, preco: Preco, quantidade: Quantidade):
        self.produto_uuid = produto_uuid
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def validar(self):
        if not self.nome:
            raise ValueError("Nome do produto é obrigatório")
