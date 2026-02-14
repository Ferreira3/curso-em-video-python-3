# Desafio 21

from rich import print

class Caneta:
    
    cores = {
        'vermelha': 'red',
        'azul': 'blue',
        'preta': 'black',
        'verde': 'green'
    }

    def __init__(self, cor):
        self.cor = Caneta.cores[cor]
        self.cor_nome = cor
        self.caneta_aberta = False
    
    def destampar(self):
        self.caneta_aberta = True
    
    def escrever(self, texto):
        if self.caneta_aberta == True:
            print(f"[{self.cor}]{texto}[/{self.cor}]", end='')
        else:
            print(f"A [{self.cor}]caneta {self.cor_nome}[/{self.cor}] está tampada!", end='')

    def quebrar_linha(self, n_linhas):
        print('\n'  * n_linhas)


c1 = Caneta('azul')
c1.destampar()
c1.escrever("Testando caneta azul")
c1.quebrar_linha(1)

c2 = Caneta('verde')
c2.escrever("Testando caneta verde fechada")

c3 = Caneta('vermelha')
c3.destampar()
c3.quebrar_linha(1)
c3.escrever("Caneta vermelha disponível!")
