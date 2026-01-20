#Exercício Python 46:
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from datetime import date
from time import sleep

anoatual = date.today().year

print(f'Contagem regressiva para o fim de {anoatual}!')

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print(f'FELIZ ANO NOVO!!!\nSEJA BEM-VINDO A {anoatual + 1}!!!')
