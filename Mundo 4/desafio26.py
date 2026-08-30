# Desafio 26

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome='None'):
        self.nome = nome
        
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        salario = self.calc_sal()
        texto=(f'''O salário de {self.nome} ({self.__class__.__name__}) é de R${salario:.2f} e corresponde a {(salario / self.sal_min):.1f} salários mínimos.''')
        analise = Panel(texto, title="Análise de salário", width=40)

        print(analise)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.5, horas_trab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        sal_bruto = self.valor_hora * self.horas_trab
        return round(sal_bruto * (1 - self.inss / 100), 2)


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto=1612):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        return round(self.sal_bruto * (1 - self.inss / 100), 2)


f1 = Horista("Paulo", 12, 200)
print(f1.calc_sal())
f1.analisar_sal()

f2 = Mensalista("Amanda", 9500)
print(f2.calc_sal())
f2.analisar_sal()