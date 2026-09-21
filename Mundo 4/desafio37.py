# Desafio 37

from rich import print
from rich.panel import Panel

class Mensagem():
    def __init__(self, msg:str = None):
        self._mensagem = msg
        self._icone = ':bell:'
        self._tipo = 'AVISO'
        self._cores = ('bold black', 'white')

    def mostrar(self):
        texto_cor = self._cores[0]
        fundo_cor = self._cores[1]

        print(
            Panel(
                f"[{texto_cor}]{self._mensagem}[/]",
                title=f"[{texto_cor}]{self._tipo}[/]",
                subtitle=f"{self._icone}",
                border_style=texto_cor,
                style=f"on {fundo_cor}",
                expand=False,
                safe_box=False
            )
        )


class Alerta(Mensagem):
    def __init__(self, msg = None):
        super().__init__(msg)
        self._icone = ':warning:'
        self._tipo = 'ALERTA'
        self._cores = ('bold black', 'yellow')


class Erro(Mensagem):
    def __init__(self, msg = None):
        super().__init__(msg)
        self._icone = ':no_entry:'
        self._tipo = 'ERRO'
        self._cores = ('bold white', 'red')


m1 = Mensagem('Olá, Mundo!').mostrar()
m2 = Alerta('Seu saldo está esgotando. Garanta acesso realizando uma recarga agora mesmo.').mostrar()
m3 = Erro('ERRO: Seu usuário não possui essa permissão').mostrar()
