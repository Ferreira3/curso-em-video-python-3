#Exercício Python 060:
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

valor = int(input('Digite um número para calcular seu fatorial: '))
total = 1
total2 = factorial(valor)

while valor > 1:
    total = total * valor
    print(f'total {total}')
    valor -= 1

print(f'Total via while: {total}')
print(f'Total via função factorial: {total2}')
