# Desafio 22

from rich.panel import Panel
from rich import print
from os import system

class ControleRemoto:
    
    def __init__(self):
        self.volume = 1
        self.canais = [1, 2, 3, 4, 5]
        self.canal = 0
        self.tv_desligada()
    
    # Método para mostrar a tv ligada, volume e canal
    def tv_ligada(self):
        while True:
            system('cls')
            output_canal = " ".join(f"[green]{n}[/]" if n == self.canal+1 else str(n) for n in self.canais)
            print(Panel(
                f"Canal = {output_canal}\n"
                f"Volume = {':green_square:' * self.volume}{':white_large_square:' * (5 - self.volume)}"
                , title="[ TV ]", width=30
            ))

            resp = input("< CH > | - VOL + ")
            if resp == '@':
                self.tv_desligada()
            elif resp == '-':
                if self.volume > 1:
                    self.volume -= 1
            elif resp == '+':
                if self.volume < 5:
                    self.volume += 1
            elif resp == '<':
                if self.canal > 0:
                    self.canal -= 1
            elif resp == '>':
                if self.canal < 4:
                    self.canal += 1
            elif resp == 0:
                break
            else:
                print("[red]Comando inválido! Tente novamente[/]")
                input()
                continue
    
    # Método para mostrar a tv desligada
    def tv_desligada(self):
        while True:
            system('cls')
            print(Panel(
                "[red]A tv está desligada[/]"
                , title="[ TV ]", width=30
            ))

            resp = input("< CH > | - VOL + ")
            if resp == '@':
                self.tv_ligada()
            elif resp == 0:
                break
            else:
                print("[red]Comando inválido! Tente novamente[/]")
                input()
                continue

c1 = ControleRemoto()
