#Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número qualquer: '))
conversao = int(input('Você gostaria de converter ele para:\n[1]Binário\n[2]Octal\n[3]Hexadecimal\nRespota: '))

if conversao == 1:
    print(f'{num} em Binário é = {bin(num)[2:]}')
elif conversao == 2:
    print(f'{num} em Octal é = {oct(num)[2:]}')
elif conversao == 3:
    print(f'{num} em Hexadecimal é = {hex(num)[2:]}')
else:
    print('Você não digitou um número válido!')
