#Exercício Python 038:
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro valor é MAIOR!')
elif num1 < num2:
    print('O segundo valor é MAIOR!')
else:
    print('Os dois valores são IGUAIS!')
