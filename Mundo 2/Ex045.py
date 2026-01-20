#Exercício Python 45:
#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('=====JOKENPO V1.0=====')
print('SUAS OPÇÕES:\n[1]PEDRA\n[2]PAPEL\n[3]TESOURA')

escolhapc = randint(1, 3)
escolhauser = int(input('Sua opção: '))
escolhas = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)


if escolhapc == escolhauser: #caso de empate
    print(f'EMPATE! Ambos escolheram {escolhas[escolhauser]}')
elif escolhapc > escolhauser: #caso o valor do computador seja maior
    if escolhapc == 3 and escolhauser == 1:  #caso especifico de tesoura perder para pedra
        print(f'VOCÊ VENCEU! O computador jogou {escolhas[escolhapc]} e você jogou {escolhas[escolhauser]}')
    else:
        print(f'VOCÊ PERDEU! O computador jogou {escolhas[escolhapc]} e você jogou {escolhas[escolhauser]}')
else: #caso o valor do usuario seja maior
    if escolhauser == 3 and escolhapc == 1:  #caso especifico de tesoura perder para pedra
        print(f'VOCÊ PERDEU! O computador jogou {escolhas[escolhapc]} e você jogou {escolhas[escolhauser]}')
    else:
        print(f'VOCÊ VENCEU! O computador jogou {escolhas[escolhapc]} e você jogou {escolhas[escolhauser]}')
