#Exercício Python 4:
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite alguma coisa no teclado: ')

print(f'Esse é o tipo primitivo do que você digitou: {type(valor)}')

print(f'Ele é um valor númerico? {valor.isnumeric()}')
print(f'Ele é um valor alfabético? {valor.isalpha()}')
print(f'Ele é um valor alfanúmerico? {valor.isalnum()}')
print(f'Ele está em minúsculo? {valor.islower()}')
print(f'Ele está em maiúsculo? {valor.isupper()}')
print(f'Ele está capitalizado? {valor.istitle()}')
print(f'Ele é somente espaços? {valor.isspace()}')
