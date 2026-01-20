#Exercício Python 74:
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

nums = (randint(1, 100), randint(1, 100), randint(1, 100),
        randint(1, 100), randint(1, 100))

print(f"Valores da tupla: {nums}")
print(f"O menor valor é {min(nums)} e o maior {max(nums)}!")
