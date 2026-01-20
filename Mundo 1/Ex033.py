#Exercício Python 33:
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

listanums = sorted([n1, n2, n3])

print(f'O menor número é {listanums[0]} e o maior número é {listanums[-1]}!')
