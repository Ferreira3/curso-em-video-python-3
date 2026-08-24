# Desafio 23

from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro():
        pass

    @abstractmethod
    def area():
        pass


class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def area(self):
        return 3.14 * (self.raio ** 2)

  
q = Quadrado(20)
print(f"Um quadrado de lado {q.lado}cm tem perimetro de {q.perimetro()}cm e area de {q.area()}cm.")

c = Circulo(12)
print(f"Um círculo de radio {c.raio}cm tem circunferencia de {c.perimetro()}cm e area de {c.area()}cm.")