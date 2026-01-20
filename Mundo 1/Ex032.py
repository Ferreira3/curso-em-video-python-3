#Exercício Python 32:
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

anoatual = date.today().year
ano = int(input('Digite um ano qualquer (ou 0 para analisar o ano atual): '))

if ano == 0:
    ano = anoatual

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')
