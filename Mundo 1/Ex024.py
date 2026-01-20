#Exercício Python 24:
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite onde você nasceu: ')).strip().lower().split()

print('santo' in cidade[0])
