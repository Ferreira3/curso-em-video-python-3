#Exercício Python 52:
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
cont = 0
cores = {'azul':'\033[34m',
         'vermelho':'\033[31m'}

for i in range(1, num+1):
    if num % i == 0:
        cont += 1
        print(f'{cores['azul']}{i}',end=' ')
    else:
        print(f'{cores['vermelho']}{i}',end=' ')

if cont == 2:
    print(f'\n{cores['azul']}O NÚMERO DIGITADO É PRIMO!')
else:
    print(f'\n{cores['vermelho']}O NÚMERO DIGITADO NÃO É PRIMO!')
