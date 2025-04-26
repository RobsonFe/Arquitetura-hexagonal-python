class Quantidade:
    def __init__(self, valor: int):
        if valor <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        self.valor = valor

    def __eq__(self, other):
        if not isinstance(other, Quantidade):
            return False
        return self.valor == other.valor

    def __str__(self):
        return str(self.valor)
