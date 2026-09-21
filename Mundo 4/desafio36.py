# Desafio 36

from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self):
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor

    def fvalor(self):
        return f"R${self._valor:.2f}"

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def pagar(self):
        return f"Pagamento CONFIRMADO de {self.fvalor()} via Boleto bancário"


class Pix(Pagamento):
    def pagar(self):
        return f"Pagamento CONFIRMADO de {self.fvalor()} via Pix"


class CartaoCredito(Pagamento):
    def pagar(self):
        return f"Pagamento CONFIRMADO de {self.fvalor()} via Cartão de Crédito"


def finalizar_compra(metodo_pagamento:Pagamento, valor:int|float):
    try:
        metodo_pagamento.valor = valor
        print(metodo_pagamento.pagar())
    except Exception as e:
        print(e)
        print("ERRO: Não foi possível finalizar a compra")

finalizar_compra(Pix(), 810)
finalizar_compra(Boleto(), 150)
finalizar_compra(CartaoCredito(), 560)
