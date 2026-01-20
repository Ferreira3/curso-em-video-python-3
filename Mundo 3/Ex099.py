#Exercício Python 99:
#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    print("-" * 40)
    print("Analisando os valores recebidos...")
    for i in num:
        print(i, end=' ', flush=True)
        sleep(0.3)
    print(f"\nO maior valor encontrado em {num} foi {max(num)}")


maior(1, 3, 7)
maior(0)
maior(8, 7, 3, 0, 1, 2, 4)
maior(7, 7, 7, 81, 23, 14)
