#Exercício Python 58:
#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

numrand = randint(0, 10)
tentativas = 1

print('Vou pensar em um número de 0 a 10...')
escolhido = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(1)

while escolhido != numrand:
    if escolhido > numrand:
        escolhido = int(input('Escolhi um número menor... Tente novamente! '))
    else:
        escolhido = int(input('Escolhi um número maior... Tente novamente! '))
    
    tentativas += 1

print(f'Você acertou! Eu pensei no número {numrand}!')
print(f'Você acertou depois de tentar {tentativas} vezes!!')
