#Exercício Python 63:
#Escreva um programa que leia um número N inteiro qualquer e mostre na tela
#os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('||||||FIBONACCI V1.0||||||\n')

num = int(input('Quantos termos quer mostrar? '))
prim = 0
seg = 1
atual = prim + seg

while num > 0:
    num -= 1
    print(atual,end=' > ')
    atual = prim + seg
    prim = seg
    seg = atual

print('FIM!')
