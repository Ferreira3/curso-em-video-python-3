# Desafio 27

from abc import ABC, abstractmethod
from random import randint, choice
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        golpe = choice(self.golpes)

        print(f"[yellow]{self.nome}[/][green]({self.vida})[/] atacou [yellow]{alvo.nome}[/][green]({alvo.vida})[/] com um {golpe} de [blue]Força {forca}[/]")
        alvo.receber_dano(forca)

    def receber_dano(self, dano):
        dano_causado = randint(1, dano)
        print(f"[yellow]{self.nome}[/][green]({self.vida})[/] recebeu [red]{dano_causado} de dano![/]")
        self.vida -= dano_causado

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def curar(self):
        cura = randint(100, 500)
        print(f"[yellow]{self.nome}[/][green]({self.vida})[/] amarrou uma bandagem para se [green]curar em {cura}[/] pontos de vida")


class Mago(Personagem):
    def curar(self):
        cura = randint(300, 900)
        print(f"[yellow]{self.nome}[/][green]({self.vida})[/] bebeu uma poção mágica para se [green]curar em {cura}[/] pontos de vida")


p1 = Guerreiro("Kratos", 5000, ["Pulo Giratório", "Chuva de Lâminas"])
p2 = Mago("Veigar", 2500, ["Explosão Galática", "Bola de Fogo"])
p1.atacar(p2, 500)
p2.curar()
p1.curar()
p2.atacar(p1, 500)
p1.curar()