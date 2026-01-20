#Exercício Python 25:
#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o seu nome completo: ')).lower()

if 'silva' in nome.split():
    print('Seu nome contém silva!')
else:
    print('Seu nome não contém silva')
