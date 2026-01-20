#Exercício Python 041:
#A Confederação Nacional de Natação precisa de um programa que leia o
#ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date

anoatual = date.today().year
anonasc = int(input('Ano de nascimento do atleta: '))
idade = anoatual - anonasc

print(f'O atleta tem {idade} anos e competirá na categoria:')

if idade < 10:
    print('MIRIM')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JUNIOR')
elif idade < 26:
    print('SENIOR')
else:
    print('MASTER')
