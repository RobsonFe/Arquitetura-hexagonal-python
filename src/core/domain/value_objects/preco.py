class Preco:
    def __init__(self, valor: float):
        if valor <= 0:
            raise ValueError("Preço deve ser maior que zero")
        self.valor = valor

    def __eq__(self, other):
        if not isinstance(other, Preco):
            return False
        return self.valor == other.valor

    def __str__(self):
        return f"R$ {self.valor:.2f}"
