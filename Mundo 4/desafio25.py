# Desafio 25

from abc import ABC, abstractmethod
from rich.table import Table
from rich.console import Console

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def calc_frete(self):
        self.frete = Moto.fator * self.distancia
        return self.frete


class Caminhao(Transporte):
    fator = 1.20

    def calc_frete(self):
        if self.distancia < 50:
            raise ValueError("[red]Distância mínima de 50km não atingida.[/red]")
        self.frete = Caminhao.fator * self.distancia
        return self.frete

class Drone(Transporte):
    fator = 9.50

    def calc_frete(self):
        if self.distancia > 10:
            raise ValueError("[red]Distância máxima de 10km ultrapassada.[/red]")
        self.frete = Drone.fator * self.distancia
        return self.frete


entregas = [Moto(15), Caminhao(60), Drone(15)]

tabela_entregas = Table(title="ENTREGAS")
tabela_entregas.add_column("Modalidade")
tabela_entregas.add_column("Distância", justify='center')
tabela_entregas.add_column("Custo")

for entrega in entregas:
    try:
        custo = f"R${entrega.calc_frete():.2f}"
    except ValueError as e:
        custo = str(e)

    tabela_entregas.add_row(f"{entrega.__class__.__name__}", f"{entrega.distancia}KM", custo)

console = Console()
console.print(tabela_entregas)
