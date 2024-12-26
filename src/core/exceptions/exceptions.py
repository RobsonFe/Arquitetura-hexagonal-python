class PrecoError(Exception):
    
    def __init__(self, preco:float , message="O Preço do Produto não pode ser negativo"):
        self.preco = preco
        self.message = message = f"{message}. Preço recebido: {preco}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
    
class QuantidadeError(Exception):
    
    def __init__(self, quantidade: int, message="A Quantidade do Produto não pode ser menor do que zero"):
        self.quantidade = quantidade
        self.message = message = f"{message}. Quantidade recebida: {quantidade}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
    
class ProdutoError(Exception):
    
    def __init__(self, produto_uuid:str, message="Produto não encontrado"):
        self.produto_uuid = produto_uuid
        self.message = message = f"{message}. Produto recebido: {produto_uuid}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
    
class ProdutoJaExisteError(Exception):
    
    def __init__(self, produto_uuid:str, message="Produto já existe"):
        self.produto_uuid = produto_uuid
        self.message = message = f"{message}. Produto recebido: {produto_uuid}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
    
class ProdutoNaoEncontradoError(Exception):
    
    def __init__(self, produto_uuid:str, message="Produto não encontrado"):
        self.produto_uuid = produto_uuid
        self.message = message = f"{message}. Produto recebido: {produto_uuid}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
    
class ProdutoSemEstoqueError(Exception):
    
    def __init__(self, message="Estoque Vazio"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message