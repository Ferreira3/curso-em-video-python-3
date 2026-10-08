# Desafio 34

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str = None, salario: int|float = 1650):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario: int|float):
        if novo_salario > self.__salario:
            self.__salario = novo_salario
        else:
            print(f"Aviso: O salário de {self.nome} não foi alterado. O novo valor (R${novo_salario:.2f}) deve ser maior que o atual (R${self.salario:.2f}).")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        valor_bonus = self.calcular_bonus()

        return f"{self.nome} ganha R${self.salario:.2f} e por ser {self.__class__.__name__} o bônus será de R${valor_bonus:.2f}"


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10


class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08    


a = Desenvolvedor("Pedro", 1800)
a.salario = 1200
a.salario = 1900
print(a)
print(a.salario)
print(a.calcular_bonus())
