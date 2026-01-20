#Exercício Python 54:
#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoatual = date.today().year
contmaior = 0
contmenor = 0

for i in range(1, 8):
    anonasc = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    if (anoatual - anonasc) >= 18:
        contmaior += 1
    else:
        contmenor += 1

print(f'Ao total tivemos {contmaior} pessoas de maiores de idade \ne também tivemos {contmenor} pessoas de menores de idade!')
