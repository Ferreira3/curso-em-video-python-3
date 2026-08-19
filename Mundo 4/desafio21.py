# Desafio 21

from rich import print

class Caneta:
    
    CORES = {
        'vermelha': 'red',
        'azul': 'blue',
        'preta': 'black',
        'verde': 'green'
    }

    def __init__(self, cor):
        self.cor_nome = cor if cor in Caneta.CORES else 'preta'
        self.cor_codigo = Caneta.CORES[self.cor_nome]
        self.aberta = False
    
    def destampar(self):
        self.aberta = True
    
    def escrever(self, texto):
        if self.aberta:
            print(f"[{self.cor_codigo}]{texto}[/{self.cor_codigo}]", end='')
        else:
            print(f"A [{self.cor_codigo}]caneta {self.cor_nome}[/{self.cor_codigo}] está tampada!", end='')

    def quebrar_linha(self, n_linhas):
        print('\n' * n_linhas)


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
