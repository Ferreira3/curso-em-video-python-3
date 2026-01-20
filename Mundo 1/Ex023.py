#Exercício Python 23:
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input('Informe um número: '))

print(f'Unidade: {num[len(num)-1]}')

if len(num) > 1:
    print(f'Dezena: {num[len(num)-2]}')
else:
    print(f'Dezena: 0')

if len(num) > 2:
    print(f'Centena: {num[len(num)-3]}')
else:
    print(f'Centena: 0')

if len(num) > 3:
    print(f'Milhar: {num[len(num)-4]}')
else:
    print(f'Milhar: 0')
