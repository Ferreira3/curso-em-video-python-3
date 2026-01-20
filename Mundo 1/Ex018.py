#Exercício Python 18:
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

num = int(input('Digite um ângulo: '))
ang = radians(num)

print(f'O ângulo de {num} tem o SENO de {sin(ang):.2f}!')
print(f'O ângulo de {num} tem o COSSENO de {cos(ang):.2f}!')
print(f'O ângulo de {num} tem a TANGENTE de {tan(ang):.2f}!')
