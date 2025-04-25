from adapters.primary.criar_produto_adapter import CriarProdutoController
from adapters.secondary.estoque_repository_impl import EstoqueRepositoryImpl
from core.usecases.criar_produto_service import CriarProdutoService
import uuid
import json


# Configuração dos adaptadoress
repository = EstoqueRepositoryImpl()
use_case = CriarProdutoService(repository=repository)
controller = CriarProdutoController(use_case=use_case)

produto_uuid = str(uuid.uuid4())
nome = "Notebook"
preco = 2500.0
quantidade = 10

# Simulando a chamada da API

# Post
produto = controller.execute(
    produto_uuid=produto_uuid,
    nome=nome,
    preco=preco,
    quantidade=quantidade
)

# Get
produto = controller.execute(
    produto_uuid=produto_uuid
)

# Put
produto = controller.execute(
    produto_uuid=produto_uuid,
    nome=nome,
    preco=preco,
    quantidade=quantidade
)

# Delete
produto = controller.execute(
    produto_uuid=produto_uuid
)

if __name__ == "__main__":
    print(f"Produto criado: {json.dumps(
        produto,
        indent=4,
        ensure_ascii=False
    )}")
