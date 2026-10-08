# Desafio 36

from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Valor do pagamento é inválido")

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
        print(f"ERRO NO PAGAMENTO: {e}")

finalizar_compra(Pix(), -1)
finalizar_compra(Boleto(), 150)
finalizar_compra(CartaoCredito(), 560)
