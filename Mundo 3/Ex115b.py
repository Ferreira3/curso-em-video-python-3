#Exercício Python 115b:
#Vamos ver como fazer acesso a arquivos usando o Python.

from exer115.lib.interface import *
from time import sleep

try:
    with open('arquivo.txt', 'x') as arquivo:
        print("Lista criada!")
except:
    with open('arquivo.txt', 'r') as arquivo:
        print("Lista aberta!")

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        cabecalho("LISTA DE PESSOAS")
        with open('arquivo.txt', 'r') as arquivo:
            print(arquivo.read())
    elif resp == 2:
        cabecalho("Opção 2")
    elif resp == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida!")
    sleep(1)
