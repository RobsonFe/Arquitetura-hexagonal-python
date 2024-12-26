from core.ports.output import EstoqueRepository

class EstoqueRepositoryImpl(EstoqueRepository):
    
    def __init__(self):
        self.produtos = {}
    
    def salvar_produto(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        
        return {
            "produto_uuid": produto_uuid,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "status": "201: salvo lindamente!"
        }
        
    def buscar_produto_pelo_id(self, produto_uuid: str) -> dict:
        produto = self.produtos.get(produto_uuid)
        return {
            "produto_uuid": produto_uuid,
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": produto["quantidade"],
            "status" : "200: produto encontrado com maestria!"
        }
    
    def atualizar_produto(self, produto_uuid: str, nome: str, preco: float, quantidade: int) -> dict:
        
        produto = self.produtos.get(produto_uuid)
        
        if produto:
            produto["nome"] = nome
            produto["preco"] = preco
            produto["quantidade"] = quantidade
            return {
                "produto_uuid": produto_uuid,
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade,
                "status": "200: Produto atualizado para mais bonito!"
            }
        
        return {
            "produto_uuid": produto_uuid,
            "status": "404: Produto não encontrado!"
        }
        
    def deletar_produto(self, produto_uuid: str) -> dict:
        produto = self.produtos.pop(produto_uuid, None)
        
        if produto:
            return {
                "produto_uuid": produto_uuid,
                "status": "200: Produto deletado por ser muito tabacudo!"
            }
        
        return {
            "produto_uuid": produto_uuid,
            "status": "404: Produto não encontrado!"
        }
        
    
    def listar_produtos(self) -> list:
        return list(self.produtos.values())