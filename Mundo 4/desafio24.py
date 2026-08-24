# Desafio 24

from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def ferver_agua(self):
        return "Fervendo água até a temperatura de 100°C"

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def preparar(self):
        nome_classe = self.__class__.__name__

        print(f"\n----- Preparando {nome_classe} -----")
        print("1. ", self.ferver_agua())
        print("2. ", self.misturar())
        print("3. ", self.servir())
        print(f"----- {nome_classe} está pronto(a) -----\n")


class Cafe(BebidaQuente):
    def misturar(self):
        return "Misturando o pó no filtro"

    def servir(self):
        return "Servindo na xícara de porcelana"


class Leite(BebidaQuente):
    def misturar(self):
        return "Misturando com uma colher"

    def servir(self):
        return "Servindo num copo grande"


class Cha(BebidaQuente):
    def misturar(self):
        return "Misturando ervas"

    def servir(self):
        return "Servindo numa xícara de porcelana"


b1 = Cha()
b2 = Cafe()
b3 = Leite()

b1.preparar()
b2.preparar()
b3.preparar()
