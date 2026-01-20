#Exercício Python 35:
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
