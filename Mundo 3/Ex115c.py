#Exercício Python 115c:
#Vamos finalizar o projeto de acesso a arquivos em Python.

from exer115.lib.interface import *
from time import sleep

abrirArquivo('arquivo.txt')

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerArquivo('arquivo.txt')
    elif resp == 2:
        cadastrarPessoa('arquivo.txt')
    elif resp == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida!")
    sleep(1)
