#Exercício Python 17:
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Qual o comprimento do cateto oposto? '))
adja = float(input('Qual o comprimento do cateto adjacente? '))
hipot = hypot(oposto, adja)

print(f'A hipotenusa vai medir: {hipot:.2f}!')
