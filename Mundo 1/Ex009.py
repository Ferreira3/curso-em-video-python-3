#Exercício Python 9:
#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número para obter sua tabuada: '))

for i in range(11):
    print(f'{n1} x {i:2} = {n1*i}')
