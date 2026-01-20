#Exercício Python 39:
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoatual = date.today().year
anonasc = int(input('Digite o ano de nascimento: '))
idade = anoatual - anonasc

print(f'Quem nasceu em {anonasc} terá {idade} em {anoatual}!')

if idade == 18:
    print(f'Você deve se alistar ainda este ano!')
elif idade < 18:
    print(f'Você deverá se alistar somente em {anoatual + (18 - idade)}!')
else:
    print(f'Você já deveria ter se alistado em {anoatual - (idade - 18)}!')
