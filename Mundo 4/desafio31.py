# Desafio 31

from rich import inspect

class Retangulo():
    def __init__(self, base=1, altura=1):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, bas):
        if bas > 0:
            self._base = bas
        else:
            raise ValueError('Erro! Base inválida')

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, alt):
        if alt > 0:
            self._altura = alt
        else:
            raise ValueError('Erro! Altura inválida')

    @property
    def medidas(self):
        return [self._base, self._altura, self.area]

    @medidas.setter
    def medidas(self, med=(1, 1)):
        self.base = med[0]
        self.altura = med[1]

    @property
    def area(self):
        return self._base * self._altura

    @area.setter
    def area(self, a):
        raise ValueError ("ERRO: Você não tem permissão para alterar a área!")


r = Retangulo(2, 5)
print(r.medidas)
