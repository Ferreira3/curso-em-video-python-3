#Exercício Python 28:
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numrand = randint(0, 5)

print('Vou pensar em um número de 0 a 5...')
escolhido = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)

if numrand == escolhido:
    print(f'Você acertou! Eu pensei no número {numrand}!')
else:
    print(f'Você errou! Eu pensei no número {numrand} e você escolheu o {escolhido}!')
