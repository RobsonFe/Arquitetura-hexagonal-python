from core.domain.entities.produto import Produto
from core.domain.value_objects.quantidade import Quantidade


class Estoque:
    def __init__(self):
        self.produtos = {}
        self.quantidade_total = Quantidade(0)

    def adicionar_produto(self, produto: Produto, quantidade: Quantidade):
        if produto.produto_uuid in self.produtos:
            raise ValueError("Produto já existe no estoque")

        self.produtos[produto.produto_uuid] = {
            'produto': produto,
            'quantidade': quantidade
        }
        self.quantidade_total = Quantidade(
            self.quantidade_total.valor + quantidade.valor)

    def remover_produto(self, produto_uuid: str, quantidade: Quantidade):
        if produto_uuid not in self.produtos:
            raise ValueError("Produto não encontrado no estoque")

        produto_estoque = self.produtos[produto_uuid]
        if produto_estoque['quantidade'].valor < quantidade.valor:
            raise ValueError("Quantidade insuficiente em estoque")

        produto_estoque['quantidade'] = Quantidade(
            produto_estoque['quantidade'].valor - quantidade.valor
        )
        self.quantidade_total = Quantidade(
            self.quantidade_total.valor - quantidade.valor)

    def obter_produto(self, produto_uuid: str) -> dict:
        if produto_uuid not in self.produtos:
            raise ValueError("Produto não encontrado no estoque")
        return self.produtos[produto_uuid]
