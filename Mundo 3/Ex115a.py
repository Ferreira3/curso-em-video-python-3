#Exercício Python 115a:
#Vamos criar um menu em Python, usando modularização.

from exer115.lib.interface import *
from time import sleep

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        cabecalho("Opção 1")
    elif resp == 2:
        cabecalho("Opção 2")
    elif resp == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida!")
    sleep(1)
