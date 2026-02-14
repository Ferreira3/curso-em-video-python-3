# Desafio 20

from rich.panel import Panel
from rich import print

class Gamer:
    
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nickname = nickname
        self.favoritos = list()
    
    # Método para adicionar jogos favoritos no registro do jogador
    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
    
    # Método para mostrar a ficha do jogador
    def ficha(self):
        favoritos_str = "\n".join(self.favoritos)
        print(Panel(
            f"Nome real: {self.nome}\nJogos favoritos:\n{favoritos_str}",
            title=f"Jogador <{self.nickname}>",
            width=40
            ))

j1 = Gamer("João Silva", "noobmaster123")
j1.add_favoritos("CS2")
j1.add_favoritos("Halo 3")
j1.add_favoritos("Starcraft 2")
j1.add_favoritos("Minecraft")
j1.ficha()
